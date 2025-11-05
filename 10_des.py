from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

def pkcs5_pad(data: bytes, block_size: int = 8) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len]) * pad_len

def pkcs5_unpad(data: bytes) -> bytes:
    if not data:
        raise ValueError("Empty input to unpad")
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 8:
        raise ValueError("Invalid padding")
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("Invalid padding bytes")
    return data[:-pad_len]

def parse_key(key_str: str) -> bytes:

    key_str = key_str.strip()
    if all(c in "0123456789abcdefABCDEF" for c in key_str) and len(key_str) == 16:
        return binascii.unhexlify(key_str)
    if len(key_str.encode('utf-8')) == 8:
        return key_str.encode('utf-8')
    raise ValueError("Key must be either 16 hex chars or exactly 8 ASCII characters (8 bytes).")

def encrypt_des_cbc(plaintext: bytes, key: bytes) -> tuple[bytes, bytes]:
    iv = get_random_bytes(8)  
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded = pkcs5_pad(plaintext, 8)
    ct = cipher.encrypt(padded)
    return iv, ct

def decrypt_des_cbc(iv: bytes, ciphertext: bytes, key: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_CBC, iv)
    pt_padded = cipher.decrypt(ciphertext)
    return pkcs5_unpad(pt_padded)

def main():
    print("DES")
    plaintext = input("Enter plaintext: ")
    key_input = input("Enter 64-bit key (16 hex digits OR 8 ASCII chars): ")

    try:
        key = parse_key(key_input)
    except ValueError as e:
        print("Key error:", e)
        return

    pt_bytes = plaintext.encode('utf-8')

    iv, ciphertext = encrypt_des_cbc(pt_bytes, key)
    print("\n--- Encryption result ---")
    print("Initialization Vector (hex):", binascii.hexlify(iv).decode())
    print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())

    recovered = decrypt_des_cbc(iv, ciphertext, key)
    print("\n--- Decryption ---")
    try:
        print("Recovered plaintext:", recovered.decode('utf-8'))
    except UnicodeDecodeError:
        print("Recovered plaintext (raw bytes):", recovered)

    if recovered == pt_bytes:
        print("\nVerified: Decrypted plaintext matches the original.")
    else:
        print("\nVerification FAILED — mismatch.")

if __name__ == "__main__":
    main()
