import random

def is_prime(n):
    """Check if a number is prime (simple method for demonstration)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_primitive_root(p):
    """Find a primitive root modulo p."""
    required_set = set(num for num in range(1, p))
    for g in range(2, p):
        actual_set = set(pow(g, powers, p) for powers in range(1, p))
        if actual_set == required_set:
            return g
    return None

def diffie_hellman_demo():
    print("=== Diffie-Hellman Key Exchange Demo ===\n")
    
    p = int(input("Enter a prime number (p): "))
    while not is_prime(p):
        p = int(input("Number is not prime. Enter a prime number (p): "))
    
    g = find_primitive_root(p)
    print(f"Primitive root modulo {p} automatically found: g = {g}\n")
    
    a = random.randint(1, p-2)  
    b = random.randint(1, p-2)  
    print(f"Alice's private key (a) is kept secret.")
    print(f"Bob's private key (b) is kept secret.\n")
    
    A = pow(g, a, p)  
    B = pow(g, b, p)  
    print(f"Alice's public key (A) = g^a mod p = {A}")
    print(f"Bob's public key (B) = g^b mod p = {B}\n")
    
    K_Alice = pow(B, a, p)
    K_Bob = pow(A, b, p)
    
    print(f"Alice computes shared key K = B^a mod p = {K_Alice}")
    print(f"Bob computes shared key K = A^b mod p = {K_Bob}\n")

    if K_Alice == K_Bob:
        print("Success! Shared secret key established.")
    else:
        print("Error! Keys do not match.")
    
    print("\nSimulating attacker (Eve) trying to compute the shared key without private keys...")
    print("Eve cannot compute the shared key without solving the discrete logarithm problem.")
    print("Therefore, the shared secret key remains secure.")

if __name__ == "__main__":
    diffie_hellman_demo()
