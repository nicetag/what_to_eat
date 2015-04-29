#! /usr/bin/env python
# -*- coding=utf-8 -*-

import sys
import os
import sqlite3

if os.path.exists(sys.path[0]+"/Store.db"):
    conn = sqlite3.connect(sys.path[0] + '/Store.db')
else:
    sqlite3.connect(sys.path[0] + '/Store.db')
    conn = sqlite3.connect(sys.path[0] + '/Store.db')
    with conn:
        conn.execute('''create table storelist (store_id char(4) not null, 
            StoreName varchar(77) not null, 
            StoreAddress varchar(77) not null, 
            primary key (store_id));''')


'''
try:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
except ImportError:
    try:
        import pyqt4
    except ImportError:
        GuiModule = "None"
    else:
        GuiModule = "pyqt4"
else:
    GuiModule = "simplegui"
finally:
    print(GuiModule)'''