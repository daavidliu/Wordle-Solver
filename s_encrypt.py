import v3

message = input("This is a substitution cipher program. The substituions will be random.\nEnter the message to be encrypted: ")

encrypted_msg = v3.sub_encrypt(message)
print("THE ENCRYPTED MESSAGE:")
print(encrypted_msg)