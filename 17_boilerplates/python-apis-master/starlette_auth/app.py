import base64
import binascii

from starlette.applications import Starlette
from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    SimpleUser,
    UnauthenticatedUser,
    AuthCredentials,
    requires
)
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse

import uvicorn


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here,
        #       possibly by installing `DatabaseMiddleware`
        #       and retrieving user information from `request.database`.
        if username == 'user' and password == 'password':
            value = 'authenticated'
        else:
            value = 'unauthorzed'
        return AuthCredentials([value]), SimpleUser(username)


app = Starlette()
app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend())


@app.route('/')
async def homepage(request):
    if request.user.is_authenticated:
        return PlainTextResponse('hello, ' + request.user.display_name)
    return PlainTextResponse('hello, you')


@app.route('/dashboard')
@requires('authenticated', redirect='homepage')
async def dashboard(request):
    return PlainTextResponse('Dashboard')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
