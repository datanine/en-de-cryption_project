import os
os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from Ui.Ui_ende import Ui_Form
from qt_material import apply_stylesheet
import subprocess

class MyWindows(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        apply_stylesheet(app, theme='light_blue.xml')

        self.initUI()
        self.bind()

    def initUI(self):
        # 映射加密算法到对应的加密程序
        self.Enalgorithms_mapping = {
            "Caesar cipher": "./En_code/Caesar.py",
            "Affine cipher": "./En_code/Affine.py",
            "Multilateral cipher": "./En_code/Multilateral.py",
            "Keyword cipher": "./En_code/Keyword.py",
            "Vigenere cipher": "./En_code/Vigenere.py",
            "Autokey ciphertext": "./En_code/Autokey_ciphertext.py",
            "Autokey plaintext": "./En_code/Autokey_plaintext.py",
            "Playfair cipher": "./En_code/Playfair.py",
            "Permutation cipher": "./En_code/Permutation.py",
            "Column permutation cipher": "./En_code/Column_permutation.py",
            "Rc4 cipher": "./En_code/Rc4.py",
            "Rsa cipher": "./En_code/Rsa.py",
        }

        # 映射解密算法到对应的解密程序
        self.Dealgorithms_mapping = {
            "Caesar cipher": "./De_code/Caesar.py",
            "Affine cipher": "./De_code/Affine.py",
            "Multilateral cipher": "./De_code/Multilateral.py",
            "Keyword cipher": "./De_code/Keyword.py",
            "Vigenere cipher": "./De_code/Vigenere.py",
            "Autokey ciphertext": "./De_code/Autokey_ciphertext.py",
            "Autokey plaintext": "./De_code/Autokey_plaintext.py",
            "Playfair cipher": "./De_code/Playfair.py",
            "Permutation cipher": "./De_code/Permutation.py",
            "Column permutation cipher": "./De_code/Column_permutation.py",
            "Rc4 cipher": "./De_code/Rc4.py",
            "Rsa cipher": "./De_code/Rsa.py",
        }

    def bind(self):
        self.EnButton.clicked.connect(self.encryptText)
        self.DeButton.clicked.connect(self.decryptText)
        
        self.EnFileButton.clicked.connect(self.showEnfile)
        self.DeFileButton.clicked.connect(self.showDefile)

# 加密端
    def encryptText(self):
        # 获取输入文本
        key = self.EnKeytext.toPlainText()
        input_text = self.EnPlaintext.toPlainText()

        # 获取选择的加密方式
        selected_encryption = self.EnAlgorithm.currentText()

        if selected_encryption in self.Enalgorithms_mapping:
            process = subprocess.Popen(['python', self.Enalgorithms_mapping[selected_encryption]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        else:
            # 处理未知的加密程序选择
            print("Invalid encryption selection.")
            return

        # 向加密程序传递密钥
        process.stdin.write(key + '\n')
        process.stdin.flush()
        # 向加密程序传递文本
        process.stdin.write(input_text + '\n;')
        process.stdin.flush()

        # 从标准输出中读取加密结果
        output, errors = process.communicate(input_text + '\n;')  # 输入文本并在末尾加上分号表示结束

        if errors:
            print(f"Error: {errors}")
        else:
            print(f"Output: {output}")

        # 将加密结果显示在输出QTextEdit中
        self.Enresult.setPlainText(output)

    def showEnfile(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '.')
        if filename:
            self.EnFileline.setText(filename)
            with open(filename, 'r') as file:
                content = file.read()
                self.EnPlaintext.setPlainText(content)

# 解密端
    def decryptText(self):
        # 获取输入文本
        key = self.DeKeytext.toPlainText()
        input_text = self.DePlaintext.toPlainText()

        # 获取选择的解密方式
        selected_decryption = self.DeAlgorithm.currentText()

        if selected_decryption in self.Dealgorithms_mapping:
            process = subprocess.Popen(['python', self.Dealgorithms_mapping[selected_decryption]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        else:
            # 处理未知的解密程序选择
            print("Invalid encryption selection.")
            return

        # 向解密程序传递密钥
        process.stdin.write(key + '\n')
        process.stdin.flush()
        # 向解密程序传递文本
        process.stdin.write(input_text + '\n;')
        process.stdin.flush()

        # 从标准输出中读取解密结果
        output, errors = process.communicate(input_text + '\n;')  # 输入文本并在末尾加上分号表示结束

        if errors:
            print(f"Error: {errors}")
        else:
            print(f"Output: {output}")

        # 将解密结果显示在输出QTextEdit中
        self.Deresult.setPlainText(output)

    def showDefile(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '.')
        if filename:
            self.DeFileline.setText(filename)
            with open(filename, 'r') as file:
                content = file.read()
                self.DePlaintext.setPlainText(content)


if __name__ == '__main__':
    app = QApplication([])
    windows = MyWindows()
    windows.show()
    app.exec()
