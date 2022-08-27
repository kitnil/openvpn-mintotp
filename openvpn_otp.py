#!/usr/bin/env python3

"""OpenVPN wrapper with OTP authentication."""

import os
import sys
from pathlib import Path

import mintotp
import pexpect


def main():
    """Entrypoint."""
    child = pexpect.spawn(f"openvpn --config {os.environ['OPENVPN_CONFIG_FILE']}")
    child.logfile = sys.stdout.buffer
    child.expect("CHALLENGE: Verification code:")
    child.sendline(
        mintotp.totp(Path(os.environ["OPENVPN_OTP_SECRET_FILE"]).read_text())
    )
    # macos - python script: pexpect hangs on child.wait()? - Stack Overflow
    # https://stackoverflow.com/questions/58751357/python-script-pexpect-hangs-on-child-wait
    while True:
        try:
            child.read_nonblocking()
        except Exception:
            break
    if child.isalive():
        child.wait()


if __name__ == "__main__":
    main()
