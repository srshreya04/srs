def process_text(text):
    """Keep only letters and convert to uppercase."""
    return "".join(ch.upper() for ch in text if ch.isalpha())

def rail_fence_encrypt(plain_text, rails):
    plain_text = process_text(plain_text)
    if rails <= 1:
        return plain_text

    rail_matrix = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]

    direction_down = False
    row, col = 0, 0

    for ch in plain_text:
        rail_matrix[row][col] = ch
        col += 1

        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    cipher_text = ""
    for i in range(rails):
        for j in range(len(plain_text)):
            if rail_matrix[i][j] != '\n':
                cipher_text += rail_matrix[i][j]
    return cipher_text

def rail_fence_decrypt(cipher_text, rails):
    cipher_text = process_text(cipher_text)
    if rails <= 1:
        return cipher_text

    rail_matrix = [['\n' for _ in range(len(cipher_text))] for _ in range(rails)]
    
    direction_down = None
    row, col = 0, 0

    for _ in cipher_text:
        rail_matrix[row][col] = '*'
        col += 1

        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False
        row += 1 if direction_down else -1

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if rail_matrix[i][j] == '*' and index < len(cipher_text):
                rail_matrix[i][j] = cipher_text[index]
                index += 1

    result = ""
    row, col = 0, 0
    for _ in cipher_text:
        result += rail_matrix[row][col]
        col += 1

        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False
        row += 1 if direction_down else -1

    return result

while True:
    print("\nChoose an option:")
    print("1. Encrypt (Rail Fence Cipher)")
    print("2. Decrypt (Rail Fence Cipher)")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        plain_text = input("Enter the plain text: ")
        rails = int(input("Enter number of rails: "))
        print("Encrypted Text:", rail_fence_encrypt(plain_text, rails))

    elif choice == '2':
        cipher_text = input("Enter the cipher text: ")
        rails = int(input("Enter number of rails: "))
        print("Decrypted Text:", rail_fence_decrypt(cipher_text, rails))

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
