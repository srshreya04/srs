import numpy as np

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def process_text(text):
    return "".join(ch.upper() for ch in text if ch.isalpha())

def letters_to_matrix(letters):
    """Convert space-separated letters into a numpy matrix of numbers (A=0,...,Z=25)"""
    letters = process_text(letters)
    values = [ord(ch) - 65 for ch in letters]
    return np.array(values).reshape(2, 2)

def hill_encrypt(plain_text, key_matrix):
    plain_text = process_text(plain_text)
    if len(plain_text) % 2 != 0:
        plain_text += "X"
    
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        pair = [ord(plain_text[i]) - 65, ord(plain_text[i+1]) - 65]
        result = np.dot(key_matrix, pair) % 26
        cipher_text += chr(result[0] + 65) + chr(result[1] + 65)
    return cipher_text

def hill_decrypt(cipher_text, key_matrix):
    cipher_text = process_text(cipher_text)
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        raise ValueError("Key matrix is not invertible modulo 26.")
    
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (det_inv * adjugate) % 26
    
    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        pair = [ord(cipher_text[i]) - 65, ord(cipher_text[i+1]) - 65]
        result = np.dot(inv_matrix, pair) % 26
        plain_text += chr(result[0] + 65) + chr(result[1] + 65)
    return plain_text

while True:
    print("\nChoose an option:")
    print("1. Encrypt (Hill Cipher)")
    print("2. Decrypt (Hill Cipher)")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        plain_text = input("Enter the plain text: ")
        print("Enter the 2x2 key matrix letters (row-wise, e.g., 'GY BN'):")
        key_letters = input()
        try:
            key_matrix = letters_to_matrix(key_letters)
            print("Encrypted Text:", hill_encrypt(plain_text, key_matrix))
        except Exception as e:
            print("Error in key matrix:", e)

    elif choice == '2':
        cipher_text = input("Enter the cipher text: ")
        print("Enter the 2x2 key matrix letters (row-wise):")
        key_letters = input()
        try:
            key_matrix = letters_to_matrix(key_letters)
            print("Decrypted Text:", hill_decrypt(cipher_text, key_matrix))
        except Exception as e:
            print("Error:", e)

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
