from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.exceptions import InvalidSignature

# ---------- DSS/DSA Demo ----------
def dss_demo():
    print("=== Digital Signature Standard (DSA) Demo ===\n")
    
    # Step 1: Key Generation
    print("Step 1: Generating DSA keys...")
    private_key = dsa.generate_private_key(key_size=2048)  # Private key for signing
    public_key = private_key.public_key()  # Public key for verification
    print("Keys generated successfully.\n")
    
    # Step 2: Message Signing
    message = input("Enter the message to sign: ").encode()
    print("\nStep 2: Signing the message using private key...")
    signature = private_key.sign(message, hashes.SHA256())
    print("Message signed successfully!")
    print(f"Digital Signature (hex): {signature.hex()}\n")
    
    # Step 3: Signature Verification
    print("Step 3: Verifying the signature using public key...")
    try:
        public_key.verify(signature, message, hashes.SHA256())
        print("Signature is VALID. Message integrity and authenticity confirmed.\n")
    except InvalidSignature:
        print("Signature is INVALID! Message may have been tampered with.\n")
    
    # Step 4: Demonstrate security (tampering)
    print("Step 4: Demonstrating tampering detection...")
    tampered_message = message + b" "  # Small modification
    try:
        public_key.verify(signature, tampered_message, hashes.SHA256())
        print("Signature is VALID (unexpected).")
    except InvalidSignature:
        print("Tampered message detected! Signature verification failed.")
    
    tampered_signature = signature[:-1] + b'\x00'  # Modify the signature
    try:
        public_key.verify(tampered_signature, message, hashes.SHA256())
        print("Signature is VALID (unexpected).")
    except InvalidSignature:
        print("Tampered signature detected! Verification failed.")

if __name__ == "__main__":
    dss_demo()
