def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  
    else:
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y

def mod_inverse(a, m):
    gcd_val, x, y = extended_gcd(a, m)
    if gcd_val != 1:
        return None  
    else:
        return x % m

a = 30
b = 20
print("GCD of", a, "and", b, "=", gcd(a, b))

g, x, y = extended_gcd(a, b)
print(f"Extended GCD: gcd({a},{b}) = {g}, x = {x}, y = {y}")
print(f"Verification: {a}*{x} + {b}*{y} = {a*x + b*y}")

m = 7
num = 3
inv = mod_inverse(num, m)
if inv:
    print(f"Modular Inverse of {num} mod {m} = {inv}")
else:
    print(f"No modular inverse exists for {num} mod {m}")
