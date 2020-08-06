# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1263, 861)
        Form.setStyleSheet("#Form{background-color: rgb(153, 247, 255);}\n"
"")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabWidget.setStyleSheet("QTabWidget{background-color: rgb(0, 150, 250);}\n"
"QTabBar::tab:selected{background-color: rgb(255, 100, 10);}\n"
"#tab{background-color: rgb(153, 247, 255);}\n"
"#tab_2{background-color: rgb(153, 247, 255);}\n"
"#tab_3{background-color: rgb(153, 247, 255);}\n"
"#tab_4{background-color: rgb(153, 247, 255);}\n"
"#tab_5{background-color: rgb(153, 247, 255);}\n"
"#tab_6{background-color: rgb(153, 247, 255);}\n"
"#tab_7{background-color: rgb(153, 247, 255);}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{background-color:rgb(10, 150, 250);color:white;}\n"
"#pushButton:hover{background-color:rgb(10, 10, 250);}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.tableView.setFont(font)
        self.tableView.setAutoFillBackground(True)
        self.tableView.setObjectName("tableView")
        self.gridLayout_5.addWidget(self.tableView, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(216, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(200, 37, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.tab_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 8, 2, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.tab_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_6.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_6.addWidget(self.radioButton)
        self.gridLayout.addWidget(self.frame_5, 3, 1, 1, 2)
        self.frame_6 = QtWidgets.QFrame(self.tab_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.gridLayout.addWidget(self.frame_6, 4, 1, 1, 2)
        self.frame_7 = QtWidgets.QFrame(self.tab_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_8.addWidget(self.lineEdit_7)
        self.gridLayout.addWidget(self.frame_7, 5, 1, 1, 2)
        self.frame_8 = QtWidgets.QFrame(self.tab_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_9.addWidget(self.lineEdit_8)
        self.gridLayout.addWidget(self.frame_8, 6, 1, 1, 2)
        self.frame_17 = QtWidgets.QFrame(self.tab_3)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(294, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_17)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3,#pushButton_6,#pushButton_7{background-color: rgb(85, 255, 0);border-radius: 5px;border:1px solid black;}#pushButton_3:hover{background-color: rgb(0, 170, 0);}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(295, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_17, 7, 1, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.tab_4)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{background-color:rgb(10, 150, 250);color:white;}\n"
"#pushButton_2:hover{background-color:rgb(10, 10, 250);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.tab_5)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_11.addWidget(self.lineEdit_10)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("#pushButton_8{background-color:rgb(10, 150, 250);color:white;}\n"
"#pushButton_8:hover{background-color:rgb(10, 10, 250);}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_11.addWidget(self.pushButton_8)
        self.verticalLayout_4.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.tab_5)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBox = QtWidgets.QGroupBox(self.frame_13)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget_2)
        self.horizontalLayout_12.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_13)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_13.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_13.addWidget(self.radioButton_3)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_14.addWidget(self.lineEdit_11)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_9 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_15.addWidget(self.label_9)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_16)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_15.addWidget(self.lineEdit_12)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.frame_18 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_11 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_16.addWidget(self.label_11)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_16.addWidget(self.lineEdit_13)
        self.verticalLayout_5.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem6)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_19)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("#pushButton_9{background-color:rgb(10, 150, 250);color:white;}\n"
"#pushButton_9:hover{background-color:rgb(10, 10, 250);}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_17.addWidget(self.pushButton_9)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem7)
        self.verticalLayout_5.addWidget(self.frame_19)
        self.horizontalLayout_12.addWidget(self.groupBox_2)
        self.verticalLayout_4.addWidget(self.frame_13)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.tab_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_10.addWidget(self.lineEdit_9)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("#pushButton_6{background-color:rgb(10, 150, 250);color:white;}\n"
"#pushButton_7:hover{background-color:rgb(10, 10, 250);}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_10.addWidget(self.pushButton_6)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.tableView_4 = QtWidgets.QTableView(self.tab_6)
        self.tableView_4.setObjectName("tableView_4")
        self.verticalLayout_3.addWidget(self.tableView_4)
        self.frame_11 = QtWidgets.QFrame(self.tab_6)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(461, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("#pushButton_7{background-color:rgb(10, 150, 250);color:white;}\n"
"#pushButton_7:hover{background-color:rgb(10, 10, 250);}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        spacerItem9 = QtWidgets.QSpacerItem(460, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.tab_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout.addWidget(self.lineEdit_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("#pushButton_4{background-color:rgb(10, 150, 250);color:white;}\n"
"#pushButton_4:hover{background-color:rgb(10, 10, 250);}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("#pushButton_5{background-color:rgb(10, 150, 250);color:white;}\n"
"#pushButton_5:hover{background-color:rgb(10, 10, 250);}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget_3)
        self.tabWidget.addTab(self.tab_7, "")
        self.verticalLayout_7.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(5)
        self.pushButton.clicked.connect(Form.search)
        self.pushButton_3.clicked.connect(Form.add)
        self.pushButton_2.clicked.connect(Form.delete_search)
        self.pushButton_8.clicked.connect(Form.modify_search)
        self.pushButton_9.clicked.connect(Form.modify)
        self.pushButton_6.clicked.connect(Form.choose_file)
        self.pushButton_7.clicked.connect(Form.lead_in)
        self.pushButton_4.clicked.connect(Form.output_search)
        self.pushButton_5.clicked.connect(Form.lead_out)
        self.radioButton_2.toggled['bool'].connect(Form.sex)
        self.radioButton.toggled['bool'].connect(Form.sex)
        self.radioButton_4.toggled['bool'].connect(Form.sex)
        self.radioButton_3.toggled['bool'].connect(Form.sex)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学生管理系统"))
        self.label.setText(_translate("Form", "欢迎进入学生管理系统"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "主页"))
        self.lineEdit.setPlaceholderText(_translate("Form", "输入学号\\姓名\\学院查找"))
        self.pushButton.setText(_translate("Form", "搜 索"))
        self.pushButton.setShortcut(_translate("Form", "Enter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "查找学生信息"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "输入学号"))
        self.label_2.setText(_translate("Form", "学号"))
        self.label_3.setText(_translate("Form", "姓名"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "输入姓名"))
        self.label_4.setText(_translate("Form", "性别"))
        self.radioButton_2.setText(_translate("Form", "男"))
        self.radioButton.setText(_translate("Form", "女"))
        self.label_5.setText(_translate("Form", "出生日期"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "出生日期1997--1-1"))
        self.label_6.setText(_translate("Form", "电话"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "电话号码"))
        self.label_7.setText(_translate("Form", "学院"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "输入学院"))
        self.pushButton_3.setText(_translate("Form", "添 加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "添加学生信息"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "输入学号\\姓名\\学院查找"))
        self.pushButton_2.setText(_translate("Form", "搜 索"))
        self.pushButton_2.setShortcut(_translate("Form", "Enter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "删除学生信息"))
        self.lineEdit_10.setPlaceholderText(_translate("Form", "输入学号"))
        self.pushButton_8.setText(_translate("Form", "搜 索"))
        self.pushButton_8.setShortcut(_translate("Form", "Enter"))
        self.groupBox.setTitle(_translate("Form", "结果"))
        self.groupBox_2.setTitle(_translate("Form", "修改"))
        self.label_8.setText(_translate("Form", "性别"))
        self.radioButton_4.setText(_translate("Form", "男"))
        self.radioButton_3.setText(_translate("Form", "女"))
        self.label_10.setText(_translate("Form", "出生日期"))
        self.lineEdit_11.setPlaceholderText(_translate("Form", "出生日期1997-1-1"))
        self.label_9.setText(_translate("Form", "电话"))
        self.lineEdit_12.setPlaceholderText(_translate("Form", "电话号码"))
        self.label_11.setText(_translate("Form", "学院"))
        self.lineEdit_13.setPlaceholderText(_translate("Form", "输入学院"))
        self.pushButton_9.setText(_translate("Form", "确认修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "修改学生信息"))
        self.pushButton_6.setText(_translate("Form", "选择文件"))
        self.pushButton_6.setShortcut(_translate("Form", "Enter"))
        self.pushButton_7.setText(_translate("Form", "导  入"))
        self.pushButton_7.setShortcut(_translate("Form", "Enter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Excel导入"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "输入学号\\姓名\\学院查找"))
        self.pushButton_4.setText(_translate("Form", "搜 索"))
        self.pushButton_4.setShortcut(_translate("Form", "Enter"))
        self.pushButton_5.setText(_translate("Form", "导 出"))
        self.pushButton_5.setShortcut(_translate("Form", "Enter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "Excel导出"))