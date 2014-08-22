from setuptools import setup

setup(
    name='codeforces_api',
    version='0.1a1.dev',
    description='Wrapper library for Codeforces API',
    license='MIT',
    keywords='codeforces api wrapper',
    url='https://github.com/soon/CodeforcesAPI',
    packages=['codeforces'],
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