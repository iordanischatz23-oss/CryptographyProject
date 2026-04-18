from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def count_bit_differences(bytes1, bytes2):
    diff = [b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)]
    return sum(d.bit_count() for d in diff)

for _ in range(60):
    key = get_random_bytes(16) # 128 bits
    iv = get_random_bytes(16)  #iv state for CBC

    m1 = get_random_bytes(32) # 256 bits
    m2 = bytearray(m1)
    m2[0] ^= 1 #change the first bit of the first block

    cipher_ecb = AES.new(key, AES.MODE_ECB)
    ciphertext1_ecb = cipher_ecb.encrypt(m1)
    ciphertext2_ecb = cipher_ecb.encrypt(m2)

    cipher_CBC = AES.new(key, AES.MODE_CBC, iv)
    ciphertext1_cbc = cipher_CBC.encrypt(m1)
    #Create a new cipher for the second encryption to reset the IV state
    cipher_CBC2 = AES.new(key, AES.MODE_CBC, iv)
    ciphertext2_cbc = cipher_CBC2.encrypt(m2)



    print(f"Differences in ECB for iteration: {count_bit_differences(ciphertext1_ecb, ciphertext2_ecb)} bits")
    print(f"Differences in CBC for iteration: {count_bit_differences(ciphertext1_cbc, ciphertext2_cbc)} bits")