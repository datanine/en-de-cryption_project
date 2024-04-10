def jiemi(miwen, kkkkey):
    matrix = [([0] * 26) for i in range(26)]
    for x in range(26):  # 生成加密的26*26矩阵
        for y in range(26):
            t = 65 + y + x
            if t > 90:
                matrix[x][y] = chr(t - 26)
            if t <= 90:
                matrix[x][y] = chr(t)
    key = kkkkey
    keysize = len(key)
    textsize = len(miwen)
    kkmat = [([0] * 2) for i in range(textsize)]  # 解密一对一对照矩阵
    t = 0  # 用于密钥和密文匹配时循环判断
    for i in range(textsize):  # 生成解密一对一矩阵
        t = t % keysize
        kkmat[i][0] = miwen[i]
        kkmat[i][1] = key[t]
        t = t + 1
    pptext = ''
    for i in range(textsize):  # 解密过程，区分大小写的解密
        for x in range(26):
            # print(ord(kkmat[i][1]))
            if ord(kkmat[i][0]) < 97:
                if (ord(kkmat[i][1]) <= 90):
                    y = (ord(kkmat[i][1]) - 65)
                else:
                    y = (ord(kkmat[i][1]) - 97)
                if matrix[y][x] == kkmat[i][0]:
                    pptext = pptext + chr(x + 65)
                    break
            if ord(kkmat[i][0]) >= 97:
                if (ord(kkmat[i][1]) <= 90):
                    y = (ord(kkmat[i][1]) - 65)
                else:
                    y = (ord(kkmat[i][1]) - 97)
                if matrix[y][x] == chr(ord(kkmat[i][0]) - 32):
                    pptext = pptext + chr(x + 97)
                    break
    return pptext

def decrypt(ciphertext, kkkey):
    len1 = len(ciphertext)
    len2 = len(kkkey)
    t = int(len1 / len2)  # 循环次数
    z = len1 % len2
    plaintext = ''
    key = kkkey
    for i in range(t):
        key = jiemi(ciphertext[i * len2:(i + 1) * len2], key)
        print(key)
        plaintext = plaintext + key
    mmm = jiemi(ciphertext[len1 - z:len1], key[:z])
    plaintext = plaintext + mmm

    return plaintext

def main():
    key = input()
    ciphertext = input()

    plaintext = decrypt(ciphertext, key)
    print(plaintext)

    # 示例：
    # print(encrypt("anautokeycipherprovidedesalongkeyword", "cap"))
    # print(decrypt("cnpugoexmmmnjmgwvfkzrzlhwdpgnryregspz", "cap"))

if __name__ == "__main__":
    main()