alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#SUBJECT TO CHANGE!

class CeasarCipher:
    def __init__(self, shift=5):
        self.shift = shift

    def __str__(self):
        return 'Ceasar Cipher with Shift: ' + str(self.shift)

    def encode(self, plaintext, order=1):
        return ''.join([list(alphabet)[int(i) + self.shift * order] if isinstance(i, int) else i for i in [list(alphabet).index(k.upper()) if k.upper() in list(alphabet) else k for k in list(plaintext)]])

    def decode(self, ciphertext, order=-1):
        return self.encode(ciphertext, order=order)

class VignereCipher:
    def __init__(self, key='key'):
        self.key = key

    def __str__(self):
        return 'Vignere Cipher with Key: ' + self.key

    def encode(self, plaintext):
        return "".join([chr(((ord(plaintext[i]) + ord(("".join(list(self.key) + [self.key[i % len(self.key)] for i in range(len(plaintext) - len(self.key))]))[i])) % 26) + ord('A')) for i in range(len(plaintext))])

    def decode(self, ciphertext): 
        return "".join([chr((ord(ciphertext[i]) - ord(("".join(list(self.key) + [self.key[i % len(self.key)] for i in range(len(ciphertext) - len(self.key))]))[i] + 26) % 26) + ord('A')) for i in range(len(ciphertext))]) 