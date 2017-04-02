#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

#
# check host name
#

def test_hostname(hostname):
    output = subprocess.check_output(["ssh", hostname, "hostname"])    
    hostname = hostname + "\n"
    if output == hostname:
        return True
    return False

if __name__ == "__main__":
    if test_hostname("test-server"):
        print("[Passed]")
    else:
        print("[Failed]")
