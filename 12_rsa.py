import random
from math import gcd

def is_prime(n, k=5):
    """Check if n is prime using Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bits=1024):
    """Generate a random prime number of specified bit length."""
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  
        if is_prime(num):
            return num

def modinv(a, m):
    """Compute modular inverse using Extended Euclidean Algorithm."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def extended_gcd(a, b):
    """Extended Euclidean Algorithm."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

class RSA:
    def __init__(self, bits=1024):
        self.bits = bits
        self.p = generate_large_prime(bits // 2)
        self.q = generate_large_prime(bits // 2)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.choose_e(self.phi)
        self.d = modinv(self.e, self.phi)

    def choose_e(self, phi):
        """Choose e coprime with phi(n)."""
        e = 65537  
        if gcd(e, phi) == 1:
            return e
        for e in range(3, phi, 2):
            if gcd(e, phi) == 1:
                return e

    def encrypt(self, plaintext):
        """Encrypt a message (string) into a list of integers."""
        return [pow(ord(char), self.e, self.n) for char in plaintext]

    def decrypt(self, ciphertext):
        """Decrypt a list of integers back to a string."""
        return ''.join([chr(pow(char, self.d, self.n)) for char in ciphertext])

if __name__ == "__main__":
    rsa = RSA(bits=16)  
    print("Public Key: (n={}, e={})".format(rsa.n, rsa.e))
    print("Private Key: (n={}, d={})".format(rsa.n, rsa.d))

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter message to encrypt: ")
            encrypted = rsa.encrypt(message)
            print("Encrypted Message:", encrypted)

        elif choice == '2':
            cipher_input = input("Enter ciphertext numbers separated by space: ")
            try:
                ciphertext = [int(x) for x in cipher_input.strip().split()]
                decrypted = rsa.decrypt(ciphertext)
                print("Decrypted Message:", decrypted)
            except ValueError:
                print("Invalid input! Enter integers separated by space.")

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
