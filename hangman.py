import random
file = open("words.txt", "r")
words = file.read().splitlines()
while(True):
    word = random.choice(words)
    print("Here is the word:")
    for _ in range(len(word)):
        print("_", end = " ")
    guessed = []
    guessed_wrong = []
    wrong_guess = 0
    while(wrong_guess < 6):
        display = ''
        letter = input("\nGuess a letter: \n").lower()
        if(letter == '' or letter not in 'abcdefghijklmnopqrstuvwxyz' or len(letter) != 1):
            print("\nInvalid input. Please enter another one.\n")
        elif(letter in guessed):
            print("\nYou have already guessed that letter.\n")
        else:
            guessed.append(letter)
            if letter in word:
                print("\nCorrect guess!")
            else:
                print("\nIncorrect guess!")
                wrong_guess += 1
                guessed_wrong.append(letter)
        for letter in word:
            if letter in guessed:
                display += letter + ' '
            else:
                display += '_ '
        if(len(display.replace('_','').replace(' ','')) == len(word)):
                print("Win! The word was:",word)
                break
        if(wrong_guess == 6):
            print("Loose! The word was:", word)
            print("Incorrect guesses:", guessed_wrong)
            break
        if(wrong_guess < 6):
            print("Current word:\n", display)
            print("Guessed letters:", guessed)
            print('Guess times left:',6 - wrong_guess)  
    choice = input("\nDo you want to play again? (y/n): \n").lower()
    if(choice != 'y'):
        break   
file.close()