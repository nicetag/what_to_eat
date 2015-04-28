#! /usr/bin/env python
# -*- coding=utf-8 -*-

import sqlite3
from __init__ import conn

class store_init(object):
    """basic store class"""
    def __init__(self):
        pass

    def name(self, argv):
        self.name = argv

    def address(self, argv):
        self.address = argv

def input_store_name():
    store_name = raw_input("去哪家店吃的？（店名）")
    srore_address = raw_input("店的地址是？（直接回车可省略）")
    a = store_init()
    a.name(store_name)
    if store_name:
        a.address(srore_address)
    add_new_store(a)

def do_sql(strr):
    with conn:
        cur = conn.execute(strr)
    return cur

store_list = list(do_sql('''select store_id,StoreName from storelist;'''))
all_store = list(do_sql('''select * from storelist;'''))

def add_new_store(s):
    try:
        do_sql('''insert into storelist values ("{id}", "{name}", "{addres}");'''
            .format(id = len(store_list)+1, name = s.name, addres = s.address))
    except:
        do_sql('''insert into storelist values ("{id}", "{name}",);'''
            .format(id = len(store_list)+1, name = s.name))