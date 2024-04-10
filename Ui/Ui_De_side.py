# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'De_side.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QTextEdit, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(475, 749)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 10, 436, 722))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.DeAlgorithm = QComboBox(self.groupBox_2)
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.setObjectName(u"DeAlgorithm")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.DeAlgorithm.setFont(font2)

        self.gridLayout_2.addWidget(self.DeAlgorithm, 3, 2, 1, 3)

        self.DeButton = QPushButton(self.groupBox_2)
        self.DeButton.setObjectName(u"DeButton")
        self.DeButton.setMinimumSize(QSize(160, 0))
        self.DeButton.setMaximumSize(QSize(16777215, 16777215))
        self.DeButton.setFont(font1)

        self.gridLayout_2.addWidget(self.DeButton, 5, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.DeFileline = QLineEdit(self.groupBox_2)
        self.DeFileline.setObjectName(u"DeFileline")

        self.gridLayout_2.addWidget(self.DeFileline, 1, 2, 1, 3)

        self.DeCiphertext = QTextEdit(self.groupBox_2)
        self.DeCiphertext.setObjectName(u"DeCiphertext")

        self.gridLayout_2.addWidget(self.DeCiphertext, 0, 2, 1, 4)

        self.Deresult = QTextEdit(self.groupBox_2)
        self.Deresult.setObjectName(u"Deresult")

        self.gridLayout_2.addWidget(self.Deresult, 4, 2, 1, 4)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.DeFileButton = QToolButton(self.groupBox_2)
        self.DeFileButton.setObjectName(u"DeFileButton")
        self.DeFileButton.setFont(font1)

        self.gridLayout_2.addWidget(self.DeFileButton, 1, 5, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 2)

        self.DeKeytext = QPlainTextEdit(self.groupBox_2)
        self.DeKeytext.setObjectName(u"DeKeytext")

        self.gridLayout_2.addWidget(self.DeKeytext, 2, 2, 1, 4)

        self.Save_cipherText = QPushButton(self.groupBox_2)
        self.Save_cipherText.setObjectName(u"Save_cipherText")
        self.Save_cipherText.setMinimumSize(QSize(0, 0))
        self.Save_cipherText.setMaximumSize(QSize(16777215, 16777215))
        self.Save_cipherText.setFont(font1)

        self.gridLayout_2.addWidget(self.Save_cipherText, 5, 4, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u89e3\u5bc6\u7aef\u670d\u52a1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Decryption", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Decryption</p><p>Result</p></body></html>", None))
        self.DeAlgorithm.setItemText(0, QCoreApplication.translate("Form", u"Caesar cipher", None))
        self.DeAlgorithm.setItemText(1, QCoreApplication.translate("Form", u"Affine cipher", None))
        self.DeAlgorithm.setItemText(2, QCoreApplication.translate("Form", u"Multilateral cipher", None))
        self.DeAlgorithm.setItemText(3, QCoreApplication.translate("Form", u"Keyword cipher", None))
        self.DeAlgorithm.setItemText(4, QCoreApplication.translate("Form", u"Vigenere cipher", None))
        self.DeAlgorithm.setItemText(5, QCoreApplication.translate("Form", u"Autokey ciphertext", None))
        self.DeAlgorithm.setItemText(6, QCoreApplication.translate("Form", u"Autokey plaintext", None))
        self.DeAlgorithm.setItemText(7, QCoreApplication.translate("Form", u"Playfair cipher", None))
        self.DeAlgorithm.setItemText(8, QCoreApplication.translate("Form", u"Permutation cipher", None))
        self.DeAlgorithm.setItemText(9, QCoreApplication.translate("Form", u"Column permutation cipher", None))
        self.DeAlgorithm.setItemText(10, QCoreApplication.translate("Form", u"Rc4 cipher", None))

        self.DeButton.setText(QCoreApplication.translate("Form", u"Decryption", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"File", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Key", None))
        self.DeFileline.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.DeCiphertext.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u6587...", None))
        self.Deresult.setPlaceholderText(QCoreApplication.translate("Form", u"\u663e\u793a\u89e3\u5bc6\u6587\u672c\u4e2d...", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ciphertext", None))
        self.DeFileButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Decryption</p><p>Algorithm</p></body></html>", None))
        self.DeKeytext.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u94a5...", None))
        self.Save_cipherText.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

