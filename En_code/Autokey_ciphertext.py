def encrypt(plain, keytext):
    plaintext = plain
    len1 = len(plain)
    len2 = len(keytext)
    key = keytext + plaintext[0:len1 - len2]
    matrix = [([0] * 26) for i in range(26)]
    for x in range(26):  # 生成加密的26*26矩阵
        for y in range(26):
            t = 65 + y + x
            if t > 90:
                matrix[x][y] = chr(t - 26)
            if t <= 90:
                matrix[x][y] = chr(t)

    # for x in range(26):  # 矩阵输出
    #     for y in range(26):
    #         print(matrix[x][y], end='')
    #         if y == 25:
    #             print(' ')

    keyword = ''  # 后面的大写密钥
    for x in key:  # 将密钥全部转化为大写
        if ord(x) >= 97:
            x = chr(ord(x) - 32)
        keyword = keyword + x
    # print("明文为：" + plaintext)
    # print("密钥为：" + keyword)

    textsize = len(plaintext)  # 明文长度
    keysize = len(key)  # 密钥长度
    pkmat = [([0] * 2) for i in range(textsize)]  # 加密一对一对照矩阵

    ciphertext = ''
    t = 0  # 用于密钥和明文匹配时循环判断
    for i in range(textsize):
        t = t % keysize
        pkmat[i][0] = plaintext[i]
        pkmat[i][1] = keyword[t]
        t = t + 1
    # print("加密一对一矩阵： ", end='')
    # print(pkmat)  # 至此，对照表完成，接下来进行转换

    for i in range(textsize):
        if ord(pkmat[i][0]) >= 97:
            t = ord(pkmat[i][0]) - 97
            x = ord(pkmat[i][1]) - 65
            ciphertext = ciphertext + chr(ord(matrix[t][x]) + 32)
        if ord(pkmat[i][0]) < 97:
            t = ord(pkmat[i][0]) - 65
            x = ord(pkmat[i][1]) - 65
            ciphertext = ciphertext + chr(ord(matrix[t][x]))
    return ciphertext

def main():
    key = input()
    plaintext = input()

    ciphertext = encrypt(plaintext, key)
    print(ciphertext)

if __name__ == "__main__":
    main()