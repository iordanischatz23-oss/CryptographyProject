import numpy as np
from sympy import GF
from sympy.polys.matrices import DomainMatrix

A = np.zeros((16, 16), dtype=int)

A[0] = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0] #for c1
A[1] = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0] #for c2
A[2] = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] #for c3
A[3] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0] #for c4
A[4] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0] #for c5
A[5] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1] #for c6
A[6] = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0] #for c7
A[7] = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0] #for c8
A[8] = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] #for c9
A[9] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1] #for c10
A[10] = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0] #for c11
A[11] = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] #for c12
A[12] = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0] #for c13
A[13] = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0] #for c14
A[14] = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] #for c15
A[15] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1] #for c16

def get_binary_inverse(matrix):
    l = len(matrix)
    FF = GF(2)
    Alpha = DomainMatrix([[FF(_) for _ in row] for row in matrix], (l, l), FF)
    inv_matrix = Alpha.inv().to_list()
    for i in range(l):
        for j in range(l):
            inv_matrix[i][j] = int(inv_matrix[i][j])
    return np.array(inv_matrix)



#Get the input from the user
message_bits = input("Enter a 16-bit sequence: ")
message_bits = message_bits.strip()

#Check if the length is correct
if len(message_bits) != 16:
    print("Error: You must enter exactly 16 numbers.")
    exit()

#Create an empty list to hold the numbers
bit_list = []

for char in message_bits:
    # Check if the character is a 0 or 1
    if char == "0" or char == "1":
        number = int(char)
        bit_list.append(number)
    else:
        print("Error: Only 0 and 1 are allowed!")
        exit()

# Turn the list into a NumPy column vector
message = np.array(bit_list)
#Make the column vector
message = message.reshape(16, 1)

print("message column vector =")
print(message.flatten())

cipher = np.mod(A @ message, 2)
print("cipher = A * message")
print(cipher.flatten())


print("A^(-1) =")
print(get_binary_inverse(A))
print("plaintext = A^(-1) * cipher")
plaintext = np.mod(get_binary_inverse(A) @ cipher, 2)

original_message = plaintext.flatten()
print(original_message)
assert np.array_equal(original_message, message.flatten()), "Decryption failed"
print("Decryption successful: plaintext matches original message.")
