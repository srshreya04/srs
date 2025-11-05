from nltk.corpus import words

# Download once (comment after the first run)
# import nltk
# nltk.download('words')

english_words = set(words.words())

def caesar_cipher_encrypt(text, k):
    cipher_text = ""
    for char in text:
        if char.isupper():
            cipher_text += chr((ord(char) + k - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + k - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def caesar_decipher_decrypt(cipher_text, key):
    return caesar_cipher_encrypt(cipher_text, -key)

def is_meaningful(text):
    words_in_text = text.lower().split()
    count = sum(1 for word in words_in_text if word in english_words)
    return count >= 1 

def cryptanalysis(cipher_text):
    print("\nTrying all possible shifts:")
    found = False
    for key in range(1, 26):
        decrypted = caesar_decipher_decrypt(cipher_text, key)
        if is_meaningful(decrypted):
            print(f"Possible key = {key} -> {decrypted}")
            found = True
    if not found:
        print("No meaningful decryption found. Try different input or expand dictionary.")

while True:
    print("\nChoose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Cryptanalysis (Try to decode without key)")
    print("4. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        plain_text = input("Enter the plain text: ")
        key = int(input("Enter the shift key (number): "))
        print("Encrypted Text:", caesar_cipher_encrypt(plain_text, key))

    elif choice == '2':
        cipher_text = input("Enter the cipher text: ")
        key = int(input("Enter the shift key (number): "))
        print("Decrypted Text:", caesar_decipher_decrypt(cipher_text, key))

    elif choice == '3':
        cipher_text = input("Enter the cipher text: ")
        cryptanalysis(cipher_text)

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
