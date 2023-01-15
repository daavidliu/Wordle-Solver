import random
import wordle_solver
import operator

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

l1 = LETTERS
l2 = LETTERS
l3 = LETTERS
l4 = LETTERS
l5 = LETTERS

word_list = [l1, l2, l3, l4, l5]

def initialise_word_list():
    l1 = LETTERS
    l2 = LETTERS
    l3 = LETTERS
    l4 = LETTERS
    l5 = LETTERS

    word_list = [l1, l2, l3, l4, l5]
    return word_list

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
    # return feedback == "GGGGG" #True if answer == guess, False otherwise 
    
def run():
    answer = ''
    
    for i in range(0, 5):
        answer += random.choice(LETTERS)

    guesses = 0
    correct = False
    
    word_list = initialise_word_list()

    while not correct:
        attempt = generate_reccommended(word_list)
        guesses += 1
        feedback = process(answer, attempt)
        correct = (feedback == "GGGGG")
        word_list = update_word_list(attempt, feedback, word_list)
        
    if correct:
        print(answer + ": " + str(guesses) + " attempts.")
    
    return guesses

def update_word_list(guess, feedback, word_list):
    for i in range(5):
        if feedback[i] == "-":
            word_list[0].replace(guess[i], '')
            word_list[1].replace(guess[i], '')
            word_list[2].replace(guess[i], '')
            word_list[3].replace(guess[i], '')
            word_list[4].replace(guess[i], '')
            break
        elif feedback[i] == "G":
            word_list[i] = ''
            word_list[i] += guess[i]
            break
        elif feedback[i] == "Y":
            word_list[i].replace(guess[i], '')
            break
    return word_list


def generate_reccommended(word_list):
    guess = ''
    for i in range(5):
        guess += random.choice(word_list[i])
        
    return guess
        
total = 0
for i in range(0, 10):
    total += run()
    
print('Average is ' + str(total/10))