import v2
import random

message = input("Hello. Enter the message to be encrypted: ")
print("Plain Text : " + message)

ranum = random.randint(1, 26)
print("Shift pattern : " + str(ranum))

encrypted_msg = v2.caencrypt(message, ranum)
print("Encrypted: " + encrypted_msg)