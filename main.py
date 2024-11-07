import re
from hashlib import pbkdf2_hmac


email = input("Enter email address: \n")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        return "Valid Email"
    else:
        return "Invalid Email Address"


password = input("Enter master password: \n")


iterations = 7000

new_iterations = 1000
salt = bytes.fromhex('f30dd5755d4d172d')
passwordtohash = email+password
vault_key = pbkdf2_hmac('sha1',bytes(passwordtohash,'utf-8'), salt, iterations, dklen=64)
# print(f"pbkdf2:{iterations}:{salt.hex()}:{hash.hex()}")


print(f"{vault_key.hex()}")

print(type(vault_key))
decoded_string = str(vault_key.hex())

auth_key_hash = decoded_string + password
auth_key = pbkdf2_hmac('sha1',bytes(auth_key_hash,'utf-8'),salt, new_iterations, dklen=128,)

print(f"{auth_key.hex()}")






