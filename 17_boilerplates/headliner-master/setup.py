import os
import pathlib
from setuptools import (
    setup,
    find_packages
)

os.chdir(pathlib.Path(__file__).parent.absolute())
import headliner

setup(
    name='headliner',
    version=headliner.__version__,
    description='Summary of URL elements',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Documentation",
    ],
    keywords='headliner',
    author='alecor Dev',
    author_email='alecor.dev@gmail.com',
    maintainer='alecor Dev',
    maintainer_email='alecor.dev@gmail.com',
    url='https://github.com/alecordev',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'headliner = headliner.headliner:cli',
        ]
    },
    install_requires=[
        'requests-html',
    ]
)