from setuptools import setup, find_packages
from os.path import join, dirname
import helloworld

setup(
    name='helloworld',
    version=helloworld.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts': [
            'helloworld = helloworld.core:print_message',
            'serve = helloworld.web:run_server',
        ]
    },
    install_requires=[
        'Flask==0.8'
    ],
    include_package_data=True,
    test_suite='tests'
)
