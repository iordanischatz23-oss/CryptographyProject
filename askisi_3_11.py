import numpy as np

encoded_map = {
    "A": "00000",
    "B": "00001",
    "C": "00010",
    "D": "00011",
    "E": "00100",
    "F": "00101",
    "G": "00110",
    "H": "00111",
    "I": "01000",
    "J": "01001",
    "K": "01010",
    "L": "01011",
    "M": "01100",
    "N": "01101",
    "O": "01110",
    "P": "01111",
    "Q": "10000",
    "R": "10001",
    "S": "10010",
    "T": "10011",
    "U": "10100",
    "V": "10101",
    "W": "10110",
    "X": "10111",
    "Y": "11000",
    "Z": "11001",
    ".": "11010",
    "!": "11011",
    "?": "11100",
    "(": "11101",
    ")": "11110",
    "-": "11111"
}

decoded_map = {v: k for k, v in encoded_map.items()}

def permutation_S(user_seed):
    seed_encoded = encode(user_seed)
    enc_seed = [int(x, 2) for x in seed_encoded]
    S = []
    for i in range(256):#cause stops one number before 256
        S.append(i)
    j = 0
    for i in range(256):
        j = (j + S[i] + enc_seed[i % len(enc_seed)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def generate_keystream(length, S):
    i = 0
    j = 0
    keystream = []
    length = length * 5
    while length > 0:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        byte = format((S[(S[i] + S[j]) % 256]), "08b")
        keystream.extend(int(b) for b in byte)
        length -= 8
    return keystream

def encode(mess):
    encoded_mess = []
    for char in mess:
        num = encoded_map[char]
        encoded_mess.append(num)
    return encoded_mess

def decode_message(list_of_chunks):
    decoded_chars = []
    for bits in list_of_chunks:
        letter = decoded_map[bits] 
        decoded_chars.append(letter)      
    return "".join(decoded_chars)

def RC4_encrypt_decrypt(encoded_message, seed):
    ciphertext = []
    S = permutation_S(seed)
    key = generate_keystream(len(encoded_message), S)
    for i in range(len(encoded_message)):
        key_bits = "".join(str(b) for b in key[i*5 : i*5+5])#Join the 5 bits of the key to form a 5-bit string 
        ciphertext.append(format(int(encoded_message[i], 2) ^ int(key_bits, 2), "05b")) #XOR the 5-bit string of the message with the 5-bit string of the key and append the result to the ciphertext list as a 5-bit binary string
    return ciphertext




if __name__ == "__main__":
    plaintext = "MISTAKESAREASSERIOUSASTHERESULTSTHEYCAUSE"
    seed_string = "HOUSE"
    encoded_plaintext = encode(plaintext)
    ciphertext = RC4_encrypt_decrypt(encoded_plaintext, seed_string)
    print(decode_message(ciphertext))
    ciphertext_taken = "!CIJ(TYRZ(CWTDMOP.ZY!JPRTKBMN!CQAK.B!B?IH"
    encoded_ciphertext_taken = encode(ciphertext_taken)
    decoded_ciphertext_taken = RC4_encrypt_decrypt(encoded_ciphertext_taken, seed_string)
    print(decode_message(decoded_ciphertext_taken))
    