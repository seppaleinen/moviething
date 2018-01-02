from setuptools import setup
from setuptools_behave import behave_test

    
setup(
    name='moviething',
    version='1.0.0',
    author='David Eriksson',
    author_email='davidbaeriksson@gmail.com',
    packages=[ 'src' ],
    scripts=[ 'scripts/binfile' ],
    url='www.google.se',
    zip_safe=False,
    license='GPLv3',
    description='Comparing watchlist to movie',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'behave = behave.__main__:main'
        ],
        'distutils.commands': [
            'behave_test = setuptools_behave:behave_test'
        ]
    },
    tests_require=[
        "behave==1.2.5", "nose>=1.3"
    ],
    test_suite='nose.collector',
    cmdclass = {
        "behave_test": behave_test,
    },
)


