class RC4:

    def KSA(self, key):
        # Key Scheduling Algorithm
        len_key = len(key)
        S = list(range(256))
        # S = [0,1,2, ... , 255]
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % len_key]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def PRGA(self, S):
        i = 0
        j = 0
        K = []
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
            yield K

    def get_keystream(self, key):
        S = self.KSA(key)
        return self.PRGA(S)

    def encrypt_logic(self, key, text):
        key = [ord(c) for c in key]
        keystream = self.get_keystream(key)
        res = []
        for c in text:
            val = ("%02X" % (c ^ next(keystream)))
            res.append(val)
        return ''.join(res)

    def encrypt(self, key, plaintext):
        plaintext = [ord(c) for c in plaintext]
        return self.encrypt_logic(key, plaintext)

def main():
    rc_instance = RC4()
    key = input()
    plaintext = input()
    ciphertext = rc_instance.encrypt(key, plaintext)
    print(ciphertext)

if __name__ == '__main__':
    main()