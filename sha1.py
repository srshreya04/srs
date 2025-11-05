import hashlib

def sha1_demo():
    print("=== SHA-1 Hash Demonstration ===\n")
    
    message = input("Enter a message: ")
    
    sha1_hash = hashlib.sha1(message.encode()).hexdigest()
    
    print(f"\nSHA-1 Digest (hexadecimal): {sha1_hash}")
    
    modified_message = message + " "  
    modified_hash = hashlib.sha1(modified_message.encode()).hexdigest()
    
    print("\nAfter a small change in the message:")
    print(f"Modified Message: '{modified_message}'")
    print(f"SHA-1 Digest (hexadecimal): {modified_hash}")
    
    print("\nNotice how even a tiny change produces a completely different hash.")
    
    
if __name__ == "__main__":
    sha1_demo()
