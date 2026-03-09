import random
import numpy as np
from GenerateKey import generate_key_for_baseline, generate_key_for_enhancement, n

class LFSR_encryption:
    # n = 6
    def __init__(self, message, type):
        self.message = message
        self.type = type
        # self.seed = [1, 0, 1, 1, 0, 1]  # fixed seed for testing
        self.seed = [1] + [random.randint(0, 1) for _ in range(n - 1)] # ensure seed is not all 0s: default first bit is 1
        self.binary_message = ''.join(format(ord(char), '08b') for char in message)
        
    def encryption_message(self):
        print("seed:", self.seed)
        keystream = ''
        if self.type == "baseline":
            keystream = generate_key_for_baseline(self.seed, self.binary_message)
        else:
            keystream = generate_key_for_enhancement(self.seed, self.binary_message)
        if not keystream:
            print("Keystream generation failed.")
            return
        while len(keystream) < len(self.binary_message):
            keystream += keystream
        ciphertext = ''
        encrypted_message = ''
        for i in range(0, len(self.binary_message), 8):
            byte_msg = int(self.binary_message[i:i+8], 2)
            byte_key = int(keystream[i:i+8], 2)
            encrypted_byte = byte_msg ^ byte_key
            encrypted_message += format(encrypted_byte, '08b')
            ciphertext += chr(encrypted_byte)
        seed_char = chr(int(''.join(str(bit) for bit in self.seed), 2))
        text_to_save = seed_char + ciphertext
        if self.type == "baseline":
            with open(r"C:\Users\LTC\Desktop\FileProject\encryption_project2\encrypted_baseline.txt", "w", encoding="utf-8") as file:
                # file.write(''.join(str(bit) for bit in self.seed) + "\n")
                # file.write(str(ciphertext))
                file.write(str(text_to_save))
                file.close()
        else:
            with open(r"C:\Users\LTC\Desktop\FileProject\encryption_project2\encrypted_enhancement.txt", "w", encoding="utf-8") as file:
                file.write(str(text_to_save))
                file.close()
        print("ciphertext as binary:", encrypted_message)
        print("ciphertext:", ciphertext)
        print("seed + ciphertext:", text_to_save)
        print("Encryption complete. Encrypted message saved to file")
        return encrypted_message