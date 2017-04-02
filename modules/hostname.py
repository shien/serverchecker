#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def test_hostname(hostname):
    output = subprocess.check_output(["ssh", hostname, "hostname"])    
    hostname = hostname + "\n"
    if output == hostname:
        return True
    return False

if __name__ == "__main__":
    if test_hostname("dmc-gate1"):
        print("[Passed]")
    else:
        print("[Failed]")
