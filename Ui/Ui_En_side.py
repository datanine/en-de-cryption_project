# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'En_side.ui'
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
        Form.resize(478, 746)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 436, 722))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.EnPlaintext = QTextEdit(self.groupBox)
        self.EnPlaintext.setObjectName(u"EnPlaintext")

        self.gridLayout.addWidget(self.EnPlaintext, 0, 2, 1, 4)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.Enresult = QTextEdit(self.groupBox)
        self.Enresult.setObjectName(u"Enresult")

        self.gridLayout.addWidget(self.Enresult, 5, 2, 1, 4)

        self.EnFileButton = QToolButton(self.groupBox)
        self.EnFileButton.setObjectName(u"EnFileButton")
        self.EnFileButton.setFont(font1)

        self.gridLayout.addWidget(self.EnFileButton, 2, 5, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.EnAlgorithm = QComboBox(self.groupBox)
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.setObjectName(u"EnAlgorithm")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.EnAlgorithm.setFont(font2)

        self.gridLayout.addWidget(self.EnAlgorithm, 4, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.EnButton = QPushButton(self.groupBox)
        self.EnButton.setObjectName(u"EnButton")
        self.EnButton.setMaximumSize(QSize(160, 16777215))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.EnButton.setFont(font3)

        self.gridLayout.addWidget(self.EnButton, 6, 3, 1, 1)

        self.EnKeytext = QPlainTextEdit(self.groupBox)
        self.EnKeytext.setObjectName(u"EnKeytext")

        self.gridLayout.addWidget(self.EnKeytext, 3, 2, 1, 4)

        self.SendSocket = QPushButton(self.groupBox)
        self.SendSocket.setObjectName(u"SendSocket")
        self.SendSocket.setFont(font1)

        self.gridLayout.addWidget(self.SendSocket, 6, 4, 1, 1)

        self.EnFileline = QLineEdit(self.groupBox)
        self.EnFileline.setObjectName(u"EnFileline")

        self.gridLayout.addWidget(self.EnFileline, 2, 3, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u52a0\u5bc6\u7aef\u670d\u52a1", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Encryption", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"File", None))
        self.EnPlaintext.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5f85\u52a0\u5bc6\u6587\u672c...", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Encryption</p><p>Result</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Encryption</p><p>Algorithm</p></body></html>", None))
        self.Enresult.setPlaceholderText(QCoreApplication.translate("Form", u"\u663e\u793a\u5bc6\u6587\u4e2d...", None))
        self.EnFileButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.label.setText(QCoreApplication.translate("Form", u"Plaintext", None))
        self.EnAlgorithm.setItemText(0, QCoreApplication.translate("Form", u"Caesar cipher", None))
        self.EnAlgorithm.setItemText(1, QCoreApplication.translate("Form", u"Affine cipher", None))
        self.EnAlgorithm.setItemText(2, QCoreApplication.translate("Form", u"Multilateral cipher", None))
        self.EnAlgorithm.setItemText(3, QCoreApplication.translate("Form", u"Keyword cipher", None))
        self.EnAlgorithm.setItemText(4, QCoreApplication.translate("Form", u"Vigenere cipher", None))
        self.EnAlgorithm.setItemText(5, QCoreApplication.translate("Form", u"Autokey ciphertext", None))
        self.EnAlgorithm.setItemText(6, QCoreApplication.translate("Form", u"Autokey plaintext", None))
        self.EnAlgorithm.setItemText(7, QCoreApplication.translate("Form", u"Playfair cipher", None))
        self.EnAlgorithm.setItemText(8, QCoreApplication.translate("Form", u"Permutation cipher", None))
        self.EnAlgorithm.setItemText(9, QCoreApplication.translate("Form", u"Column permutation cipher", None))
        self.EnAlgorithm.setItemText(10, QCoreApplication.translate("Form", u"Rc4 cipher", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"Key", None))
        self.EnButton.setText(QCoreApplication.translate("Form", u"Encryption", None))
        self.EnKeytext.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u94a5", None))
        self.SendSocket.setText(QCoreApplication.translate("Form", u"Send", None))
        self.EnFileline.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
    # retranslateUi

