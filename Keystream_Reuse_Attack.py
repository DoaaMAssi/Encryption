from LFSR_Encryption import LFSR_encryption

plainText_1 = "HELLO"
plainText_2 = "WORLD"
print("Plaintext 1:", plainText_1)
print("Plaintext 2:", plainText_2)

print("\n\n------------Baseline key-stream reuse attack--------------------\n")

baseline_ciphertext_1 = LFSR_encryption(plainText_1, "baseline").encryption_message()
baseline_ciphertext_2 = LFSR_encryption(plainText_2, "baseline").encryption_message()
print("Baseline Ciphertext 1 (binary):", baseline_ciphertext_1)
print("Baseline Ciphertext 2 (binary):", baseline_ciphertext_2)

baseline_X = int(baseline_ciphertext_1, 2) ^ int(baseline_ciphertext_2, 2)
print("Baseline XOR of two ciphertexts:", bin(baseline_X))


print("\n\n------------Enhancement key-stream reuse attack--------------------\n")

enhancement_ciphertext_1 = LFSR_encryption(plainText_1, "enhancement").encryption_message()
enhancement_ciphertext_2 = LFSR_encryption(plainText_2, "enhancement").encryption_message()
print("Enhancement Ciphertext 1 (binary):", enhancement_ciphertext_1)
print("Enhancement Ciphertext 2 (binary):", enhancement_ciphertext_2)

enhancement_X = int(enhancement_ciphertext_1, 2) ^ int(enhancement_ciphertext_2, 2)
print("Enhancement XOR of two ciphertexts:", bin(enhancement_X))