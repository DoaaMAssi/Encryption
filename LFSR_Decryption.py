import math
import numpy as np
from GenerateKey import generate_key_for_baseline, generate_key_for_enhancement, n

class LFSR_decryption:
    def __init__(self, seed, ciphertext, type):
        seed_bin = format(ord(seed), '08b')
        self.seed = [int(b) for b in seed_bin[-n:]] 
        print("Seed is binary:", self.seed)
        self.ciphertext = ciphertext
        self.type = type   
        self.binary_message = ''.join(format(ord(char), '08b') for char in ciphertext)

    def decryption_message(self):
        plaintext = ''
        if self.type == "baseline":
            keystream = generate_key_for_baseline(self.seed, self.binary_message)
        else:
            keystream = generate_key_for_enhancement(self.seed, self.binary_message)
        for i in range(0, len(self.binary_message), 8):
            byte_key = int(keystream[i:i+8], 2)
            byte_cipher = int(self.binary_message[i:i+8], 2)
            decrypted_byte = byte_cipher ^ byte_key
            plaintext += chr(decrypted_byte)
        return plaintext