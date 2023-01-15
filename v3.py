import random
import json
import operator

LETTERS_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def makeSubKey(alphabet):
    alph_list = list(alphabet)
    random.shuffle(alph_list)
    return alph_list

def sub_encrypt(text):
    key_upper = makeSubKey(LETTERS_UPPER)
    
    key_dict = {}
    i = 0
    for letter in LETTERS_UPPER:
        key_dict[letter] = key_upper[i]
        i += 1   
        
    with open("key.json", "w") as outfile:
        json.dump(key_dict, outfile)
        
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt characters in plain text
        if (char.isupper()):
            result += key_dict[char]
        elif (char.islower()):
            result += key_dict[char.upper()].lower()
        else:
            result += char
            
    return result

def initialise_key():
    key_match = {}
    for letter in LETTERS_UPPER:
        key_match[letter] = letter
    
    with open("key.json", "w") as outfile:
        json.dump(key_match, outfile)

    
def update_decrypt(message):
    with open('key.json') as json_file:
        key_match = json.load(json_file)
        
    output = ''
    for char in message:
        if char.isupper():
            output += key_match[char]
        elif char.islower():
            output += key_match[char.upper()].lower()
        else:
            output += char
    print("\nDECRYPTING MESSAGE:")       
    print(output)

    return output
    
def text_analysis(message):
    one = {}
    two = {}
    three = {}
    apos = {}
    index = {}
    
    for letter in LETTERS_UPPER:
        index[letter] = 0
        
    for char in message:
        if char.isalpha():  
            if char.upper() in index:
                index[char.upper()] += 1
                
    for word in message.split():
        word = word.lower()
        if len(word) == 1:
            if word in one:
                one[word] += 1
            else:
                one[word] = 1
        if len(word) == 2:
            if word in two:
                two[word] += 1
            else:
                two[word] = 1
        if len(word) == 3:
            if word in three:
                three[word] += 1
            else:
                three[word] = 1
        if "'" in word:
            if word in apos:
                apos[word] += 1
            else:
                apos[word] = 1
    
    one = sorted(one.items(), key=operator.itemgetter(1), reverse = True)
    two = sorted(two.items(), key=operator.itemgetter(1), reverse = True)
    three = sorted(three.items(), key=operator.itemgetter(1), reverse = True)
    apos = sorted(apos.items(), key=operator.itemgetter(1), reverse = True)
    index = sorted(index.items(), key=operator.itemgetter(1), reverse = True)
    
    print(" ")
    print("The most common letters in English are E, T, A, I, N:")
    print(index[:5])
    print(" ")
    print("Single letter words can be either A or I:")
    print(one[:5])
    print(" ")
    print("The five most common two-letter words, in order of frequency, are OF, TO, IN, IS, and IT:")
    print(two[:5])
    print(" ")
    print("The most common three letter words are THE, AND, FOR, WAS, and HIS:")
    print(three[:5])
    print(" ")
    print("Look for apostrophes. They're generally followed by S, T, D, M, LL, or RE:")
    print(apos[:5])
    print(" ")
    
    
def change_key(from_char, to_char):
    from_char = from_char.upper()
    to_char = to_char.upper()
    
    with open('key.json') as json_file:
        key_match = json.load(json_file)

    char_1 = ''
    char_2 = ''
    
    for key, val in key_match.items():
        if val == from_char:
            char_1 = key
        elif val == to_char:
            char_2 = key
    
    key_match[char_1] = to_char
    key_match[char_2] = from_char
            
    with open("key.json", "w") as outfile:
        json.dump(key_match, outfile)
    
def update_key():
    input_1 = ''
    while True:
        input_1 = input("Enter the letter you'd like to replace: ")
        if input_1.isalpha() and len(input_1) == 1:
            break
        else:
            print("Invalid input. Please only enter one alphabetical letter")
            
    input_2 = ''
    while True:
        input_2 = input("Enter the letter you'd like the replace " + input_1 + " with: ")
        if input_2.isalpha() and len(input_2) == 1 and input_1 != input_2:
            break
        else:
            print("Invalid input. Please only enter one alphabetical letter")
            
    change_key(input_1, input_2)
    print('\n\n')
    
    