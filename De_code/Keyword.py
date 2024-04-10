import string

def decrypt(ciphertext, ci_key):
    str_ciphertext = list(string.ascii_lowercase)
    ci_key = list(ci_key.lower())
    key = []
    for i in ci_key:
        if i not in key:
            key.append(i)
    for i in str_ciphertext:
        if i not in key:
            key.append(i)
    all_letter = string.ascii_lowercase
    plaintext = []
    ciphertext = list(ciphertext)
    for i in ciphertext:
        for j in range(26):
            if i == key[j]:
                plaintext.append(all_letter[j])
    return "".join(list(plaintext))

def main():
    ci_key = input()
    ciphertext = input()
    plaintext = decrypt(ciphertext, ci_key)
    print(plaintext)

if __name__ == '__main__':
    main()