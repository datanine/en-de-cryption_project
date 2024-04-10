#  对明文消息按照密钥（key）的长度进行分块，使每个块的长度与密钥相等
def msgToChunks(msg, key):
    msg = msg.replace(' ', '')
    while len(msg) % len(key) != 0:
        msg += ' '
    chunks = []
    for i in range(0, len(msg), len(key)):
        chunks.append(msg[i:i + len(key)])
    return chunks

# 对分块后的消息按照密钥规定的顺序进行列置换
def transpose(chunks, order):
    result = ''
    for x in chunks:
        for pos in order:
            result += x[pos]
    return result.replace(' ', '')

def keyToEncrptyOrder(key):
    order = [0] * len(key)
    sorted_key = ''.join(sorted(key))
    for i, x in enumerate(key):
        order[sorted_key.find(x)] = i
    # print(order)
    return order

def encrypt(msg, key):
    msg = msg.replace(' ', '')
    chunks = msgToChunks(msg, key)
    order = keyToEncrptyOrder(key)
    return transpose(chunks, order)

def main():
    key = input()
    plaintext = input()
    print(encrypt(plaintext, key))

if __name__ == '__main__':
    main()
    
# def test():
#     print(encrypt('get the ball', '34152'))
#     print(decrypt('thgetalebl', '34152'))