import time
from setuptools import setup

setup(
    name='webapp',
    version=time.strftime('%Y.%m.%d'),
    author='webapp',
    author_email='info@webapp.com',
    packages=['webapp'],
    include_package_data=True,
    description='Web App',
)