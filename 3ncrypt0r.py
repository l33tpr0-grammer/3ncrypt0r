import base64
# Note to self: always remember to install PyCrypto
from Crypto.Cipher import XOR

# You must add your own PIN, you can't have mine!
PIN = input("Your 4 number PIN please: ")

# ToDo: Remove before release
PIN = "1337"
secret = input("Your data to be securely encrypted: ")


def encrypt(key, plaintext):
  cipher = XOR.new(key)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
  cipher = XOR.new(key)
  return cipher.decrypt(base64.b64decode(ciphertext))

print("Here's your secret, encrypted, uncrackable data:")
print(encrypt(PIN,secret))

# ToDo:
# Add inputs to the decrypt field too.
