# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTabWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta


class Ui_CleopatraClac(object):
    def setupUi(self, CleopatraClac):
        CleopatraClac.setObjectName("CleopatraClac")
        CleopatraClac.setEnabled(True)
        CleopatraClac.resize(697, 549)
        self.centralwidget = QtWidgets.QWidget(CleopatraClac)
        self.centralwidget.setObjectName("centralwidget")
        self.main_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 541))
        self.main_tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.main_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.main_tabWidget.setObjectName("main_tabWidget")
        self.Tab_Clasic = QtWidgets.QWidget()
        self.Tab_Clasic.setObjectName("Tab_Clasic")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Tab_Clasic)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 90, 691, 441))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.classic_but_zero = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_zero.setObjectName("classic_but_zero")
        self.gridLayout_2.addWidget(self.classic_but_zero, 6, 1, 1, 1)
        self.classic_but_mm = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_mm.setObjectName("classic_but_mm")
        self.gridLayout_2.addWidget(self.classic_but_mm, 1, 2, 1, 1)
        self.classic_but_degree = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_degree.setMinimumSize(QtCore.QSize(100, 0))
        self.classic_but_degree.setObjectName("classic_but_degree")
        self.gridLayout_2.addWidget(self.classic_but_degree, 0, 0, 1, 1)
        self.classic_but_mr = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_mr.setObjectName("classic_but_mr")
        self.gridLayout_2.addWidget(self.classic_but_mr, 1, 0, 1, 1)
        self.classic_but_remove = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_remove.setObjectName("classic_but_remove")
        self.gridLayout_2.addWidget(self.classic_but_remove, 2, 2, 1, 1)
        self.classic_but_mc = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_mc.setObjectName("classic_but_mc")
        self.gridLayout_2.addWidget(self.classic_but_mc, 2, 0, 1, 1)
        self.classic_but_nine = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_nine.setObjectName("classic_but_nine")
        self.gridLayout_2.addWidget(self.classic_but_nine, 3, 2, 1, 1)
        self.classic_but_point = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_point.setObjectName("classic_but_point")
        self.gridLayout_2.addWidget(self.classic_but_point, 6, 2, 1, 1)
        self.classic_but_erase = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_erase.setObjectName("classic_but_erase")
        self.gridLayout_2.addWidget(self.classic_but_erase, 2, 1, 1, 1)
        self.classic_but_plusorminus = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_plusorminus.setObjectName("classic_but_plusorminus")
        self.gridLayout_2.addWidget(self.classic_but_plusorminus, 6, 0, 1, 1)
        self.classic_but_root = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_root.setObjectName("classic_but_root")
        self.gridLayout_2.addWidget(self.classic_but_root, 0, 1, 1, 1)
        self.classic_but_persent = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_persent.setObjectName("classic_but_persent")
        self.gridLayout_2.addWidget(self.classic_but_persent, 0, 2, 1, 1)
        self.classic_but_two = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_two.setObjectName("classic_but_two")
        self.gridLayout_2.addWidget(self.classic_but_two, 5, 1, 1, 1)
        self.classic_but_six = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_six.setObjectName("classic_but_six")
        self.gridLayout_2.addWidget(self.classic_but_six, 4, 2, 1, 1)
        self.classic_but_one = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_one.setObjectName("classic_but_one")
        self.gridLayout_2.addWidget(self.classic_but_one, 5, 0, 1, 1)
        self.classic_but_five = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_five.setObjectName("classic_but_five")
        self.gridLayout_2.addWidget(self.classic_but_five, 4, 1, 1, 1)
        self.classic_but_eight = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_eight.setObjectName("classic_but_eight")
        self.gridLayout_2.addWidget(self.classic_but_eight, 3, 1, 1, 1)
        self.classic_but_seven = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_seven.setObjectName("classic_but_seven")
        self.gridLayout_2.addWidget(self.classic_but_seven, 3, 0, 1, 1)
        self.classic_but_mp = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_mp.setObjectName("classic_but_mp")
        self.gridLayout_2.addWidget(self.classic_but_mp, 1, 1, 1, 1)
        self.classic_but_three = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_three.setObjectName("classic_but_three")
        self.gridLayout_2.addWidget(self.classic_but_three, 5, 2, 1, 1)
        self.classic_but_four = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_four.setObjectName("classic_but_four")
        self.gridLayout_2.addWidget(self.classic_but_four, 4, 0, 1, 1)
        self.classic_but_equally = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_equally.setObjectName("classic_but_equally")
        self.gridLayout_2.addWidget(self.classic_but_equally, 6, 3, 1, 1)
        self.classic_but_plus = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_plus.setObjectName("classic_but_plus")
        self.gridLayout_2.addWidget(self.classic_but_plus, 5, 3, 1, 1)
        self.classic_but_minus = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_minus.setObjectName("classic_but_minus")
        self.gridLayout_2.addWidget(self.classic_but_minus, 4, 3, 1, 1)
        self.classic_but_multiply = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_multiply.setObjectName("classic_but_multiply")
        self.gridLayout_2.addWidget(self.classic_but_multiply, 3, 3, 1, 1)
        self.classic_but_division = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.classic_but_division.setObjectName("classic_but_division")
        self.gridLayout_2.addWidget(self.classic_but_division, 2, 3, 1, 1)
        self.classic_lcdNumber = QtWidgets.QLCDNumber(self.Tab_Clasic)
        self.classic_lcdNumber.setGeometry(QtCore.QRect(0, 10, 691, 81))
        self.classic_lcdNumber.setDigitCount(17)
        self.classic_lcdNumber.setObjectName("classic_lcdNumber")
        self.main_tabWidget.addTab(self.Tab_Clasic, "")
        self.Tab_Programmist = QtWidgets.QWidget()
        self.Tab_Programmist.setObjectName("Tab_Programmist")
        self.programmist_tabWidget = QtWidgets.QTabWidget(self.Tab_Programmist)
        self.programmist_tabWidget.setGeometry(QtCore.QRect(0, 0, 691, 511))
        self.programmist_tabWidget.setObjectName("programmist_tabWidget")
        self.SistemSchis_Program_Tab = QtWidgets.QWidget()
        self.SistemSchis_Program_Tab.setObjectName("SistemSchis_Program_Tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.SistemSchis_Program_Tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 671, 315))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.SistemSchis_Label_In = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SistemSchis_Label_In.setObjectName("SistemSchis_Label_In")
        self.gridLayout.addWidget(self.SistemSchis_Label_In, 0, 1, 1, 1)
        self.SistemSchis_Label_From = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SistemSchis_Label_From.setObjectName("SistemSchis_Label_From")
        self.gridLayout.addWidget(self.SistemSchis_Label_From, 0, 0, 1, 1)
        self.SistemSchis_spinBox_From = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.SistemSchis_spinBox_From.setObjectName("SistemSchis_spinBox_From")
        self.gridLayout.addWidget(self.SistemSchis_spinBox_From, 1, 0, 1, 1)
        self.SistemSchis_spinBox_In = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.SistemSchis_spinBox_In.setObjectName("SistemSchis_spinBox_In")
        self.gridLayout.addWidget(self.SistemSchis_spinBox_In, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.SistemSchis_Label_Number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SistemSchis_Label_Number.setObjectName("SistemSchis_Label_Number")
        self.verticalLayout.addWidget(self.SistemSchis_Label_Number)
        self.SistemSchis_textEdit_In = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.SistemSchis_textEdit_In.setObjectName("SistemSchis_textEdit_In")
        self.verticalLayout.addWidget(self.SistemSchis_textEdit_In)
        self.SistemSchis_but_calculate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SistemSchis_but_calculate.setObjectName("SistemSchis_but_calculate")
        self.verticalLayout.addWidget(self.SistemSchis_but_calculate)
        self.SistemSchis_Label_rezult = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SistemSchis_Label_rezult.setObjectName("SistemSchis_Label_rezult")
        self.verticalLayout.addWidget(self.SistemSchis_Label_rezult)
        self.SistemSchis_textEdit_rezult = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.SistemSchis_textEdit_rezult.setObjectName("SistemSchis_textEdit_rezult")
        self.verticalLayout.addWidget(self.SistemSchis_textEdit_rezult)
        self.programmist_tabWidget.addTab(self.SistemSchis_Program_Tab, "")
        self.SistemIzmer_Program_Tab = QtWidgets.QWidget()
        self.SistemIzmer_Program_Tab.setObjectName("SistemIzmer_Program_Tab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.SistemIzmer_Program_Tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(30, 30, 621, 431))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SistemIzmer_label_from = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.SistemIzmer_label_from.setObjectName("SistemIzmer_label_from")
        self.verticalLayout_2.addWidget(self.SistemIzmer_label_from)
        self.SistemIzmer_radioButton_byte_from = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_byte_from.setObjectName("SistemIzmer_radioButton_byte_from")
        self.buttonGroup = QtWidgets.QButtonGroup(CleopatraClac)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.SistemIzmer_radioButton_byte_from)
        self.verticalLayout_2.addWidget(self.SistemIzmer_radioButton_byte_from)
        self.SistemIzmer_radioButton_kylobyte_from = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_kylobyte_from.setObjectName("SistemIzmer_radioButton_kylobyte_from")
        self.buttonGroup.addButton(self.SistemIzmer_radioButton_kylobyte_from)
        self.verticalLayout_2.addWidget(self.SistemIzmer_radioButton_kylobyte_from)
        self.SistemIzmer_radioButton_megabyte_from = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_megabyte_from.setObjectName("SistemIzmer_radioButton_megabyte_from")
        self.buttonGroup.addButton(self.SistemIzmer_radioButton_megabyte_from)
        self.verticalLayout_2.addWidget(self.SistemIzmer_radioButton_megabyte_from)
        self.SistemIzmer_gigaradioButton_byte_from = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_gigaradioButton_byte_from.setObjectName("SistemIzmer_gigaradioButton_byte_from")
        self.buttonGroup.addButton(self.SistemIzmer_gigaradioButton_byte_from)
        self.verticalLayout_2.addWidget(self.SistemIzmer_gigaradioButton_byte_from)
        self.SistemIzmer_radioButton_terabyte_from = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_terabyte_from.setObjectName("SistemIzmer_radioButton_terabyte_from")
        self.buttonGroup.addButton(self.SistemIzmer_radioButton_terabyte_from)
        self.verticalLayout_2.addWidget(self.SistemIzmer_radioButton_terabyte_from)
        self.SistemIzmer_radioButton_petabyte_from = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_petabyte_from.setObjectName("SistemIzmer_radioButton_petabyte_from")
        self.buttonGroup.addButton(self.SistemIzmer_radioButton_petabyte_from)
        self.verticalLayout_2.addWidget(self.SistemIzmer_radioButton_petabyte_from)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SistemIzmer_label_in = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.SistemIzmer_label_in.setObjectName("SistemIzmer_label_in")
        self.verticalLayout_3.addWidget(self.SistemIzmer_label_in)
        self.SistemIzmer_radioButton_byte_in = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_byte_in.setObjectName("SistemIzmer_radioButton_byte_in")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(CleopatraClac)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.SistemIzmer_radioButton_byte_in)
        self.verticalLayout_3.addWidget(self.SistemIzmer_radioButton_byte_in)
        self.SistemIzmer_radioButton_kylobyte_in = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_kylobyte_in.setObjectName("SistemIzmer_radioButton_kylobyte_in")
        self.buttonGroup_2.addButton(self.SistemIzmer_radioButton_kylobyte_in)
        self.verticalLayout_3.addWidget(self.SistemIzmer_radioButton_kylobyte_in)
        self.SistemIzmer_radioButton_megabyte_in = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_megabyte_in.setObjectName("SistemIzmer_radioButton_megabyte_in")
        self.buttonGroup_2.addButton(self.SistemIzmer_radioButton_megabyte_in)
        self.verticalLayout_3.addWidget(self.SistemIzmer_radioButton_megabyte_in)
        self.SistemIzmer_radioButton_gigabyte_in = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_gigabyte_in.setObjectName("SistemIzmer_radioButton_gigabyte_in")
        self.buttonGroup_2.addButton(self.SistemIzmer_radioButton_gigabyte_in)
        self.verticalLayout_3.addWidget(self.SistemIzmer_radioButton_gigabyte_in)
        self.SistemIzmer_radioButton_terabyte_in = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_terabyte_in.setObjectName("SistemIzmer_radioButton_terabyte_in")
        self.buttonGroup_2.addButton(self.SistemIzmer_radioButton_terabyte_in)
        self.verticalLayout_3.addWidget(self.SistemIzmer_radioButton_terabyte_in)
        self.SistemIzmer_radioButton_petabyte_in = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_radioButton_petabyte_in.setObjectName("SistemIzmer_radioButton_petabyte_in")
        self.buttonGroup_2.addButton(self.SistemIzmer_radioButton_petabyte_in)
        self.verticalLayout_3.addWidget(self.SistemIzmer_radioButton_petabyte_in)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.SistemIzmer_label_number = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.SistemIzmer_label_number.setObjectName("SistemIzmer_label_number")
        self.verticalLayout_4.addWidget(self.SistemIzmer_label_number)
        self.SistemIzmer_textEdit_number = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.SistemIzmer_textEdit_number.setObjectName("SistemIzmer_textEdit_number")
        self.verticalLayout_4.addWidget(self.SistemIzmer_textEdit_number)
        self.SistemIzmer_but_calculate = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.SistemIzmer_but_calculate.setObjectName("SistemIzmer_but_calculate")
        self.verticalLayout_4.addWidget(self.SistemIzmer_but_calculate)
        self.SistemIzmer_label_result = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.SistemIzmer_label_result.setObjectName("SistemIzmer_label_result")
        self.verticalLayout_4.addWidget(self.SistemIzmer_label_result)
        self.SistemIzmer_textEdit_rezult = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.SistemIzmer_textEdit_rezult.setReadOnly(False)
        self.SistemIzmer_textEdit_rezult.setObjectName("SistemIzmer_textEdit_rezult")
        self.verticalLayout_4.addWidget(self.SistemIzmer_textEdit_rezult)
        self.programmist_tabWidget.addTab(self.SistemIzmer_Program_Tab, "")
        self.SistemSchisOperation_Program_Tab = QtWidgets.QWidget()
        self.SistemSchisOperation_Program_Tab.setObjectName("SistemSchisOperation_Program_Tab")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.SistemSchisOperation_Program_Tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 70, 671, 315))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.SistemSchisOperation_label_sistemtwonumber = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_label_sistemtwonumber.setObjectName("SistemSchisOperation_label_sistemtwonumber")
        self.gridLayout_3.addWidget(self.SistemSchisOperation_label_sistemtwonumber, 0, 1, 1, 1)
        self.SistemSchisOperation_spinBox_sistemonenumber = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_spinBox_sistemonenumber.setObjectName("SistemSchisOperation_spinBox_sistemonenumber")
        self.gridLayout_3.addWidget(self.SistemSchisOperation_spinBox_sistemonenumber, 1, 0, 1, 1)
        self.SistemSchisOperation_label_twonumber = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_label_twonumber.setObjectName("SistemSchisOperation_label_twonumber")
        self.gridLayout_3.addWidget(self.SistemSchisOperation_label_twonumber, 2, 1, 1, 1)
        self.SistemSchisOperation_label_onenumber = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_label_onenumber.setObjectName("SistemSchisOperation_label_onenumber")
        self.gridLayout_3.addWidget(self.SistemSchisOperation_label_onenumber, 2, 0, 1, 1)
        self.SistemSchisOperation_label_sistemonenumber = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_label_sistemonenumber.setObjectName("SistemSchisOperation_label_sistemonenumber")
        self.gridLayout_3.addWidget(self.SistemSchisOperation_label_sistemonenumber, 0, 0, 1, 1)
        self.SistemSchisOperation_spinBox_sistemtwonumber = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_spinBox_sistemtwonumber.setObjectName("SistemSchisOperation_spinBox_sistemtwonumber")
        self.gridLayout_3.addWidget(self.SistemSchisOperation_spinBox_sistemtwonumber, 1, 1, 1, 1)
        self.SistemSchisOperation_textEdit_onenumber = QtWidgets.QTextEdit(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_textEdit_onenumber.setObjectName("SistemSchisOperation_textEdit_onenumber")
        self.gridLayout_3.addWidget(self.SistemSchisOperation_textEdit_onenumber, 3, 0, 1, 1)
        self.SistemSchisOperation_textEdit_twonumber = QtWidgets.QTextEdit(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_textEdit_twonumber.setObjectName("SistemSchisOperation_textEdit_twonumber")
        self.gridLayout_3.addWidget(self.SistemSchisOperation_textEdit_twonumber, 3, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SistemSchisOperation_but_plus = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_but_plus.setObjectName("SistemSchisOperation_but_plus")
        self.horizontalLayout_2.addWidget(self.SistemSchisOperation_but_plus)
        self.SistemSchisOperation_but_minus = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_but_minus.setObjectName("SistemSchisOperation_but_minus")
        self.horizontalLayout_2.addWidget(self.SistemSchisOperation_but_minus)
        self.SistemSchisOperation_but_multiply = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_but_multiply.setObjectName("SistemSchisOperation_but_multiply")
        self.horizontalLayout_2.addWidget(self.SistemSchisOperation_but_multiply)
        self.SistemSchisOperation_but_divide = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_but_divide.setObjectName("SistemSchisOperation_but_divide")
        self.horizontalLayout_2.addWidget(self.SistemSchisOperation_but_divide)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.SistemSchisOperation_but_calculate = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_but_calculate.setObjectName("SistemSchisOperation_but_calculate")
        self.verticalLayout_5.addWidget(self.SistemSchisOperation_but_calculate)
        self.SistemSchisOperation_label_result = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_label_result.setObjectName("SistemSchisOperation_label_result")
        self.verticalLayout_5.addWidget(self.SistemSchisOperation_label_result)
        self.SistemSchisOperation_textEdit_result = QtWidgets.QTextEdit(self.verticalLayoutWidget_5)
        self.SistemSchisOperation_textEdit_result.setObjectName("SistemSchisOperation_textEdit_result")
        self.verticalLayout_5.addWidget(self.SistemSchisOperation_textEdit_result)
        self.programmist_tabWidget.addTab(self.SistemSchisOperation_Program_Tab, "")
        self.main_tabWidget.addTab(self.Tab_Programmist, "")
        self.Tab_Date = QtWidgets.QWidget()
        self.Tab_Date.setObjectName("Tab_Date")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.Tab_Date)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(20, 90, 651, 211))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.datecalculation_label_from = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.datecalculation_label_from.setFont(font)
        self.datecalculation_label_from.setObjectName("datecalculation_label_from")
        self.verticalLayout_6.addWidget(self.datecalculation_label_from)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.datecalculation_dateEdit_from = QtWidgets.QDateEdit(self.verticalLayoutWidget_8)
        self.datecalculation_dateEdit_from.setObjectName("datecalculation_dateEdit_from")
        self.horizontalLayout_3.addWidget(self.datecalculation_dateEdit_from)
        self.datecalculation_timeEdit_from = QtWidgets.QTimeEdit(self.verticalLayoutWidget_8)
        self.datecalculation_timeEdit_from.setObjectName("datecalculation_timeEdit_from")
        self.horizontalLayout_3.addWidget(self.datecalculation_timeEdit_from)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.datecalculation_label_in = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.datecalculation_label_in.setFont(font)
        self.datecalculation_label_in.setObjectName("datecalculation_label_in")
        self.verticalLayout_7.addWidget(self.datecalculation_label_in)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.datecalculation_dateEdit_in = QtWidgets.QDateEdit(self.verticalLayoutWidget_8)
        self.datecalculation_dateEdit_in.setObjectName("datecalculation_dateEdit_in")
        self.horizontalLayout_4.addWidget(self.datecalculation_dateEdit_in)
        self.datecalculation_timeEdit_in = QtWidgets.QTimeEdit(self.verticalLayoutWidget_8)
        self.datecalculation_timeEdit_in.setObjectName("datecalculation_timeEdit_in")
        self.horizontalLayout_4.addWidget(self.datecalculation_timeEdit_in)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.datecalculation_but_calculat = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.datecalculation_but_calculat.setObjectName("datecalculation_but_calculat")
        self.verticalLayout_8.addWidget(self.datecalculation_but_calculat)
        self.datecalculation_label_result = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.datecalculation_label_result.setFont(font)
        self.datecalculation_label_result.setObjectName("datecalculation_label_result")
        self.verticalLayout_8.addWidget(self.datecalculation_label_result)
        self.datecalculation_textEdit_result = QtWidgets.QTextEdit(self.verticalLayoutWidget_8)
        self.datecalculation_textEdit_result.setObjectName("datecalculation_textEdit_result")
        self.verticalLayout_8.addWidget(self.datecalculation_textEdit_result)
        self.main_tabWidget.addTab(self.Tab_Date, "")
        CleopatraClac.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CleopatraClac)
        self.statusbar.setObjectName("statusbar")
        CleopatraClac.setStatusBar(self.statusbar)

        self.retranslateUi(CleopatraClac)
        self.main_tabWidget.setCurrentIndex(0)
        self.programmist_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CleopatraClac)

    def retranslateUi(self, CleopatraClac):
        _translate = QtCore.QCoreApplication.translate
        CleopatraClac.setWindowTitle(_translate("CleopatraClac", "Клеопатра Calc"))
        self.classic_but_zero.setText(_translate("CleopatraClac", "0"))
        self.classic_but_mm.setText(_translate("CleopatraClac", "M-"))
        self.classic_but_degree.setText(_translate("CleopatraClac", "X²"))
        self.classic_but_mr.setText(_translate("CleopatraClac", "MR"))
        self.classic_but_remove.setText(_translate("CleopatraClac", "←"))
        self.classic_but_mc.setText(_translate("CleopatraClac", "MC"))
        self.classic_but_nine.setText(_translate("CleopatraClac", "9"))
        self.classic_but_point.setText(_translate("CleopatraClac", ","))
        self.classic_but_erase.setText(_translate("CleopatraClac", "C"))
        self.classic_but_plusorminus.setText(_translate("CleopatraClac", "+/-"))
        self.classic_but_root.setText(_translate("CleopatraClac", "√x"))
        self.classic_but_persent.setText(_translate("CleopatraClac", "%"))
        self.classic_but_two.setText(_translate("CleopatraClac", "2"))
        self.classic_but_six.setText(_translate("CleopatraClac", "6"))
        self.classic_but_one.setText(_translate("CleopatraClac", "1"))
        self.classic_but_five.setText(_translate("CleopatraClac", "5"))
        self.classic_but_eight.setText(_translate("CleopatraClac", "8"))
        self.classic_but_seven.setText(_translate("CleopatraClac", "7"))
        self.classic_but_mp.setText(_translate("CleopatraClac", "M+"))
        self.classic_but_three.setText(_translate("CleopatraClac", "3"))
        self.classic_but_four.setText(_translate("CleopatraClac", "4"))
        self.classic_but_equally.setText(_translate("CleopatraClac", "="))
        self.classic_but_plus.setText(_translate("CleopatraClac", "+"))
        self.classic_but_minus.setText(_translate("CleopatraClac", "-"))
        self.classic_but_multiply.setText(_translate("CleopatraClac", "*"))
        self.classic_but_division.setText(_translate("CleopatraClac", "/"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.Tab_Clasic),
                                       _translate("CleopatraClac", "Обычный"))
        self.SistemSchis_Label_In.setText(_translate("CleopatraClac", "В какую систему счисления"))
        self.SistemSchis_Label_From.setText(_translate("CleopatraClac", "Из какой системы счисления"))
        self.SistemSchis_Label_Number.setText(_translate("CleopatraClac", "Ваше число"))
        self.SistemSchis_but_calculate.setText(_translate("CleopatraClac", "Рассчитать"))
        self.SistemSchis_Label_rezult.setText(_translate("CleopatraClac", "Результат"))
        self.programmist_tabWidget.setTabText(self.programmist_tabWidget.indexOf(self.SistemSchis_Program_Tab),
                                              _translate("CleopatraClac", "Перевод между системами счисления"))
        self.SistemIzmer_label_from.setText(_translate("CleopatraClac", "С какой единицы измерения"))
        self.SistemIzmer_radioButton_byte_from.setText(_translate("CleopatraClac", "Байт"))
        self.SistemIzmer_radioButton_kylobyte_from.setText(_translate("CleopatraClac", "Килобайт (Кб)"))
        self.SistemIzmer_radioButton_megabyte_from.setText(_translate("CleopatraClac", "Мегабайт (Мб)"))
        self.SistemIzmer_gigaradioButton_byte_from.setText(_translate("CleopatraClac", "Гигабайт (Гб)"))
        self.SistemIzmer_radioButton_terabyte_from.setText(_translate("CleopatraClac", "Терабайт (Тб)"))
        self.SistemIzmer_radioButton_petabyte_from.setText(_translate("CleopatraClac", "Петабайт (Пб)"))
        self.SistemIzmer_label_in.setText(_translate("CleopatraClac", "В какую единицу измерения"))
        self.SistemIzmer_radioButton_byte_in.setText(_translate("CleopatraClac", "Байт"))
        self.SistemIzmer_radioButton_kylobyte_in.setText(_translate("CleopatraClac", "Килобайт (Кб)"))
        self.SistemIzmer_radioButton_megabyte_in.setText(_translate("CleopatraClac", "Мегабайт (Мб)"))
        self.SistemIzmer_radioButton_gigabyte_in.setText(_translate("CleopatraClac", "Гигабайт (Гб)"))
        self.SistemIzmer_radioButton_terabyte_in.setText(_translate("CleopatraClac", "Терабайт (Тб)"))
        self.SistemIzmer_radioButton_petabyte_in.setText(_translate("CleopatraClac", "Петабайт (Пб)"))
        self.SistemIzmer_label_number.setText(_translate("CleopatraClac", "Ваше число"))
        self.SistemIzmer_but_calculate.setText(_translate("CleopatraClac", "Рассчитать"))
        self.SistemIzmer_label_result.setText(_translate("CleopatraClac", "Результат"))
        self.SistemIzmer_textEdit_rezult.setHtml(_translate("CleopatraClac",
                                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.programmist_tabWidget.setTabText(self.programmist_tabWidget.indexOf(self.SistemIzmer_Program_Tab),
                                              _translate("CleopatraClac", "Перевод между единицами измерения"))
        self.SistemSchisOperation_label_sistemtwonumber.setText(
            _translate("CleopatraClac", "Система счисления 2 числа"))
        self.SistemSchisOperation_label_twonumber.setText(_translate("CleopatraClac", "Число 2"))
        self.SistemSchisOperation_label_onenumber.setText(_translate("CleopatraClac", "Число 1"))
        self.SistemSchisOperation_label_sistemonenumber.setText(
            _translate("CleopatraClac", "Система счисления 1 числа"))
        self.SistemSchisOperation_but_plus.setText(_translate("CleopatraClac", "+"))
        self.SistemSchisOperation_but_minus.setText(_translate("CleopatraClac", "-"))
        self.SistemSchisOperation_but_multiply.setText(_translate("CleopatraClac", "*"))
        self.SistemSchisOperation_but_divide.setText(_translate("CleopatraClac", "/"))
        self.SistemSchisOperation_but_calculate.setText(_translate("CleopatraClac", "Рассчитать"))
        self.SistemSchisOperation_label_result.setText(_translate("CleopatraClac", "Результат"))
        self.programmist_tabWidget.setTabText(self.programmist_tabWidget.indexOf(self.SistemSchisOperation_Program_Tab),
                                              _translate("CleopatraClac", "Операции в других системах счисления"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.Tab_Programmist),
                                       _translate("CleopatraClac", "Программист"))
        self.datecalculation_label_from.setText(_translate("CleopatraClac", "С"))
        self.datecalculation_label_in.setText(_translate("CleopatraClac", "До"))
        self.datecalculation_but_calculat.setText(_translate("CleopatraClac", "Рассчитать"))
        self.datecalculation_label_result.setText(_translate("CleopatraClac", "Разница"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.Tab_Date),
                                       _translate("CleopatraClac", "Вычисление даты"))


class Main(QMainWindow, Ui_CleopatraClac):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Datetime
        self.datecalculation_but_calculat.clicked.connect(self.datecalculation_rezult)

        # Program Perevod Meshdu Sistem of Chisleniy
        self.SistemSchis_but_calculate.clicked.connect(self.SistemSchis_Rezult)

        # Programa Perevod mezdu edinicami izmerenia
        self.SistemIzmer_but_calculate.clicked.connect(self.SistemIzmer_rezult)
        self.buttonGroup.buttonClicked.connect(self.SistemIzmer_def_1)
        self.buttonGroup_2.buttonClicked.connect(self.SistemIzmer_def_2)
        self.SistemIzmer_num1 = 0
        self.SistemIzmer_num2 = 0

        # SistemSchisOperation_Program
        self.SistemSchisOperation_but_plus.clicked.connect(self.SistemSchisOperation_Program_plus)
        self.SistemSchisOperation_but_minus.clicked.connect(self.SistemSchisOperation_Program_minus)
        self.SistemSchisOperation_but_multiply.clicked.connect(self.SistemSchisOperation_Program_multiply)
        self.SistemSchisOperation_but_divide.clicked.connect(self.SistemSchisOperation_Program_divide)
        self.SistemSchisOperation_but_calculate.clicked.connect(self.SistemSchisOperation_Program_rezult)

        # Clasic
        self.classic_a = ''
        self.classic_b = ''
        self.classic_simvol = ''
        self.classic_mp = ''
        self.classic_mm = ''
        self.classic_mr = ''
        self.classic_znach = ''
        self.classic_but_plusorminus.clicked.connect(self.addclassic_but_plusorminus)
        self.classic_but_zero.clicked.connect(self.addclassic_but_zero)
        self.classic_but_point.clicked.connect(self.addclassic_but_point)
        self.classic_but_one.clicked.connect(self.addclassic_but_one)
        self.classic_but_two.clicked.connect(self.addclassic_but_two)
        self.classic_but_three.clicked.connect(self.addclassic_but_three)
        self.classic_but_four.clicked.connect(self.addclassic_but_four)
        self.classic_but_five.clicked.connect(self.addclassic_but_five)
        self.classic_but_six.clicked.connect(self.addclassic_but_six)
        self.classic_but_seven.clicked.connect(self.addclassic_but_seven)
        self.classic_but_eight.clicked.connect(self.addclassic_but_eight)
        self.classic_but_nine.clicked.connect(self.addclassic_but_nine)
        self.classic_but_mc.clicked.connect(self.addclassic_but_mc)
        self.classic_but_erase.clicked.connect(self.addclassic_but_erase)
        self.classic_but_remove.clicked.connect(self.addclassic_but_remove)
        self.classic_but_mr.clicked.connect(self.addclassic_but_mr)
        self.classic_but_remove.clicked.connect(self.addclassic_but_remove)
        self.classic_but_mp.clicked.connect(self.addclassic_but_mp)
        self.classic_but_mm.clicked.connect(self.addclassic_but_mm)
        self.classic_but_degree.clicked.connect(self.addclassic_but_degree)
        self.classic_but_root.clicked.connect(self.addclassic_but_root)
        self.classic_but_persent.clicked.connect(self.addclassic_but_persent)
        self.classic_but_plus.clicked.connect(self.addclassic_but_plus)
        self.classic_but_minus.clicked.connect(self.addclassic_but_minus)
        self.classic_but_multiply.clicked.connect(self.addclassic_but_multiply)
        self.classic_but_division.clicked.connect(self.addclassic_but_division)
        self.classic_but_equally.clicked.connect(self.addclassic_but_equally)

    def addclassic_but_plusorminus(self):
        if self.classic_simvol == '':
            a = float(self.classic_a) * -1
            self.classic_a = str(a)
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            b = float(self.classic_b) * -1
            self.classic_b = str(b)
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_zero(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '0'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '0'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_point(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '.'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '.'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_one(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '1'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '1'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_two(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '2'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '2'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_three(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '3'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '3'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_four(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '4'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '4'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_five(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '5'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '5'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_six(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '6'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '6'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_seven(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '7'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '7'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_eight(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '8'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '8'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_nine(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_a + '9'
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_b + '9'
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_mc(self):
        self.classic_mr = ''

    def addclassic_but_erase(self):
        self.classic_a = ''
        self.classic_lcdNumber.display(0)
        self.classic_b = ''
        self.classic_simvol = ''

    def addclassic_but_remove(self):
        if self.classic_simvol == '':
            a = self.classic_a[:-1]
            self.classic_a = a
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            b = self.classic_b[:-1]
            self.classic_b = b
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_mr(self):
        if self.classic_simvol == '':
            self.classic_a = self.classic_mr
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = self.classic_mr
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_mp(self):
        if self.classic_simvol == '':
            self.classic_mr = self.classic_a
        elif self.classic_simvol != '' and self.classic_simvol == '':
            self.classic_mr = self.classic_b
        elif self.classic_simvol != '' and self.classic_simvol != '':
            self.classic_mr = self.classic_znach

    def addclassic_but_mm(self):
        if self.classic_simvol == '':
            self.classic_mr = self.classic_a
        elif self.classic_simvol != '' and self.classic_simvol == '':
            self.classic_mr = self.classic_b
        elif self.classic_simvol != '' and self.classic_simvol != '':
            self.classic_mr = self.classic_znach

    def addclassic_but_degree(self):
        if self.classic_simvol == '':
            self.classic_a = str(float(self.classic_a) ** 2)
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = str(float(self.classic_b) ** 2)
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_root(self):
        if self.classic_simvol == '':
            self.classic_a = str(float(self.classic_a) ** 0.5)
            self.classic_lcdNumber.display(float(self.classic_a))
        elif self.classic_simvol != '':
            self.classic_b = str(float(self.classic_b) ** 0.5)
            self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_persent(self):
        b = float(self.classic_b) * float(self.classic_a) / 100
        print(b)
        self.classic_b = str(b)
        print(b)
        self.classic_lcdNumber.display(float(self.classic_b))

    def addclassic_but_plus(self):
        self.classic_simvol = '+'

    def addclassic_but_minus(self):
        self.classic_simvol = '-'

    def addclassic_but_multiply(self):
        self.classic_simvol = '*'

    def addclassic_but_division(self):
        self.classic_simvol = '/'

    def addclassic_but_equally(self):
        if self.classic_simvol == '+':
            self.classic_znach = str(float(self.classic_a) + float(self.classic_b))
            self.classic_lcdNumber.display(float(self.classic_znach))
        elif self.classic_simvol == '-':
            self.classic_znach = str(float(self.classic_a) - float(self.classic_b))
            self.classic_lcdNumber.display(float(self.classic_znach))
        elif self.classic_simvol == '*':
            self.classic_znach = str(float(self.classic_a) * float(self.classic_b))
            self.classic_lcdNumber.display(float(self.classic_znach))
        elif self.classic_simvol == '/':
            self.classic_znach = str(float(self.classic_a) / float(self.classic_b))
            self.classic_lcdNumber.display(float(self.classic_znach))
        self.classic_a = self.classic_znach
        self.classic_lcdNumber.display(float(self.classic_a))
        self.classic_znach = ''
        self.classic_b = ''
        self.classic_simvol = ''

    # Classic END

    # Program Perevod Meshdu Sistem of Chisleniy

    def SistemSchis_Rezult(self):
        num = self.SistemSchis_textEdit_In.toPlainText()
        print(num)
        to_base = self.SistemSchis_spinBox_From.value()
        print(to_base)
        from_base = self.SistemSchis_spinBox_In.value()
        print(from_base)
        self.SistemSchis_textEdit_rezult.setText(self.convert_base(num, to_base=from_base, from_base=to_base))

    def convert_base(self, num, to_base=10, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return self.convert_base(n // to_base, to_base) + alphabet[n % to_base]

    # Programa Perevod mezdu edinicami izmerenia
    def SistemIzmer_def_1(self, button):
        a = button.text()
        if a == 'Байт':
            self.SistemIzmer_num1 = 0
        elif a == 'Килобайт (Кб)':
            self.SistemIzmer_num1 = 1
        elif a == 'Мегабайт (Мб)':
            self.SistemIzmer_num1 = 2
        elif a == 'Гигабайт (Гб)':
            self.SistemIzmer_num1 = 3
        elif a == 'Терабайт (Тб)':
            self.SistemIzmer_num1 = 4
        elif a == 'Петабайт (Пб)':
            self.SistemIzmer_num1 = 5

    def SistemIzmer_def_2(self, button):
        a = button.text()
        if a == 'Байт':
            self.SistemIzmer_num2 = 0
        elif a == 'Килобайт (Кб)':
            self.SistemIzmer_num2 = 1
        elif a == 'Мегабайт (Мб)':
            self.SistemIzmer_num2 = 2
        elif a == 'Гигабайт (Гб)':
            self.SistemIzmer_num2 = 3
        elif a == 'Терабайт (Тб)':
            self.SistemIzmer_num2 = 4
        elif a == 'Петабайт (Пб)':
            self.SistemIzmer_num2 = 5

    def SistemIzmer_rezult(self):
        num = float(self.SistemIzmer_textEdit_number.toPlainText())

        if self.SistemIzmer_num1 == 0:
            pass
        elif self.SistemIzmer_num1 == 1:
            num = num * 1024
        elif self.SistemIzmer_num1 == 2:
            num = num * 1024 * 1024
        elif self.SistemIzmer_num1 == 3:
            num = num * 1024 * 1024 * 1024
        elif self.SistemIzmer_num1 == 4:
            num = num * 1024 * 1024 * 1024 * 1024
        elif self.SistemIzmer_num1 == 5:
            num = num * 1024 * 1024 * 1024 * 1024 * 1024

        if self.SistemIzmer_num2 == 0:
            pass
        elif self.SistemIzmer_num2 == 1:
            num = num / 1024
        elif self.SistemIzmer_num2 == 2:
            num = num / 1024 / 1024
        elif self.SistemIzmer_num2 == 3:
            num = num / 1024 / 1024 / 1024
        elif self.SistemIzmer_num2 == 4:
            num = num / 1024 / 1024 / 1024 / 1024
        elif self.SistemIzmer_num2 == 5:
            num = num / 1024 / 1024 / 1024 / 1024 / 1024
        self.SistemIzmer_textEdit_rezult.setText(str(num))

    def SistemSchisOperation_Program_plus(self):
        num = self.SistemSchisOperation_textEdit_onenumber.toPlainText()
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        a = self.convert_base(num, to_base=10, from_base=from_base)
        a = int(a)
        num = self.SistemSchisOperation_textEdit_twonumber.toPlainText()
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        b = self.convert_base(num, to_base=10, from_base=from_base)
        b = int(b)
        self.SistemSchisOperation_number = a + b

    def SistemSchisOperation_Program_minus(self):
        num = self.SistemSchisOperation_textEdit_onenumber.toPlainText()
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        a = self.convert_base(num, to_base=10, from_base=from_base)
        a = int(a)
        num = self.SistemSchisOperation_textEdit_twonumber.toPlainText()
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        b = self.convert_base(num, to_base=10, from_base=from_base)
        b = int(b)
        self.SistemSchisOperation_number = a - b

    def SistemSchisOperation_Program_multiply(self):
        num = self.SistemSchisOperation_textEdit_onenumber.toPlainText()
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        a = self.convert_base(num, to_base=10, from_base=from_base)
        a = int(a)
        num = self.SistemSchisOperation_textEdit_twonumber.toPlainText()
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        b = self.convert_base(num, to_base=10, from_base=from_base)
        b = int(b)
        self.SistemSchisOperation_number = a * b

    def SistemSchisOperation_Program_divide(self):
        num = self.SistemSchisOperation_textEdit_onenumber.toPlainText()
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        a = self.convert_base(num, to_base=10, from_base=from_base)
        a = int(a)
        num = self.SistemSchisOperation_textEdit_twonumber.toPlainText()
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        b = self.convert_base(num, to_base=10, from_base=from_base)
        b = int(b)
        self.SistemSchisOperation_number = a // b

    def SistemSchisOperation_Program_rezult(self):
        from_base = self.SistemSchisOperation_spinBox_sistemonenumber.value()
        num = str(self.SistemSchisOperation_number)
        nu = self.convert_base(num, to_base=from_base, from_base=10)
        print(nu)
        self.SistemSchisOperation_textEdit_result.setText(nu)

    # Date Calculate
    def datecalculation_rezult(self):
        year1 = self.datecalculation_dateEdit_from.date().year()
        year2 = self.datecalculation_dateEdit_in.date().year()
        month1 = self.datecalculation_dateEdit_from.date().month()
        month2 = self.datecalculation_dateEdit_in.date().month()
        day1 = self.datecalculation_dateEdit_from.date().day()
        day2 = self.datecalculation_dateEdit_in.date().day()

        hour1 = self.datecalculation_timeEdit_from.time().hour()
        hour2 = self.datecalculation_timeEdit_in.time().hour()
        minute1 = self.datecalculation_timeEdit_from.time().minute()
        minute2 = self.datecalculation_timeEdit_in.time().minute()
        t1 = datetime(year1, month1, day1, hour1, minute1)

        t2 = datetime(year2, month2, day2, hour2, minute2)

        rez = t2 - t1
        self.datecalculation_textEdit_result.setText(str(rez))


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())
