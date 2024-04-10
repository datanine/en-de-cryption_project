table_encrypt = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5,
                 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
                 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
table_decrypt = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 
                 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 
                 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 
                 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

# 加密
def encrypt(plaintext, key_a, key_b):
    key_a = key_a % 26
    key_b = key_b % 26
    result = ""
    for i in filter_clear(plaintext):
        result += table_decrypt.get((key_a * table_encrypt.get(i) + key_b) % 26)
    return result

def filter_clear(clear): # 过滤大写字母，并将大写字母转换为小写字母
    result = ""
    clear = clear.lower()
    for i in clear:
        if 97 <= ord(i) <= 122:
            result += i
    return result

def main():
    a = int(input())
    b = int(input())
    plaintext = input()

    ciphertext = encrypt(plaintext, a, b)
    print(ciphertext)

if __name__ == '__main__':
    main()