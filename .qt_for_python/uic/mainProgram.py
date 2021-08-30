# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainProgram.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import photos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 630)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 791, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(255, 255,255)\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 80, 761, 521))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 424, 230, 80))
        self.groupBox_2.setStyleSheet(u"border: 1px solid rgb(250,250,250);\n"
"border-radius: 3px")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-1, 0, 121, 20))
        self.label_4.setStyleSheet(u"color: rgb(0,0,0);\n"
"background-color: rgb(250,250,250);\n"
"border-radius: 3px")
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 30, 100, 41))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"\n"
"QPushButton:focus {\n"
"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"")
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 30, 100, 41))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"\n"
"QPushButton:focus {\n"
"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 30, 231, 89))
        self.groupBox_3.setStyleSheet(u"border: 1px solid rgb(250,250,250);\n"
"border-radius: 3px")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 30, 120, 20))
        self.label_5.setStyleSheet(u"color: rgb(0,0,0);\n"
"background-color: rgb(250,250,250);\n"
"border-radius: 3px")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 454, 35, 25))
        self.label_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 454, 35, 25))
        self.label_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 60, 170, 39))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius:7px;\n"
"}")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 130, 231, 140))
        self.groupBox_4.setStyleSheet(u"border: 1px solid rgb(250,250,250);\n"
"border-radius: 3px")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 130, 120, 20))
        self.label_8.setStyleSheet(u"color: rgb(0,0,0);\n"
"background-color: rgb(250,250,250);\n"
"border-radius: 3px")
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(40, 190, 210, 73))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(0,255,0);\n"
"}")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 160, 40, 19))
        self.label_9.setStyleSheet(u"QLabel{color: rgb(245, 121, 0);\n"
"border-left: 1.5px solid rgb(245, 121, 0);}\n"
"")
        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setGeometry(QRect(30, 280, 230, 129))
        self.groupBox_5.setStyleSheet(u"border: 1px solid rgb(250,250,250);\n"
"border-radius: 3px")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 280, 120, 20))
        self.label_10.setStyleSheet(u"color: rgb(0,0,0);\n"
"background-color: rgb(250,250,250);\n"
"border-radius: 3px")
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(40, 310, 210, 89))
        self.plainTextEdit_2.setStyleSheet(u"QPlainTextEdit{\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(0,255,0);\n"
"}")
        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(270, 25, 480, 480))
        self.groupBox_6.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"")
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(35, 51, 410, 160))
        self.groupBox_7.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"")
        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(15, 121, 60, 20))
        self.label_13.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 3px;")
        self.label_25 = QLabel(self.groupBox_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(192, 121, 90, 20))
        self.label_25.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 3px;")
        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 80, 60, 20))
        self.label_11.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 3px;")
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 120, 60, 20))
        self.label_12.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 3px;")
        self.lineEdit = QLineEdit(self.groupBox_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(120, 119, 310, 26))
        self.lineEdit.setStyleSheet(u"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius: 2px;\n"
"")
        self.lineEdit_2 = QLineEdit(self.groupBox_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QRect(120, 79, 310, 26))
        self.lineEdit_2.setStyleSheet(u"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius: 2px;\n"
"")
        self.lineEdit_3 = QLineEdit(self.groupBox_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QRect(120, 170, 90, 26))
        self.lineEdit_3.setStyleSheet(u"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius: 2px;\n"
"")
        self.groupBox_8 = QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(35, 220, 410, 160))
        self.groupBox_8.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"")
        self.label_15 = QLabel(self.groupBox_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(15, 79, 60, 20))
        self.label_15.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 3px;")
        self.label_16 = QLabel(self.groupBox_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(15, 42, 80, 20))
        self.label_16.setStyleSheet(u"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 3px;")
        self.label_17 = QLabel(self.groupBox_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(110, 43, 130, 18))
        self.label_17.setStyleSheet(u"color: rgb(0,255,0);")
        self.pushButton_4 = QPushButton(self.groupBox_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(150, 111, 120, 40))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius:10px;\n"
"}")
        self.lineEdit_4 = QLineEdit(self.groupBox_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QRect(115, 298, 240, 26))
        self.lineEdit_4.setStyleSheet(u"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius: 2px;\n"
"")
        self.label_19 = QLabel(self.groupBox_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(2, 400, 471, 71))
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.lineEdit_5 = QLineEdit(self.groupBox_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QRect(330, 170, 100, 26))
        self.lineEdit_5.setStyleSheet(u"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius: 2px;\n"
"")
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(630, 320, 80, 31))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"color: rgb(245, 121, 0);\n"
"border: 1px solid rgb(245, 121, 0);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"color:rgb(0,255,0);\n"
"border: 1px solid rgb(0,255,0);\n"
"border-radius:10px;\n"
"}")
        self.groupBox_5.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.pushButton_3.raise_()
        self.groupBox_4.raise_()
        self.label_8.raise_()
        self.plainTextEdit.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.plainTextEdit_2.raise_()
        self.groupBox_6.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox.raise_()
        self.label.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hide My Message (HMM) V.1.0.0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hide My Message (HMM)", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Mode Options</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"     Hide", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"    Show", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Image Options</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/photos/hide.png\"/></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/photos/eye.png\"/></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.groupBox_4.setTitle("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"> Encryption</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"  Key:", None))
        self.groupBox_5.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Your Message</p></body></html>", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Informations and Progress", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Image Info :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Size :</p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Extension :</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Name :</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Path :</p></body></html>", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Process Info :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u" Output :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u" Operation :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"By: Abdullah Ibrahim", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
    # retranslateUi

