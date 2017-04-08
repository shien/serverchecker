#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import target

test_name = "hostname"

#
# check host name
#

def test_hostname(target):
    output = subprocess.check_output(["ssh", target.connection_name, "hostname"])    
    hostname = target.get_test_contents(test_name) + "\n"
    if output == hostname:
        return True
    return False

if __name__ == "__main__":
    target = target.Target("test_file/test_hostname.json")
    if test_hostname(target):
        print("[Passed]")
    else:
        print("[Failed]")
