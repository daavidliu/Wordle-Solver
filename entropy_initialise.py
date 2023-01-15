import random
import operator
import math
from itertools import product
import json

def process(answer, guess):
    position = 0
    feedback = ""
    for letter in guess:
        if letter == answer[position]:
            feedback += "G"
        elif letter in answer:
            feedback += "Y"
        else:
            feedback += "-"
        position += 1
        
    return feedback

def entropy_calculate(word_list, attempt):
    
    total = 0
    
    for feedback in FEEDBACKS:
        updated_word_list = update_word_list(attempt, feedback, word_list)
        if updated_word_list != []:
            prob = len(updated_word_list)/len(word_list)
            #print(prob)
            total += prob * math.log(1/prob,2)

    return total
    
    

def update_word_list(guess, feedback, words):
    word_list = words.copy()
    for word in tuple(word_list):
        for i in range(5):
            if feedback[i] == "-" and guess[i] in word:
                word_list.remove(word)
                break
            elif feedback[i] == "G" and guess[i] != word[i]:
                word_list.remove(word)
                break
            elif feedback[i] == "Y" and guess[i] not in word:
                word_list.remove(word)
                break
            elif feedback[i] == "Y" and guess[i] == word[i]:
                word_list.remove(word)
                break
    return word_list
    
def update_entropy(word_list):
    #print(word_list)
    entropy = {}
    for word in word_list:
        print(word)
        entropy[word] = entropy_calculate(word_list, word)
        #print(word_list)
        
    #print(entropy)
    return entropy

FEEDBACKS = [''.join(i) for i in product('-GY', repeat = 5)]


word_list = []
word_file = open("words.txt")

for word in word_file:
    word_list.append(word.strip())
    
#print(word_list)
entropy = update_entropy(word_list)

with open("entropy2.json", "w") as outfile:
    json.dump(entropy, outfile)
    
print("done")
exit()