"""Package recipe."""

import setuptools


setuptools.setup(
    name='openvpn-mintotp',
    version='0.0.1',
    author='Oleg Pykhalov',
    author_email='go.wigust@gmail.com',
    description='OpenVPN with authentication via MinTOTP',
    url='https://github.com/kitnil/openvpn-mintotp',
    license='GPLv3+',

    dependency_links=['https://github.com/susam/mintotp/tarball/0.3.0#egg=mintotp-0.3.0'],
    install_requires=[
        'pexpect',
        'mintotp',
    ],

    py_modules=['openvpn_otp'],
    entry_points={
        'console_scripts': {
            'openvpn-mintotp = openvpn_otp:main'
        }
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],

    keywords='openvpn totp hotp otp hmac cryptography 2fa authenticator',
)
