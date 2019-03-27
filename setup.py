import sys

if sys.version_info.major < 3:
    print('Python 3 is required')
    sys.exit()

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

from setuptools import setup, find_packages

setup(
    name='codeforces_api',
    version='0.3.3',
    description='Wrapper library for Codeforces API',
    license='MIT',
    keywords='codeforces api wrapper',
    url='https://github.com/soon/CodeforcesAPI',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples']),
    classifiers=[
        'Development Status :: 4 - Beta',
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
