import os
os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from Ui.Ui_De_side import Ui_Form
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
        self.run()

    def initUI(self):
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
        }

    def bind(self):
        self.DeButton.clicked.connect(self.decryptText)
        self.DeAlgorithm.currentIndexChanged.connect(self.Algorithm_change)

        self.DeFileButton.clicked.connect(self.showDefile)
        self.Save_cipherText.clicked.connect(self.save_to_file)

    def run(self):
        # 设置解密端的IP地址和端口
        server_ip = '0.0.0.0'
        server_port = 50000

        # 创建socket对象
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 绑定IP地址和端口
        server_socket.bind((server_ip, server_port))

        # 监听连接
        server_socket.listen(5)
        print(f"Decryption Server listening on {server_ip}:{server_port}")

        # 等待加密客户端连接
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # 接收密钥、加密信息和加密算法
        received_data = client_socket.recv(1024).decode('utf-8')
        print(received_data)
        key, ciphertext, algorithm = received_data.splitlines()

        print(f"Received key: {key}")
        print(f"Received ciphertext: {ciphertext}")
        print(f"Received algorithm: {algorithm}")


        # 进行解密
        self.decryptText(key, ciphertext, algorithm)

        # # 发送解密后的消息
        # self.data_received.emit(decrypted_message)

        # 关闭连接
        client_socket.close()
        server_socket.close()

# 解密端
    def decryptText(self, key, ciphertext, algorithm):
        # 获取输入文本
        # key = self.DeKeytext.toPlainText()
        # ciphertext = self.DeCiphertext.toPlainText()
        self.DeKeytext.setPlainText(key)
        self.DeCiphertext.setPlainText(ciphertext)

        # 获取选择的解密方式
        # selected_decryption = self.DeAlgorithm.findText(algorithm)
        self.Algorithm_change(algorithm)

        if algorithm in self.Dealgorithms_mapping:
            process = subprocess.Popen(['python', self.Dealgorithms_mapping[algorithm]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        else:
            # 处理未知的解密程序选择
            print("Invalid encryption selection.")
            return

        # 向解密程序传递密钥
        process.stdin.write(key + '\n')
        process.stdin.flush()
        # 向解密程序传递文本
        process.stdin.write(ciphertext + '\n;')
        process.stdin.flush()

        # 从标准输出中读取解密结果
        output, errors = process.communicate(ciphertext + '\n;')  # 输入文本并在末尾加上分号表示结束

        if errors:
            print(f"Error: {errors}")
        else:
            print(f"Output: {output}")

        # 将解密结果显示在输出QTextEdit中
        self.Deresult.setPlainText(output)

    def Algorithm_change(self, algorithm):
        # 通过 findData 方法找到匹配的项的索引
        index = self.DeAlgorithm.findText(str(algorithm))

        if index >= 0:
            # 找到匹配项，设置 QComboBox 的当前索引
            self.DeAlgorithm.setCurrentIndex(index)
        
    def save_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.Deresult.toPlainText())

    def showDefile(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', '.')
        if filename:
            self.DeFileline.setText(filename)
            with open(filename, 'r') as file:
                content = file.read()
                self.DeCiphertext.setPlainText(content)


if __name__ == '__main__':
    app = QApplication([])
    windows = MyWindows()
    windows.show()
    app.exec()
