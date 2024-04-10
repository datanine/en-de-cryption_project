# 将字母A-Z转化成0-26的数
def strCGnum(str):
    if len(str) == 1:
        return ord(str) - 65
    else:
        tmpstr = []
        for i in range(len(str)):
            tmpstr.append(ord(str[i]) - 65)
        return tmpstr

# 将0-26的数转化为字母A-Z
def numCGstr(str):
    tmpstr = ""
    for i in str:
        tmpstr += chr(i + 65)
    return tmpstr

# 转化为大写
def strupper(str):
    s = ""
    s += str
    return s.upper()

# 使得密钥长度和明文一致
def expendkey(key, length):
    if len(key) > length:
        return key[:length]
    elif len(key) == length:
        return key
    else:
        while len(key) < length:
            key += key
        if len(key) != length:
            return key[:length]
        else:
            return key

# 加密
def encrypt(plaintext, key):
    plaintext = strupper(plaintext)
    tmpkey = strupper(key)
    Key = expendkey(tmpkey, len(plaintext))
    tmpciphertext = []
    for index, item in enumerate(plaintext):
        tmpciphertext.append(((strCGnum(Key[index]) + strCGnum(item)) % 26))
    return numCGstr(tmpciphertext)

def main():
    key = input()
    plaintext = input()
    
    ciphertext = encrypt(plaintext, key)
    print(ciphertext, end='')

if __name__ == "__main__":
    main()