#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def test_gateway():
    output = subprocess.check_output(["ssh", hostname, "/sbin/ip", "route"])    
