import RSA_key as RSA
def rsa_encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)
# p, q, e = 61, 53, 17
# public_key, private_key = RSA.generate_rsa_keys(p, q, e)

# message = 42
# ciphertext = rsa_encrypt(message, public_key)
# decrypted = rsa_decrypt(ciphertext, private_key)

# print("Original message:", message)
# print("Encrypted (ciphertext):", ciphertext)
# print("Decrypted message:", decrypted)