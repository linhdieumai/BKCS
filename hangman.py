import random


def choose_topic(file_animal, file_jobs, file_things):
    while True:
        topic = input('Choose a topic (animal, jobs, things) (a/j/t): \n').lower()
        if topic == 'a':
            file_animal.seek(0)  # Đưa con trỏ về đầu file
            words = file_animal.read().splitlines()
            print("You have chosen the topic: Animal")
            return words
        elif topic == 'j':
            file_jobs.seek(0)    # Đưa con trỏ về đầu file
            words = file_jobs.read().splitlines()
            print("You have chosen the topic: Jobs")
            return words
        elif topic == 't':
            file_things.seek(0)  # Đưa con trỏ về đầu file
            words = file_things.read().splitlines()
            print("You have chosen the topic: Things")
            return words
        else:
            print("Invalid topic. Please choose again.")


def choose_level(words):
    while True:
        level = input('Choose a level (easy, medium, hard) (e/m/h): \n').lower()
        if level == 'e':
            word = random.choice([w for w in words if len(w) <= 5])
            guess_allowed = 6
            return word, guess_allowed
        elif level == 'm':
            word = random.choice([w for w in words if 6 <= len(w) <= 8])
            guess_allowed = 8
            return word, guess_allowed
        elif level == 'h':
            word = random.choice([w for w in words if len(w) > 8])
            guess_allowed = 10
            return word, guess_allowed
        else:
            print("Invalid level. Please choose again.")


def process_guess(letter, word, guessed, guessed_wrong, wrong_guess, guess_allowed, check_hint):
    if (letter == 'hint' and not check_hint):
        check_hint = True
        if len(guessed) == 0:
            hint_letter = random.choice(word)
        else:
            hint_letter = random.choice([w for w in word if w not in guessed])
        print(f"\nHint: The word contains the letter '{hint_letter}'.")
        guessed.append(hint_letter)
        guess_allowed -= 1
    elif (letter == 'hint' and check_hint):
        print("\nYou have already used the hint. You can only use it once per game.")
    elif (letter not in 'abcdefghijklmnopqrstuvwxyz' or len(letter) != 1):
        print("\nInvalid input. Please enter another one.\n")
    elif (letter in guessed): 
        print("\nYou have already guessed that letter.\n")
    else:
        guessed.append(letter)
        if letter in word:
            print("\nCorrect guess!")
        else:
            print("\nIncorrect guess!")
            wrong_guess += 1
            guessed_wrong.append(letter)
            
    return wrong_guess, guess_allowed, check_hint


def play_game(file_animal, file_jobs, file_things):
    print('Welcome to Hangman Game!')
    print("Note: If you want to use hint, type 'hint' and press enter whenever you want to use. You can only use hint once per game and you will lose a guess for that hint.")
    
    words = choose_topic(file_animal, file_jobs, file_things)
    word, guess_allowed = choose_level(words)
    
    print("Here is the word:")
    for _ in range(len(word)):
        print("_", end = " ")

    guessed = []
    guessed_wrong = []
    wrong_guess = 0
    check_hint = False
    
    while(wrong_guess < guess_allowed):
        display = ''
        letter = input("\nGuess a letter: \n").lower()
        
        wrong_guess, guess_allowed, check_hint = process_guess(
            letter, word, guessed, guessed_wrong, wrong_guess, guess_allowed, check_hint
        )
        
        for letter in word:
            if letter in guessed:
                display += letter + ' '
            else:
                display += '_ '
                
        if(len(display.replace('_','').replace(' ','')) == len(word)):
            print("Win! The word was:", word)
            break
        if(wrong_guess == guess_allowed):
            print("Loose! The word was:", word)
            break
        if(wrong_guess < guess_allowed):
            print("Current word:\n", display)
            print("Guessed letters:", guessed)
            print('Guess times left:', guess_allowed - wrong_guess)


def main():
    file_animal = open("words_animal.txt", "r")
    file_jobs = open("words_jobs.txt", "r")
    file_things = open("words_things.txt", "r")

    while(True):
        play_game(file_animal, file_jobs, file_things)
        
        choice = input("\nDo you want to play again? (y/n): \n").lower()
        if(choice != 'y'):
            print("Thank you for playing! Goodbye!")
            break   

    file_animal.close()
    file_jobs.close()
    file_things.close()


if __name__ == "__main__":
    main()