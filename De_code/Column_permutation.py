# 获得读取顺序，返回一个读取列号的列表
def getOrder(key):
    result = []
    tmp = []
    for i in key:
        tmp.append(ord(i))
    order = tmp.copy()
    order.sort()
    tmporder = set(order)
    for i in tmporder:
        if order.count(i) == 1:
            result.append(tmp.index(i))
        else:
            uniqueindex = unique_index(tmp, i)
            for j in uniqueindex:
                result.append(j)
    return result

# 输入列表和元素，返回列表中和该元素相等的元素的序号的列表
def unique_index(L, e):
    return [i for (i, j) in enumerate(L) if j == e]

# 向明文尾部填充字符e
def padding(plaintext, m):
    while len(plaintext) % m != 0:
        plaintext += "e"
    return plaintext

# 解密
def decrypt(ciphertext, key):
    plaintext = ""
    m = len(key)
    Ciphertext = padding(ciphertext, m)
    n = len(ciphertext) // m
    order = getOrder(key)
    readorder = []
    for i in range(len(order)):
        readorder.append(order.index(i))
    for i in range(n):
        for j in readorder:
            plaintext += Ciphertext[i + j * n]
    return plaintext

def main():
    key = input()
    ciphertext = input()
    
    plaintext = decrypt(ciphertext, key)
    print(plaintext)

if __name__ == "__main__":
    main()