# Extended Euclidean Algorithm for Modular Inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def chinese_remainder(a, m):
    M = 1
    for modulus in m:
        M *= modulus

    result = 0
    for ai, mi in zip(a, m):
        Mi = M // mi
        yi = mod_inverse(Mi, mi)
        result += ai * Mi * yi

    return result % M

a = [2, 3, 2]       
m = [3, 5, 7]      
solution = chinese_remainder(a, m)
print(f"Solution of x ≡ {a} mod {m} is x = {solution}")
