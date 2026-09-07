import random
file = open("words.txt", "r")
words = file.read().splitlines()
word = random.choice(words)
print("Here is the word:")
for _ in range(len(word)):
    print("_", end = " ")
guessed = []
max_guess = 6

for i in range(max_guess):
    display = ''
    letter = input("\nGuess a letter: \n").lower()
    guessed.append(letter)
    if letter in word:
        print("\nCorrect guess!")
    else:
        print("\nIncorrect guess!")
        max_guess -= 1

    for letter in word:
        if letter in guessed:
            display += letter + ' '
        else:
            display += '_ '
    if(len(display.replace('_','').replace(' ','')) == len(word)):
            print("Win! The word was:",word)
            break
    if(max_guess == 0):
        print("Loose! The word was:", word)
        break
    if(max_guess>0):
        print("\nCurrent word:\n", display)
    
file.close()