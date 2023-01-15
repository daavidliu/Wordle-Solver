import v2
import random

message = input("This is a Caesar Cipher program. The key shift will be random.\nPlease enter the message to be encrypted: ")

ranum = random.randint(1, 26)
print("Shift pattern : " + str(ranum))

encrypted_msg = v2.caencrypt(message, ranum)
print("THE ENCRYPTED MESSAGE:")
print(encrypted_msg)