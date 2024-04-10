def encrypt(pla, key):
    pla = pla.lower()
    key = key.lower()
    cip = []
    # 定义好矩阵
    table = [['', key[0], key[1], key[2], key[3], key[4]], 
             [key[0], 'a', 'b', 'c', 'd', 'e'],
             [key[1], 'f', 'g', 'h', 'i', 'k'], 
             [key[2], 'l', 'm', 'n', 'o', 'p'], 
             [key[3], 'q', 'r', 's', 't', 'u'],
             [key[4], 'v', 'w', 'x', 'y', 'z']]
    for k in pla:
        # 当明文中有“j”的时候，当做“i”进行处理
        if k == 'j':
            k = 'i'
        for i in range(1, 6):
            for j in range(1, 6):
                if k == table[i][j] and k != 'j':
                    cip.append(table[i][0])
                    cip.append(table[0][j])
    cipertext = ''.join(cip)
    return cipertext

def main():
    # 只能有英文
    key = input("")
    plaintext = input("")
    
    # 密钥只能有5位，英文
    print(encrypt(plaintext, key))

if __name__ == '__main__':
    main()