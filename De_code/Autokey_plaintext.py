def decrypt(cipherText, key):
    alphabet = [chr(65 + x) for x in range(26)]
    cipherTable = []
    count1 = 0
    for x in range(26):
        row = alphabet[count1:] + alphabet[:count1]
        cipherTable.append(row)
        count1 += 1
    keyList = [x.upper() for x in key]
    cipherTextList = [x.upper() for x in cipherText]
    cipherTextList.reverse()
    keyList.reverse()
    plainTextList, count2 = [], 0

    for x in range(len(cipherTextList)):
        plainTextList.append(
            chr((cipherTable[ord(cipherTextList[x + len(keyList)]) - ord("A")].index(cipherTextList[x])) + ord("A")))
        count2 += 1
        if count2 >= len(cipherTextList) - len(keyList):
            break

    for x, y in zip(keyList, cipherTextList[len(cipherTextList) - len(keyList):]):
        plainTextList.append(chr(cipherTable[ord(x) - ord("A")].index(y) + ord("A")))
    plainTextList.reverse()

    plainText = ""
    for x in plainTextList:
        plainText += x
    return plainText

def main():
    key = input()
    ciphertext = input()
    
    plaintext = decrypt(ciphertext, key)
    print(plaintext)

if __name__ == "__main__":
    main()