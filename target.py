#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

SERVER_CHECKER_MARK = "serverchecker"

class Target:
    def __init__(self, target_file):
        self.connection_name = ""
        self.data = {}
        self.read_target_data(target_file)

    def read_target_data(self, target_file):
        tmp_data = ""
        try:
            with open(target_file, 'r') as fd:
                tmp_data = json.load(fd)
        except:
            print("open failed: " + target_file)
            pass
        if SERVER_CHECKER_MARK not in tmp_data:
            exit(1)
        self.data = tmp_data[SERVER_CHECKER_MARK]
        self.connection_name = self.data["connection_name"]

    def __add_data(self, key, data):
        self.data.update({key: data})

    def get_test_contents(self,key):
        return self.data["test"]

    def get_connection_name(self):
        return self.connection_name

if __name__ == "__main__":
    target = Target("test_file/targetname1.json")
    print(target.get_test_contents("default_gateway"))
    print(target.get_connection_name())

