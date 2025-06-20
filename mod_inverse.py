import random as rand

def mod_inverse(a, m):
    def extended_euclidean(a, b):
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r != 0:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
        return old_r, old_s, old_t

    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        return None  # No inverse exists
    else:
        return x % m  # Make sure the result is positive

a = rand.randrange(20,90)
m = rand.randrange(20,90)
inverse = mod_inverse(a, m)

if inverse is not None:
    print(f"The modular inverse of {a} modulo {m} is: {inverse}")
    print(f"Check: {a} * {inverse} % {m} = {(a * inverse) % m}")
else:
    print(f"{a} and {m} are not coprime, so no modular inverse exists.")
