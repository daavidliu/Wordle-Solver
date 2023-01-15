from spellchecker import SpellChecker
import random

def caencrypt(text, key):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt characters in plain text
        if (char.isupper()):
             result += chr((ord(char) + key -65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
            
    return result
    
def caedecrypt(message):

    LETTERS_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS_LOWER = 'abcdefghijklmnopqrstuvwxyz'

    outputs = []
    
    spell = SpellChecker()

    for key in range(len(LETTERS_UPPER)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS_UPPER:
                num = LETTERS_UPPER.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS_UPPER)
                translated = translated + LETTERS_UPPER[num]
            elif symbol in LETTERS_LOWER:
                num = LETTERS_LOWER.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS_LOWER)
                translated = translated + LETTERS_LOWER[num]   
            else:
                translated = translated + symbol
        words = translated.split()
        correct = spell.known(words)
        this_dict = {
            "key": key,
            "message": translated,
            "occurrence": len(correct)
        }
        outputs.append(this_dict)
        
    outputs = sorted(outputs, key = lambda i: i['occurrence'])

    for output in outputs:
        print(output['message'] + "\nKEY SHIFTED: " + str(output['key']) + "\nWORDS MATCHED: " + str(output['occurrence']))
        print('\n')


