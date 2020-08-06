#  __*_coding:utf-8_*_
# Time :        2020/8/4 23:58
# Author:       LeiLei
# File:         MainApp.py
# Software:     PyCharm
import sys
from PyQt5.QtWidgets import QApplication
from login.Login import *
from StudentManage.student.Student import Student


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stu = Student()
    login = Login(stu=stu)
    login.show()
    sys.exit(app.exec_())
