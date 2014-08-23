import sys

if sys.version_info.major < 3:
    print('Python 3 is required')
    sys.exit()

from setuptools import setup, find_packages

setup(
    name='codeforces_api',
    version='0.1a',
    description='Wrapper library for Codeforces API',
    license='MIT',
    keywords='codeforces api wrapper',
    url='https://github.com/soon/CodeforcesAPI',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],

    install_requires=['enum34'],

    author='Andrew Kuchev',
    author_email='0coming.soon@gmail.com',

    test_suite='tests'
)
