import random
import wordle_solver

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

    word_list = []
    word_file = open("words.txt")

    for word in word_file:
        word_list.append(word.strip())
        
    answer = random.choice(word_list)

    guesses = 0
    correct = False

    frequency = {}
    frequency = wordle_solver.update_frequency(frequency, word_list)

    while not correct:
        attempt = wordle_solver.generate_reccommended(frequency, word_list)
        print(attempt)
        guesses += 1
        feedback = process(answer, attempt)
        print(feedback)
        correct = (feedback == "GGGGG")
        wordle_solver.update_word_list(attempt, feedback, word_list)
        wordle_solver.update_frequency(frequency, word_list)
        
    #print(answer + ": " + str(guesses) + " attempts.")
    print("WON AFTER " + str(guesses))
    return guesses
        
total = 0
for i in range(0, 1000):
    total += run()
    
print('Average is ' + str(total/1000))