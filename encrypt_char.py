import encrypt_decrypt_rsa as ed_rsa
import RSA_key as RSA

def encrypt_text(text, public_key):
    encrypted = []
    for char in text:
        m = ord(char)
        c = ed_rsa.rsa_encrypt(m, public_key)
        encrypted.append(c)
    return encrypted

def decrypt_text(cipher_list, private_key):
    decrypted = ""
    for c in cipher_list:
        m = ed_rsa.rsa_decrypt(c, private_key)
        decrypted += chr(m)
    return decrypted

# Example keys
public_key, private_key = RSA.generate_rsa_keys(61, 53, 17)

# Encrypt and decrypt a string
message = "Hi!"
ciphertext = encrypt_text(message, public_key)
decrypted = decrypt_text(ciphertext, private_key)

print("Original text:", message)
print("Encrypted:", end=' ')
for c in ciphertext:
    print(f"{c}", end='')
print()
print("Decrypted:", decrypted)
