import os
import base64
import hashlib
import datetime
import functools

from flask import (
    Flask,
    render_template,
    jsonify,
    url_for,
    redirect,
    request,
    session,
    flash,
    abort
)

import init
from tasks import add

init.init()
logger = init.logger

app = Flask('Portal',
            template_folder=os.path.join(init.here, 'templates'),
            static_folder=os.path.join(init.here, 'static'))
app.secret_key = 'secret key'


@app.before_request
def csrf_protect():
    """
    For each request, checks if its a POST HTTP request, and checks for the CSRF TOKEN
    in the current session as a mitigation for CSRF attacks.

    Returns:
        redirect
    """
    if request.method == 'POST':
        token = session.pop('_csrf_token', None)
        if not token:
            logger.debug('No CSRF token in session')
            abort(400)
        elif request.json:
            _csrf_token = request.json.get('_csrf_token')
            if token != _csrf_token:
                logger.debug('Invalid CSRF token received')
                logger.debug('{token} expected and received {_csrf_token}'.format(**locals()))
                abort(400)
        elif token != request.form.get('_csrf_token'):
            logger.debug('Invalid CSRF token received in the form')
            logger.debug('Expected {} and received {}'.format(token, request.form.get('_csrf_token')))
            abort(400)
        else:
            logger.debug('CSRF valid.')


def generate_csrf_token():
    """
    Generates CSRF tokens for the forms.

    Returns:
        str
    """
    if '_csrf_token' not in session:
        token = base64.b64encode(os.urandom(42)).decode()
        logger.debug('Setting CSRF token: {token}'.format(**locals()))
        session['_csrf_token'] = token
    return session['_csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token


def generate_hash(password=None, salt=None):
    """
    Generates a salted hash from a password.

    Helps create new users.

    Args:
        password (str): Password to hash.
        salt (str): Salt string.

    Returns:
        str
    """
    if not password:
        raise Exception('Password needs to be provided.')
    if not salt:
        # salt = secrets.token_bytes(32) py36
        salt = os.urandom(32)
    hashed_password = hashlib.pbkdf2_hmac('sha512', password.encode(), salt, 100000)
    return '{impl}${iterations}${salt}${pwd}'.format(impl='pbkdf2_hmac_sha512',
                                                     iterations=100000,
                                                     salt=base64.b64encode(salt).decode(),
                                                     pwd=base64.b64encode(hashed_password).decode())


def authenticate(user, password):
    """
    Authenticates a user:password combination.

    Args:
        user (str): Username
        password (str): Password

    Returns:
        bool - True if successfully authenticated
    """
    if user in init.credentials:
        hashed_password = init.credentials.get(user)
        salt = hashed_password.split('$')[2]
        return generate_hash(password=password, salt=base64.b64decode(salt)) == hashed_password
    else:
        return False


# Ensures and redirects unauthenticated users
def login_required(f):
    @functools.wraps(f)
    def decorated_view(*args, **kwargs):
        if not session.get('logged_in'):
            logger.debug(
                'User not authenticated - cannot access requested page.')
            flash('You need to log in to access the requested resource.',
                  'alert alert-warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_view


# Validates simple auth authentication against and endpoint. Used for REST requests.
def rest_requires_simple_auth(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not authenticate(auth.username, auth.password):
            return abort(401)
        return f(*args, **kwargs)
    return decorated


@app.context_processor
def version_processor():
    """ Allows the keys returned to be global variables inside all templates """
    timestamp = datetime.datetime.fromtimestamp(os.path.getctime(__file__)).strftime('%Y%m%d - %H:%M:%S')
    version = os.getenv('PORTAL_VERSION') or '1.0.0'
    return dict(timestamp=timestamp, version=version)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login endpoint. Handles the login form and sets up the session if valid credentials are provided.

    Expects to receive:

    - username
    - password
    """
    if request.method == 'POST':
        password = request.form.get('password')
        user = request.form.get('username')
        failed_auth_msg = 'Wrong username and/or password.'

        if user not in init.credentials:
            logger.info(failed_auth_msg)
            flash(failed_auth_msg, 'alert alert-danger')
            return redirect(url_for('login'))
        else:
            if authenticate(user, password):
                logger.info('Authentication successful for user {}.'.format(user))
                session['logged_in'] = user
                flash('Logged in', 'alert alert-success')
                return redirect(url_for('index'))
            else:
                logger.info(failed_auth_msg)
                flash(failed_auth_msg, 'alert alert-danger')
                return redirect(url_for('login'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    user = session['logged_in']
    session['logged_in'] = False
    logger.debug('{} logged out.'.format(user))
    flash('Logged out.', 'alert alert-success')
    return redirect(url_for('index'))


@app.errorhandler(400)
def bad_request(e):
    """ HTTP 400 error """
    return render_template('errors/400.html'), 400


@app.errorhandler(401)
def unauthorized(e):
    """ HTTP 401 error """
    return render_template('errors/401.html'), 401


@app.errorhandler(403)
def invalid_auth(e):
    """ HTTP 403 error """
    return render_template('errors/403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    """ HTTP 404 error """
    return render_template('errors/404.html'), 404


@app.errorhandler(405)
def method_not_allowed(e):
    """ HTTP 405 error """
    return render_template('errors/405.html'), 405


@app.errorhandler(500)
def internal_server_error(e):
    """ HTTP 500 error """
    return render_template('errors/500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/background')
def background_task():
    task = add.apply_async(args=[10, 20])
    return redirect(url_for('taskstatus', task_id=task.id))
    # return jsonify({'Location': url_for('taskstatus', task_id=task.id)})


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = add.AsyncResult(task_id)
    print(task_id)
    print(task.state)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'result': task.result,
            # 'current': task.info.get('current', 0),
            # 'total': task.info.get('total', 1),
            # 'status': task.info.get('status', '')
        }
        # print(dir(task))
        # if 'result' in task.info:
        #     response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)


def run():
    app.run(host='0.0.0.0', port=8282, debug=True, threaded=True)


if __name__ == '__main__':
    run()
