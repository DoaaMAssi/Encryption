from LFSR_Encryption import LFSR_encryption

plainText_1 = "HELLO"
plainText_2 = "WORLD"
print("Plaintext 1:", plainText_1)
print("Plaintext 2:", plainText_2)

# attacking is known part of plaintext and chiphertext 
print("\n\n------------Baseline known plaintext attack--------------------\n")
plainText_1_known = "HE"
plainText_1_known_binary = ''.join(format(ord(char), '08b') for char in plainText_1_known)
baseline_ciphertext_1 = LFSR_encryption(plainText_1, "baseline").encryption_message()
cipher_known_part = baseline_ciphertext_1[:len(plainText_1_known_binary)]
keystream_part = int(plainText_1_known_binary, 2) ^ int(cipher_known_part, 2)
print("Baseline known part keystream (binary):", bin(keystream_part))

baseline_ciphertext_2 = LFSR_encryption(plainText_2, "baseline").encryption_message()
cipher_part = baseline_ciphertext_2[:len(plainText_1_known_binary)]
keystream_bits = bin(keystream_part)[2:].zfill(len(cipher_known_part))
plain_part = ""
for i in range(0, len(cipher_part), 8):
    byte_msg = int(cipher_part[i:i+8], 2)
    byte_key = int(keystream_bits[i:i+8], 2)
    decrypted_byte = byte_msg ^ byte_key
    plain_part += chr(decrypted_byte)

print("plain_part as ASCII:", plain_part)

print("\n\n------------Enhancement known plaintext attack--------------------\n")
enhancement_ciphertext_1 = LFSR_encryption(plainText_1, "enhancement").encryption_message()
plainText_1_knownenhancement = "HE"
plainText_1_known_binaryenhancement = ''.join(format(ord(char), '08b') for char in plainText_1_knownenhancement)
cipher_known_part = enhancement_ciphertext_1[:len(plainText_1_known_binaryenhancement)]
keystream_part_enhancement = int(plainText_1_known_binaryenhancement, 2) ^ int(cipher_known_part, 2)
print("Enhancement known part keystream (binary):", bin(keystream_part_enhancement))

enhancement_ciphertext_2 = LFSR_encryption(plainText_2, "enhancement").encryption_message()
cipher_part = enhancement_ciphertext_2[:len(plainText_1_known_binaryenhancement)]
keystream_bits = bin(keystream_part_enhancement)[2:].zfill(len(cipher_known_part))
plain_partenhancement = ""
for i in range(0, len(cipher_part), 8):
    byte_msg = int(cipher_part[i:i+8], 2)
    byte_key = int(keystream_bits[i:i+8], 2)
    decrypted_byte = byte_msg ^ byte_key
    plain_partenhancement += chr(decrypted_byte)
print("plain_partenhancement as ASCII:", plain_partenhancement)