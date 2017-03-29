#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def test_hostname(hostname):
    output = subprocess.check_output(["ssh", hostname, "hostname"])    
