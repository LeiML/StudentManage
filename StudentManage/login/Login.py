#  __*_coding:utf-8_*_
# Time :        2020/8/4 23:57
# Author:       LeiLei
# File:         Login.py
# Software:     PyCharm
import datetime
from PyQt5.QtWidgets import QWidget, QMessageBox
import mysql.connector as mc
from StudentManage.frame.login import Ui_Form
from StudentManage.config import *


class Login(QWidget, Ui_Form):
    def __init__(self, stu):
        super(Login, self).__init__()
        self.setupUi(self)
        self.conn = mc.connect(user='Lei', password='1314520', host='localhost', db='study')
        self.cursor = self.conn.cursor()
        self.stu = stu
        self.path = './logs.txt'
        if not self.conn.is_connected():
            QMessageBox.warning(self, "警告", "无法连接到服务器", QMessageBox.Ok)
        self.read_log()
        self.lineEdit_2.setText('123456')

    def read_log(self):
        with open(self.path, 'r')as f:
            line = f.readline(-1)
        self.lineEdit.setText(line.split('\t')[1])

    def save_log(self, line):
        with open(self.path, 'a')as f:
            f.write(line)

    def login(self):
        user_name = self.lineEdit.text()
        user_pass = self.lineEdit_2.text()
        user_identity = self.comboBox.currentText()
        command = "select * from %s where user_name='%s' and user_password='%s' and user_identity='%s';" \
                  % (TABLE_NAME, user_name, user_pass, user_identity)
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        if len(result):
            self.cursor.close()
            self.conn.close()
            self.stu.show()
            time = datetime.datetime.now()
            line = str(time).split('.')[0] + "\t" + user_name + "\t" + user_pass + "\t" + user_identity + "\n"
            self.save_log(line)
            self.close()
        else:
            QMessageBox.warning(self, "警告", '您输入的账号密码有误', QMessageBox.Ok)
