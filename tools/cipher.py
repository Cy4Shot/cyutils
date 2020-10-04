class CeasarCipher:
    def __init__(self, shift):
        self.shift = shift

    def __str__(self):
        return "Ceasar Cipher with shift: " + str(self.shift)
    
    @staticmethod
    def sysencode(text, shift):
        return "".join([chr((ord(text[i]) + shift - 65) % 26 + 65) if text[i].upper() == text[i] else chr((ord(text[i]) + shift - 97) % 26 + 97) for i in range(len(text))])

    def encode(self, plaintext):
        return self.sysencode(plaintext, self.shift)

    def decode(self, ciphertext):
        return self.sysencode(ciphertext, 26 - self.shift)

class VignereCipher:
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return "Vignere Cipher with key: " + str(self.key)

    def encode(self, plaintext): 
        return("".join([chr(((ord(plaintext[i]) + ord(([self.key[i] if i < len(self.key) else self.key[i % len(self.key)] for i in range(len(plaintext))])[i])) % 26) + ord('A')) for i in range(len(plaintext))]))

    def decode(self, ciphertext):
        return("".join([chr(((ord(ciphertext[i]) - ord(([self.key[i] if i < len(self.key) else self.key[i % len(self.key)] for i in range(len(ciphertext))])[i]) + 26) % 26) + ord('A')) for i in range(len(ciphertext))])) 
