def generate_rsa_keys(p, q, e):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def mod_inverse(a, m):
        def extended_euclidean(a, b):
            old_r, r = a, b
            old_s, s = 1, 0
            while r != 0:
                q = old_r // r
                old_r, r = r, old_r - q * r
                old_s, s = s, old_s - q * s
            return old_r, old_s
        gcd_val, x = extended_euclidean(a, m)
        return x % m if gcd_val == 1 else None

    n = p * q
    phi = (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        raise ValueError("e must be coprime with phi(n)")
    d = mod_inverse(e, phi)
    return (e, n), (d, n)
