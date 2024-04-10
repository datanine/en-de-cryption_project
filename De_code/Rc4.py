import codecs

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

    def decrypt(self, key, ciphertext):
        ciphertext = codecs.decode(ciphertext, 'hex_codec')
        res = self.encrypt_logic(key, ciphertext)
        return codecs.decode(res, 'hex_codec').decode('utf-8')

def main():
    rc_instance = RC4()
    key = input()
    ciphertext = input()
    plaintext = rc_instance.decrypt(key, ciphertext)
    print(plaintext)

if __name__ == '__main__':
    main()