#! /usr/bin/env python
# -*- coding=utf-8 -*-

import click

class store_init(object):
    """basic store class"""
    def __init__(self):
        pass

    def name(self, argv):
        self.name = argv

    def address(self, argv):
        self.address = argv

store_list = ["老家", "麦当劳", "拉面", "麻辣烫"]

def add(s):
    global store_list
    store_list.append(s)