import random
import operator
import matplotlib.pyplot as plt
import math

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
    
    for word in word_list:
        feedback = process(word, attempt)
        updated_word_list = update_word_list(attempt, feedback, word_list)
        
        prob = len(word_list)/len(updated_word_list)
        total += prob * math.log(1/prob,2)

    return total
    
def run():
    word_list = []
    word_file = open("words.txt")

    for word in word_file:
        word_list.append(word.strip())
        
    answer = random.choice(word_list)

    guesses = 0
    correct = False

    frequency = {}
    frequency = update_frequency(frequency, word_list)

    attempt = "wryly"
    
    
    feedback = process(answer, attempt)
    #print(feedback)
    correct = (feedback == "GGGGG")
    update_word_list(attempt, feedback, word_list)
    update_frequency(frequency, word_list)
    remain = len(word_list)
    prob = remain/2315
    
    dict[feedback] = prob
    
    print(feedback + " remaining: " + str(remain) + " probability: " + str(prob))
    

    return guesses

def update_word_list(guess, feedback, words):
    word_list = words
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
    
def initialise_frequency(frequency):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        frequency[letter] = [0, 0, 0, 0, 0]
    return frequency
    
def update_frequency(frequency, word_list):
    initialise_frequency(frequency)
    for word in word_list:
        i = 0
        for letter in word:
            frequency[letter][i] += 1
            i += 1 
    return frequency
    #print(frequency)

def generate_reccommended(frequency, word_list):
    
    freq_max = [0, 0, 0, 0, 0]
    for key, val in frequency.items():
        for i in range(0, 5):
            if freq_max[i] < val[i]:
                freq_max[i] = val[i]
    
    word_ranking = {}
    words = ''
    for word in word_list:
        words += word + ' '
        i = 0
        x = 1
        for i in range(0, 5):
            x *= (frequency[word[i]][i] / freq_max[i])
            
            if word.count(word[i]) > 1:
                x *= 0.5
            
        word_ranking[word] = x
    
    word_ranking = sorted(word_ranking.items(), key=operator.itemgetter(1), reverse = True)
    
    #print("Guessing " + word_ranking[0][0])
    
    print(words)
    
    return(word_ranking[0][0])
 
    #return random.choice(word_list)
    
dict = {}
        
for i in range(0, 1000):
    run()


names = list(dict.keys())
values = list(dict.values())
values.sort(reverse = True)

plt.bar(range(len(dict)), values, tick_label=names)
plt.show()