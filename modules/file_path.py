#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def test_file_path(path, hostname):
    try:
        output = subprocess.check_output(["ssh", hostname, "ls", path])    
        print(output)
        return True
    except:
        return False

if __name__ == "__main__":
    test_file_path("~/test.txt", "dmc-gate1")
