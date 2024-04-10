
'''
Caesar cipher加密算法的实现
凯撒加密(Caesar cipher)是一种简单的消息编码方式,
根据字母表将消息中的每个字母移动常量位k
'''

def caesar_encrypt(plaintext, key):
    """第一个参数为明文字符串，第二个参数为向后移位的位数"""
    result = ''
    move = int(key) % 26
    for i in plaintext:
        pass
        # 如果是大写
        if i.isupper():
            result = result + chr(65 + (ord(i) + move - 65) % 26)
        elif i.islower():
            result = result + chr(97 + (ord(i) + move - 97) % 26)
    return result

def main():
    key = input()
    plaintext = input()

    print(caesar_encrypt(plaintext, key))

if __name__ == "__main__":
    main()