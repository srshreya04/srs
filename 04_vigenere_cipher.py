def process_text(text):
    """Keep only letters and convert to uppercase."""
    return "".join(ch.upper() for ch in text if ch.isalpha())

def vigenere_encrypt(plain_text, key):
    plain_text = process_text(plain_text)
    key = process_text(key)
    if not key:
        raise ValueError("Key must contain letters only.")
    
    cipher_text = ""
    for i, char in enumerate(plain_text):
        shift = ord(key[i % len(key)]) - 65
        cipher_text += chr(((ord(char) - 65 + shift) % 26) + 65)
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text = process_text(cipher_text)
    key = process_text(key)
    if not key:
        raise ValueError("Key must contain letters only.")
    
    plain_text = ""
    for i, char in enumerate(cipher_text):
        shift = ord(key[i % len(key)]) - 65
        plain_text += chr(((ord(char) - 65 - shift) % 26) + 65)
    return plain_text

while True:
    print("\nChoose an option:")
    print("1. Encrypt (Vigenère Cipher)")
    print("2. Decrypt (Vigenère Cipher)")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        plain_text = input("Enter the plain text: ")
        key = input("Enter the key (letters only): ")
        try:
            print("Encrypted Text:", vigenere_encrypt(plain_text, key))
        except ValueError as e:
            print("Error:", e)

    elif choice == '2':
        cipher_text = input("Enter the cipher text: ")
        key = input("Enter the key (letters only): ")
        try:
            print("Decrypted Text:", vigenere_decrypt(cipher_text, key))
        except ValueError as e:
            print("Error:", e)

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

def process_text(text):
    """Keep only letters and convert to uppercase."""
    return "".join(ch.upper() for ch in text if ch.isalpha())

def vigenere_encrypt(plain_text, key):
    plain_text = process_text(plain_text)
    key = process_text(key)
    if not key:
        raise ValueError("Key must contain letters only.")
    
    cipher_text = ""
    for i, char in enumerate(plain_text):
        shift = ord(key[i % len(key)]) - 65
        cipher_text += chr(((ord(char) - 65 + shift) % 26) + 65)
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text = process_text(cipher_text)
    key = process_text(key)
    if not key:
        raise ValueError("Key must contain letters only.")
    
    plain_text = ""
    for i, char in enumerate(cipher_text):
        shift = ord(key[i % len(key)]) - 65
        plain_text += chr(((ord(char) - 65 - shift) % 26) + 65)
    return plain_text

while True:
    print("\nChoose an option:")
    print("1. Encrypt (Vigenère Cipher)")
    print("2. Decrypt (Vigenère Cipher)")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        plain_text = input("Enter the plain text: ")
        key = input("Enter the key (letters only): ")
        try:
            print("Encrypted Text:", vigenere_encrypt(plain_text, key))
        except ValueError as e:
            print("Error:", e)

    elif choice == '2':
        cipher_text = input("Enter the cipher text: ")
        key = input("Enter the key (letters only): ")
        try:
            print("Decrypted Text:", vigenere_decrypt(cipher_text, key))
        except ValueError as e:
            print("Error:", e)

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
