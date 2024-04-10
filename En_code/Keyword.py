import string

def encrypt(plaintext, ci_key):
    plaintext = list(plaintext.lower())
    ciphertext = list(string.ascii_lowercase)
    ci_key = list(ci_key.lower())
    key = []
    for i in ci_key:
        if i not in key:
            key.append(i)
    for i in ciphertext:
        if i not in key:
            key.append(i)
    all_letter = list(string.ascii_lowercase)
    ciphertext = []
    for i in plaintext:
        for j in range(26):
            if i == all_letter[j]:
                ciphertext.append(key[j])
    return "".join(list(ciphertext)), "".join(list(key))

def main():
    ci_key = input()
    plaintext = input()
    ciphertext= encrypt(plaintext, ci_key)
    print(ciphertext)

if __name__ == '__main__':
    main()