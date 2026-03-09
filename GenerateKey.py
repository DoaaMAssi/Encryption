from random import seed


n = 6

def generate_key_for_baseline(seed, binary_message):
    listKey = []
    key = [str(bit) for bit in seed.copy()] # b6, b5, b4, b3, b2, b1 => key[0], key[1], key[2], key[3], key[4], key[5]
    keystream = ''.join(key)
    listKey.append(''.join(key))
    # rounds = 0
    for _ in range((pow(2, n))-1):
        # rounds += 1
        b1 = key[5]
        b6 = key[0]
        # Shift bits to the right
        for i in range(n-1, 0, -1):
            key[i] = key[i-1]
        key[0] = str(int(b6) ^ int(b1)) # b6 = b1 xor b6 
        # if  ''.join(key) in listKey:
        #     # print("Baseline keystream generation rounds:", rounds)
        #     break
        keystream += ''.join(key)
        listKey.append(''.join(key))
        if len(keystream) >= len(binary_message):
            break
    return keystream

def generate_key_for_enhancement(seed, binary_message):
    # rounds = 0
    filtering = []
    listKey = []
    key = [str(bit) for bit in seed.copy()] # b6, b5, b4, b3, b2, b1 => key[0], key[1], key[2], key[3], key[4], key[5]
    keystream = ''.join(key)
    listKey.append(''.join(key))
    for _ in range((pow(2, n))-1):
        # rounds += 1
        f1 = int(key[4]) &  int(key[2]) | int(key[5]) # b2 and b4 or b1
        f2 = int(key[3]) & int(key[1]) | int(key[4]) # b3 and b5 or b2
        f3 = int(key[2]) & int(key[0]) | int(key[3]) # b4 and b6 or b3
        f4 = f3 ^ f2 ^ f1
        new_filter = str(f4) + str(f3) + str(f2) + str(f1)
        filtering.append(new_filter)
        b1 = key[5]
        b6 = key[0]
        b2 = key[4]
        b3 = key[3]
        b4 = key[2]
        b5 = key[1]
        # Shift bits to the right
        for i in range(n-1, 0, -1):
            key[i] = key[i-1]
        # b6 = b1 xor b6 xor (b4 and b3) xor ((b5 or b2) and (b6 or b1))
        new_bit = (int(b6) ^ int(b1)) ^ (int(b4) & int(b3)) ^ ((int(b5) | int(b2)) & (int(b6) | int(b1)))
        key[0] = str(new_bit)
        # if  ''.join(key) in listKey:
        #     # print("Enhancement keystream generation rounds:", rounds)
        #     break
        listKey.append(''.join(key))
    for i in range(len(filtering)):
        f1 = filtering[i]
        f2 = filtering[(i+1) % len(filtering)]
        c1 = int(f1[0]) ^ int(f2[0])
        c2 = int(f1[1]) ^ int(f2[1])
        c3 = int(f1[2]) ^ int(f2[2])
        c4 = int(f1[3]) ^ int(f2[3])
        c5 = int(f1[0]) ^ int(f2[2])
        c6 = int(f1[1]) ^ int(f2[3])
        combined = str(c1) + str(c2) + str(c3) + str(c4) + str(c5) + str(c6)
        keystream += combined
        if len(keystream) >= len(binary_message):
            break
    return keystream

# def count_bits(keystream):
#     zeros = keystream.count("0")
#     ones = keystream.count("1")
#     print("Keystream:", keystream)
#     print("Number of 0s:", zeros)
#     print("Number of 1s:", ones)
#     print("----------------------------\n")
#     return zeros, ones

# seed1 = [1, 0, 1, 1, 0, 1]  
# binary_message = '101100111000' 
# key_baseline = generate_key_for_baseline(seed1, binary_message)
# key_enhancement = generate_key_for_enhancement(seed1, binary_message)
# count_bits(key_baseline)
# count_bits(key_enhancement)

# print("\n\n----------------------------\n\n")
# seed2 = [1, 1, 1, 1, 0, 1]  
# key_baseline2 = generate_key_for_baseline(seed2, binary_message)
# key_enhancement2 = generate_key_for_enhancement(seed2, binary_message) 
# count_bits(key_baseline2)
# count_bits(key_enhancement2)

# print("\n\nAvalanche Effect:\n")
# key1 = "".join(str(int(b1) ^ int(b2)) for b1, b2 in zip(key_baseline, key_baseline2))
# key2 = "".join(str(int(b1) ^ int(b2)) for b1, b2 in zip(key_enhancement, key_enhancement2))
# count_bits(key1)
# count_bits(key2)