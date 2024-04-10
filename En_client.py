import os
import sys
os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from Ui.Ui_En_side import Ui_Form
from qt_material import apply_stylesheet
import subprocess
import socket

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
        }

    # 信号绑定
    def bind(self):
        self.EnButton.clicked.connect(self.encryptText)
        self.EnFileButton.clicked.connect(self.showEnfile)

        self.SendSocket.clicked.connect(self.sendData)

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

    def sendData(self):
        # 获取密钥和消息
        key = self.EnKeytext.toPlainText()
        ciphertext = self.Enresult.toPlainText()
        selected_encryption = self.EnAlgorithm.currentText()

        # 创建socket对象
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设置服务端的IP地址和端口
        server_ip = '127.0.0.1'
        server_port = 50000

        try:
            # 连接到服务端
            client_socket.connect((server_ip, server_port))

            # 发送密钥、加密信息和加密方式
            data_to_send = f"{key}\n{ciphertext}{selected_encryption}"
            client_socket.sendall(data_to_send.encode('utf-8'))

            # client_socket.sendall(key.encode('utf-8') + '\n')
            # client_socket.sendall(ciphertext.encode('utf-8') + '\n')
            # client_socket.sendall(selected_encryption.encode('utf-8') + '\n')

            # 关闭连接
            client_socket.close()
        except Exception as e:
            print(f"Error: {e}")

    # 文件内容展示
    def showEnfile(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '.')
        if filename:
            self.EnFileline.setText(filename)
            with open(filename, 'r') as file:
                content = file.read()
                self.EnPlaintext.setPlainText(content) 

if __name__ == '__main__':
    app = QApplication([])
    windows = MyWindows()
    windows.show()
    app.exec()
