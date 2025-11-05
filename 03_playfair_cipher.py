def generate_key_square(key):
    key = key.upper().replace("J", "I") 
    seen = set()
    square = []
    
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen and char.isalpha():
            seen.add(char)
            square.append(char)
    return [square[i*5:(i+1)*5] for i in range(5)] 

def find_position(square, letter):
    for r, row in enumerate(square):
        for c, col in enumerate(row):
            if col == letter:
                return r, c
    return None

def encrypt(text, key):
    square = generate_key_square(key)
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = ""
        if i + 1 < len(text):
            b = text[i+1]
            if a == b:
                b = "X"
                i += 1
            else:
                i += 2
        else:
            b = "X"
            i += 1
        digraphs.append(a + b)

    cipher_text = ""
    for a, b in digraphs:
        r1, c1 = find_position(square, a)
        r2, c2 = find_position(square, b)
        if r1 == r2:  
            cipher_text += square[r1][(c1 + 1) % 5]
            cipher_text += square[r2][(c2 + 1) % 5]
        elif c1 == c2:  
            cipher_text += square[(r1 + 1) % 5][c1]
            cipher_text += square[(r2 + 1) % 5][c2]
        else:  
            cipher_text += square[r1][c2]
            cipher_text += square[r2][c1]
    return cipher_text

def decrypt(cipher_text, key):
    square = generate_key_square(key)
    cipher_text = cipher_text.upper().replace("J", "I")
    cipher_text = "".join(ch for ch in cipher_text if ch.isalpha())

    digraphs = [cipher_text[i:i+2] for i in range(0, len(cipher_text), 2)]

    plain_text = ""
    for a, b in digraphs:
        r1, c1 = find_position(square, a)
        r2, c2 = find_position(square, b)
        if r1 == r2:  
            plain_text += square[r1][(c1 - 1) % 5]
            plain_text += square[r2][(c2 - 1) % 5]
        elif c1 == c2:  
            plain_text += square[(r1 - 1) % 5][c1]
            plain_text += square[(r2 - 1) % 5][c2]
        else: 
            plain_text += square[r1][c2]
            plain_text += square[r2][c1]
    return plain_text

while True:
    print("\nChoose an option:")
    print("1. Encrypt (Playfair)")
    print("2. Decrypt (Playfair)")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        plain_text = input("Enter the plain text: ")
        key = input("Enter the Playfair key (word/phrase): ")
        print("Encrypted Text:", encrypt(plain_text, key))

    elif choice == '2':
        cipher_text = input("Enter the cipher text: ")
        key = input("Enter the Playfair key (word/phrase): ")
        print("Decrypted Text:", decrypt(cipher_text, key))

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
