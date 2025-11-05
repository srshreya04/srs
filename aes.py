from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def aes_encrypt(plaintext, key_size):
    key = get_random_bytes(key_size // 8)  
    plaintext_bytes = plaintext.encode()
    
    while len(plaintext_bytes) % 16 != 0:
        plaintext_bytes += b' '
    
    cipher = AES.new(key, AES.MODE_CBC)  
    ciphertext = cipher.encrypt(plaintext_bytes)
    
    return {
        "key": b64encode(key).decode(),
        "iv": b64encode(cipher.iv).decode(),
        "ciphertext": b64encode(ciphertext).decode()
    }

def aes_decrypt(ciphertext_b64, key_b64, iv_b64):
    key = b64decode(key_b64)
    iv = b64decode(iv_b64)
    ciphertext = b64decode(ciphertext_b64)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext).decode().rstrip(' ')
    return decrypted

if __name__ == "__main__":
    print("=== AES Encryption / Decryption Program ===")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        plaintext = input("Enter plaintext message: ")
        
        while True:
            try:
                key_size = int(input("Choose key size (128 / 192 / 256): "))
                if key_size in [128, 192, 256]:
                    break
                else:
                    print("Invalid choice. Please enter 128, 192, or 256.")
            except ValueError:
                print("Please enter a valid number.")
        
        encrypted = aes_encrypt(plaintext, key_size)
        
        print("\n=== Encryption Successful ===")
        print(f"Key: {encrypted['key']}")
        print(f"IV: {encrypted['iv']}")
        print(f"Ciphertext: {encrypted['ciphertext']}\n")
    
    elif choice == '2':
        ciphertext_b64 = input("Enter ciphertext (base64): ")
        key_b64 = input("Enter key (base64): ")
        iv_b64 = input("Enter IV (base64): ")
        
        try:
            decrypted = aes_decrypt(ciphertext_b64, key_b64, iv_b64)
            print("\nDecrypted Text:", decrypted)
        except Exception as e:
            print("\nDecryption failed! Check your key, IV, or ciphertext.")
    
    else:
        print("Invalid choice. Please run the program again.")
