import numpy as np
import random
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

def random_key_producer(p):
    key = ""
    for i in range(p):
        # randint function to generate 0, 1 randomly and converting 
        temp = str(random.randint(0, 1))
        key += temp     
    return(key)

def encode_message(encoded_message):
    for letter,bits in encoded_map.items():
        encoded_message = encoded_message.replace(letter,bits)
    return encoded_message,len(encoded_message)

def decode_message(encoded_message):
    for letter,bits in decoded_map.items():
        decoded_message = encoded_message.replace(bits,letter)
    return decoded_message

def encrypt_message(encoded_message,key):
    ciphertext = int(encoded_message, 2) ^ int(key, 2)
    return bin(ciphertext)[2:].zfill(len(encoded_message))

def decrypt_message(ciphertext,key):
    decrypted_message = int(ciphertext, 2) ^ int(key, 2)
    return bin(decrypted_message)[2:].zfill(len(ciphertext))
 
def decode_binary_message(binary_message):
    original_text = ""
    for i in range(0, len(binary_message), 5):
        chunk = binary_message[i:i+5]  # 5 bits at a time
        letter = decoded_map[chunk]    # Maps the correspoding letter to the chunk
        original_text += letter        
    return original_text

if __name__ == "__main__":
    encoded_message = input("Enter the message: ")
    encoded_message, length = encode_message(encoded_message)
    key = random_key_producer(length)
    ciphertext = encrypt_message(encoded_message, key)
    plaintext = decrypt_message(ciphertext, key)

    print("ciphertext in binary =")
    print(ciphertext)
    print("Ciphertext in string =")
    print(decode_binary_message(ciphertext))
    print("plaintext in binary =")
    print(plaintext)
    print("Original message =")
    print(decode_binary_message(plaintext))
