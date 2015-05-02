#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

try:
    from PyQt4 import QtCore, QtGui, uic   
except ImportError:
    print("没有Qt模块，将在命令行操作")
    os.system("python " + sys.path[0] + "/main.py")
    os._exit(0)

from StoreData import store_list, all_store, store_init, add_new_store
from main import main

qtCreatorFile = sys.path[0] + "/UIView.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    """define UI init"""
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.viewlist()

    def viewlist(self):
        ss = "\n".join([st[1] for st in store_list])
        self.StoreListView.setText(ss)

class what_to_eat(MyApp):
    """操作部分"""
    def __init__(self):
        super(what_to_eat, self).__init__()
        self.pushButton.clicked.connect(self.result)
        self.pushButton_2.clicked.connect(self.add)

    def result(self):
        self.resultBrowser.setText(main(1).decode("utf-8"))

    def add(self):
        a = store_init()
        a.name = self.newst.toPlainText()
        a.address = self.newadd.toPlainText()
        if a.name:
            add_new_store(a)
        else:
            pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = what_to_eat()
    window.show()
    sys.exit(app.exec_())