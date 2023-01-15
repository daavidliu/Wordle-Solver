import random
import operator
import math
import json
from itertools import product

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

    print("                    " + feedback)

    return feedback

def entropy_calculate(word_list, attempt):
    total = 0

    for feedback in FEEDBACKS:
        updated_word_list = update_word_list(attempt, feedback, word_list)
        if updated_word_list != []:
            prob = len(updated_word_list)/len(word_list)
            total += prob * math.log(1/prob,2)
    
    return total
    
def run():
    word_list = WORDS.copy()
    entropy = INITIAL.copy()
    
    answer = random.choice(word_list)
    guesses = 0
    correct = False
    print("                    " + "RECCOMMENDED: " + generate_reccommended(entropy).upper())
    
    while not correct:
        attempt = input("Enter wordle guess: ").lower()
        guesses += 1
        feedback = process(answer, attempt)
        correct = (feedback == "GGGGG")
        ent = entropy_calculate(word_list, attempt)
        print("                    " + "ENTROPY: " + str(ent))
        new_word_list = update_word_list(attempt, feedback, word_list)
        print("                    " + "REMAINING: " + str(len(new_word_list)))
        word_list = new_word_list
        entropy = update_entropy(word_list)
        print("                    " + "RECCOMMENDED: " + generate_reccommended(entropy).upper())

    print("WORDLE WON AFTER " + str(guesses) + "\n")
    return guesses

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
    entropy = {}
    for word in word_list:
        entropy[word] = entropy_calculate(word_list, word)

    return entropy


def generate_reccommended(entropy):
    word_ranking = sorted(entropy.items(), key=operator.itemgetter(1), reverse = True)
    return(word_ranking[0][0])

FEEDBACKS = [''.join(i) for i in product('-GY', repeat = 5)]

WORDS = []
word_file = open("words.txt")

for word in word_file:
    WORDS.append(word.strip())
    
with open('entropy2.json') as json_file:
    INITIAL = json.load(json_file)

total = 0
times = 100

run()