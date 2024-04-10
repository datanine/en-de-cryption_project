# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ende.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QTextEdit, QToolButton,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(896, 740)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.EnButton = QPushButton(self.groupBox)
        self.EnButton.setObjectName(u"EnButton")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.EnButton.setFont(font1)

        self.gridLayout.addWidget(self.EnButton, 6, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.label_9.setFont(font2)

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.EnFileButton = QToolButton(self.groupBox)
        self.EnFileButton.setObjectName(u"EnFileButton")
        self.EnFileButton.setFont(font2)

        self.gridLayout.addWidget(self.EnFileButton, 2, 4, 1, 1)

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
        self.EnAlgorithm.addItem("")
        self.EnAlgorithm.setObjectName(u"EnAlgorithm")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.EnAlgorithm.setFont(font3)

        self.gridLayout.addWidget(self.EnAlgorithm, 4, 3, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.EnPlaintext = QTextEdit(self.groupBox)
        self.EnPlaintext.setObjectName(u"EnPlaintext")

        self.gridLayout.addWidget(self.EnPlaintext, 0, 2, 1, 3)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.Enresult = QTextEdit(self.groupBox)
        self.Enresult.setObjectName(u"Enresult")

        self.gridLayout.addWidget(self.Enresult, 5, 2, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.EnFileline = QLineEdit(self.groupBox)
        self.EnFileline.setObjectName(u"EnFileline")

        self.gridLayout.addWidget(self.EnFileline, 2, 3, 1, 1)

        self.EnKeytext = QPlainTextEdit(self.groupBox)
        self.EnKeytext.setObjectName(u"EnKeytext")

        self.gridLayout.addWidget(self.EnKeytext, 3, 2, 1, 2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.DeFileline = QLineEdit(self.groupBox_2)
        self.DeFileline.setObjectName(u"DeFileline")

        self.gridLayout_2.addWidget(self.DeFileline, 1, 2, 1, 1)

        self.DeKeytext = QPlainTextEdit(self.groupBox_2)
        self.DeKeytext.setObjectName(u"DeKeytext")

        self.gridLayout_2.addWidget(self.DeKeytext, 2, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 2)

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
        self.DeAlgorithm.addItem("")
        self.DeAlgorithm.setObjectName(u"DeAlgorithm")
        self.DeAlgorithm.setFont(font3)

        self.gridLayout_2.addWidget(self.DeAlgorithm, 3, 2, 1, 2)

        self.Deresult = QTextEdit(self.groupBox_2)
        self.Deresult.setObjectName(u"Deresult")

        self.gridLayout_2.addWidget(self.Deresult, 4, 2, 1, 2)

        self.DeButton = QPushButton(self.groupBox_2)
        self.DeButton.setObjectName(u"DeButton")
        self.DeButton.setFont(font2)

        self.gridLayout_2.addWidget(self.DeButton, 5, 2, 1, 1)

        self.DeFileButton = QToolButton(self.groupBox_2)
        self.DeFileButton.setObjectName(u"DeFileButton")
        self.DeFileButton.setFont(font2)

        self.gridLayout_2.addWidget(self.DeFileButton, 1, 3, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.DePlaintext = QTextEdit(self.groupBox_2)
        self.DePlaintext.setObjectName(u"DePlaintext")

        self.gridLayout_2.addWidget(self.DePlaintext, 0, 2, 1, 2)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u52a0\u89e3\u5bc6\u6d4b\u8bd5", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Encryption", None))
        self.EnButton.setText(QCoreApplication.translate("Form", u"Encryption", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Key", None))
        self.EnFileButton.setText(QCoreApplication.translate("Form", u"...", None))
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
        self.EnAlgorithm.setItemText(11, QCoreApplication.translate("Form", u"Rsa cipher", None))

        self.label.setText(QCoreApplication.translate("Form", u"Plaintext", None))
        self.EnPlaintext.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5f85\u52a0\u5bc6\u6587\u672c...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"File", None))
        self.Enresult.setPlaceholderText(QCoreApplication.translate("Form", u"\u663e\u793a\u5bc6\u6587\u4e2d...", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Encryption</p><p>Algorithm</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Encryption</p><p>Result</p></body></html>", None))
#if QT_CONFIG(accessibility)
        self.EnFileline.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.EnFileline.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.EnKeytext.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u94a5...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Decryption", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Key", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"File", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ciphertext", None))
        self.DeFileline.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.DeKeytext.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u94a5...", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Decryption</p><p>Algorithm</p></body></html>", None))
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
        self.DeAlgorithm.setItemText(11, QCoreApplication.translate("Form", u"Rsa cipher", None))

        self.Deresult.setPlaceholderText(QCoreApplication.translate("Form", u"\u663e\u793a\u89e3\u5bc6\u6587\u672c\u4e2d...", None))
        self.DeButton.setText(QCoreApplication.translate("Form", u"Decryption", None))
        self.DeFileButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Decryption</p><p>Result</p></body></html>", None))
        self.DePlaintext.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u6587...", None))
    # retranslateUi

