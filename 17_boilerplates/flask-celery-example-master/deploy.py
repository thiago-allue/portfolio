""" Deployment utility

Uses paramiko to SSH into boxes and perform operations remotely.

It expects 4 environment variables to be set up:

- QPROXY
- QPORT
- QUSER
- QPASSWD

If they are blank or evaluated to None (non-existent), the execution will interactively ask for them.
"""

import os
import sys
import glob
import shutil
import logging
import subprocess
import getpass
import argparse
import paramiko


logging.getLogger('paramiko').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] - %(message)s')


here = os.path.dirname(os.path.abspath(__file__))
logging.info(here)


class ConnectToServer:
    """
    Connects to remote server using user:password combination or key.

    It provides a context manager, interactive prompts for required details, and parameterisation of the connection details.

    Returns:
        paramiko.SSHClient - connected
    """

    def __init__(self, host=None, port=None, username=None, password=None, key_filename=None):

        if host is None:
            self.host = os.getenv('QPROXY')
        if not self.host:
            self.host = input('Host IP address or hostname: ')

        if port is None:
            self.port = os.getenv('QPORT')
        if not self.port:
            self.port = 22

        if username is None:
            self.username = os.getenv('QUSER')
        if not self.username:
            self.username = input('Username to authenticate against remote host: ')

        if password is None:
            self.password = os.getenv('QPASSWD')
        if not self.password:
            if not key_filename:
                self.password = getpass.getpass('Password for user: ')
                if not self.password:
                    raise Exception('No password and no key provided')

        self.client = paramiko.SSHClient()

        if not key_filename:
            self.client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
            self.key_filename = None
        else:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.key_filename = key_filename

    def __enter__(self):
        self.client.connect(self.host, self.port, self.username,
                            self.password, timeout=5, key_filename=self.key_filename)
        return self.client

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()


def build_the_portal(python='python3'):
    """
    Cleans the temporary directories (if present) generated upon build of Python package and regenerates them.

    Parameters
    ----------
    python: str
        Executable to install the package on.

    Returns
    -------
    None
    """
    shutil.rmtree('build', ignore_errors=True)
    shutil.rmtree('dist', ignore_errors=True)
    shutil.rmtree('the_Portal.egg-info', ignore_errors=True)

    subprocess.call('python setup.py bdist_wheel', shell=True, cwd=here)
    for f in glob.glob('dist/*.whl'):
        logging.info('Copying: {}'.format(os.path.basename(f)))
        remote_copy(f, '/home/user/tmp/{}'.format(os.path.basename(f)))

    logging.info(remote_command('{} -m pip uninstall -y the-Portal'.format(python)))
    logging.info(remote_command('{} -m pip install the-Portal --no-index -f /home/user/tmp'.format(python)))


def progress(transferred, total_transfer):
    """
    In the console, it works as a visual progress indicator. 0.00% -> 100.00%
    """
    print('Progress: {:.2f} %\r'.format((transferred / total_transfer) * 100), end='\r')
    sys.stdout.flush()


def remote_copy(local_location, remote_location):
    """
    Copies files through SSH/SFTP.

    Parameters
    ----------
    local_location: str
        Local file
    remote_location
        Remote file

    Returns
    -------
    None
    """
    with ConnectToServer() as client:
        sftp = client.open_sftp()
        logging.info('Copying {local_location} to {remote_location}'.format(**locals()))
        sftp.put(local_location, remote_location, callback=progress)


def remote_command(cmd):
    """
    Executes a command in a remote server.

    Parameters
    ----------
    cmd: str
        Command line to send and execute in the remote server.

    Returns
    -------
    str
        stdout from remote command
    """
    logging.debug('Sending command: {}'.format(cmd))
    results = {}
    with ConnectToServer() as client:
        res = client.exec_command(cmd)
        results[cmd] = {}
        for i, output in enumerate(res):
            try:
                t = output.read().decode()
            except:
                # if stdin is empty raises exception
                pass
            else:
                key = {0: 'stdin', 1: 'stdout', 2: 'stderr'}
                results[cmd][key[i]] = t
    return results[cmd]['stdout']


class CIBuilder:
    def __init__(self):
        pass

    def update_password(self):
        self.password = getpass.getpass()

    def add_step(self):
        pass

    def remove_step(self):
        pass


if __name__ == '__main__':
    try:

        parser = argparse.ArgumentParser()
        parser.add_argument('--automation', action='store_true', help='Deploy the Portal', default=True)
        args = parser.parse_args()

        # if len(sys.argv) < 2:
        #     parser.print_help()
        #     sys.exit(0)

        if args.automation:
            python1 = 'python3'
            pythons = [python1]
            for python in pythons:
                build_the_portal(python)

    except Exception as e:
        logging.exception('Error')
