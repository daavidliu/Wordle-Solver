import v3

message = input("This program will assist you in decrypting a Substitution cipher.\nPlease enter the message to be decrypted:\n")
v3.initialise_key()
v3.text_analysis(message)

while True:
    v3.update_key()
    output = v3.update_decrypt(message)
    v3.text_analysis(output)
