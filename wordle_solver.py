import operator
import random

def update_word_list(guess, feedback, word_list):
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
    for word in word_list:
        i = 0
        x = 1
        for i in range(0, 5):
            x *= (frequency[word[i]][i] / freq_max[i])
            
            if word.count(word[i]) > 1:
                x *= 0.5
            
        word_ranking[word] = x
    
    word_ranking = sorted(word_ranking.items(), key=operator.itemgetter(1), reverse = True)
    
    #print("Guessing " + word_ranking[0][0])
    
    return(word_ranking[0][0])
 
    #return random.choice(word_list)
    

'''
while True:
    guess = input("Enter the guess: ")
    feedback = input("Enter the feedback: ").upper()
    update_word_list(guess, feedback)
    update_frequency()
    print("\nReccomended words are:")
    generate_reccommended()
    print("\n")
'''