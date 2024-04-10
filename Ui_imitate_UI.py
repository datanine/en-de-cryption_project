# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imitate_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.interface_label = QLabel(Form)
        self.interface_label.setObjectName(u"interface_label")
        self.interface_label.setGeometry(QRect(20, 10, 61, 21))
        self.interface_edit = QLineEdit(Form)
        self.interface_edit.setObjectName(u"interface_edit")
        self.interface_edit.setGeometry(QRect(20, 40, 113, 20))
        self.gateway_label = QLabel(Form)
        self.gateway_label.setObjectName(u"gateway_label")
        self.gateway_label.setGeometry(QRect(20, 80, 51, 21))
        self.gateway_edit = QLineEdit(Form)
        self.gateway_edit.setObjectName(u"gateway_edit")
        self.gateway_edit.setGeometry(QRect(20, 110, 113, 20))
        self.target_label = QLabel(Form)
        self.target_label.setObjectName(u"target_label")
        self.target_label.setGeometry(QRect(20, 150, 51, 21))
        self.target_edit = QLineEdit(Form)
        self.target_edit.setObjectName(u"target_edit")
        self.target_edit.setGeometry(QRect(20, 180, 113, 20))
        self.Description_label = QLabel(Form)
        self.Description_label.setObjectName(u"Description_label")
        self.Description_label.setGeometry(QRect(160, 10, 71, 16))
        self.Description_text = QTextBrowser(Form)
        self.Description_text.setObjectName(u"Description_text")
        self.Description_text.setGeometry(QRect(150, 40, 231, 161))
        self.attack_button = QPushButton(Form)
        self.attack_button.setObjectName(u"attack_button")
        self.attack_button.setGeometry(QRect(40, 240, 75, 24))
        self.scan_button = QPushButton(Form)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setGeometry(QRect(230, 240, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.interface_label.setText(QCoreApplication.translate("Form", u"Interface:", None))
        self.gateway_label.setText(QCoreApplication.translate("Form", u"Gateway:", None))
        self.target_label.setText(QCoreApplication.translate("Form", u"Target_ip:", None))
        self.Description_label.setText(QCoreApplication.translate("Form", u"Description", None))
        self.attack_button.setText(QCoreApplication.translate("Form", u"ARP Attack", None))
        self.scan_button.setText(QCoreApplication.translate("Form", u"Scan Hosts", None))
    # retranslateUi

