# Description

This project allows to connect to OpenVPN with automatic typing OTP code.

# Installation requirements

You need to install the following Python libraries:

- [mintotp](https://github.com/susam/mintotp)
- [pexpect](https://github.com/pexpect/pexpect)

Also, make sure OpenVPN is available in the PATH environment variable.

`OPENVPN_CONFIG_FILE` should point to an OpenVPN configuration file.

`OPENVPN_OTP_SECRET_FILE` should point to an OTP secret phrase.
