
import guesser

def check_input(prompt, choice_1, choice_2, random_word):
    guess = False
    choice = (input(prompt)).upper()
    while choice != choice_1 and choice != choice_2:
        choice = (input(f'\nWrong input! Please enter only {choice_1} or {choice_2}!: ')).upper()
    if choice == choice_1:
        guess = guesser.guessed_word(random_word)
        if guess == True:
            return True
        elif guess == False:
            return 'wrong'
    elif choice == choice_2:
        return False

def yes_no(prompt, choice_1, choice_2):
    choice = (input(prompt)).upper()
    while choice != choice_1 and choice != choice_2:
        choice = (input(f'Wrong input! Please choose only {choice_1} or {choice_2}')).upper()
    if choice == choice_1:
        return True
    elif choice == choice_2:
        return False
        
def letter_check():
    
    letter = (input('\nGuess a letter: ')).lower()
    while len(letter) > 1 or letter == '':
        letter = input('\nPlease enter a single letter only: ')
    else:
        return letter.lower()
        
