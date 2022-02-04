import base64
# Note to self: always remember to install PyCrypto
from Crypto.Cipher import XOR

def encrypt(key, plaintext):
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(ciphertext))

ask = input("Do you want to decrypt or encrypt?: ")
PIN = input("Your 4 number PIN please: ")
if ask.lower() == "encrypt":
    secret = input("Your data to be securely encrypted: ")
    
    print("Here's your secret, encrypted, uncrackable data:")
    print(encrypt(PIN,secret))
    
elif ask.lower() == "decrypt":
    secret = input("Your secret data to be decrypted: ")
    
    print("Here's your decrypted data:")
    print(decrypt(PIN,secret))

else:
    print("Invalid option specified! Please try again.")
