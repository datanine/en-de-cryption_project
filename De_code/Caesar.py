def caesar_decrypt(ciphertext, key):
    result = ''
    move = int(key) % 26
    for i in ciphertext:
        # 如果是大写
        if i.isupper():
            result = result + chr(65 + (ord(i) - move - 65) % 26)
        elif i.islower():
            result = result + chr(97 + (ord(i) - move - 97) % 26)
    return result

def main():
    key = input()
    ciphertext = input()

    print(caesar_decrypt(ciphertext, key))

if __name__ == "__main__":
    main()