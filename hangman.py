
import random
import checker
import show_letters
import hangman_art
import input_checker
import show_instructions
import randomizer

show_instructions.readme()

lives = 6
answer = ''
guessed_letters = []

while True:
    
    random_word = randomizer.word()
    random_word_listed = list(random_word)
    
    print('\nThe word you need to guess has ' + str(len(random_word)) + ' letters.')
    
    while lives > 0 and answer != random_word:
    
        letter = input_checker.letter_check()
        
        letter_in_random_word = checker.check_letter(letter, random_word, guessed_letters)
        if letter_in_random_word == 'already guessed':
            print('\nYou already guessed this letter!')
    
        elif letter_in_random_word == False:
            print('\nLetter not in the word!')
            lives -= 1
            hangman_art.drawing(lives)
            show_letters.remaining_letters(random_word_listed, guessed_letters)
            print('\n')
        else:
        
            print('\nYou guessed a letter!\n')
            guessed_letters.append(letter_in_random_word)
            show_letters.remaining_letters(random_word_listed, guessed_letters)
            print('\n')
    
        guess_the_word = input_checker.check_input('\nDo you know the word? Y/N: ', 'Y', 'N', random_word)
    
        if guess_the_word == True:
            print('\nYou guessed the word!')
            show_instructions.win_text()
            break
            
        elif guess_the_word == 'wrong':
            print('\nThe word you guessed is wrong!')
            lives -= 1
            if lives < 0:
                break
            else:
                hangman_art.drawing(lives)
                
        elif guess_the_word == False:
            if lives == 0:
                break
            else:
                continue
            

    if lives == 0 and guess_the_word == 'wrong':
        show_instructions.lose_text()
        print(f'\nThe word is {random_word}')
        retry = input_checker.yes_no('\nDo you want to play again? Y/N: ', 'Y', 'N')
        if retry == True:
            lives = 6
            guessed_letters = []
            print('\n\nNEW GAME!')
            continue
        else:
            print('\nThank you for playing!')
            break
            
    elif guess_the_word == True:
        retry = input_checker.yes_no('\nDo you want to play again? Y/N: ', 'Y', 'N')
        if retry == True:
            lives = 6
            guessed_letters = []
            print('\n\nNEW GAME!')
            continue
        else:
            print('\nThank you for playing!')
            break
    
    elif guess_the_word == 'wrong':
        show_instructions.lose_text()
        print(f'\nThe word is {random_word}.')
        retry = input_checker.yes_no('\nDo you want to play again? Y/N: ', 'Y', 'N')
        if retry == True:
            lives = 6
            guessed_letters = []
            print('\n\nNEW GAME!')
            continue
        else:
            print('\nThank you for playing!')
            break
        
    elif lives == 0 and guess_the_word == False:
        show_instructions.lose_text()
        print(f'\nThe word is {random_word}')
        retry = input_checker.yes_no('\nDo you want to play again? Y/N: ', 'Y', 'N')
        if retry == True:
            lives = 6
            guessed_letters = []
            print('\n\nNEW GAME!')
            continue
        else:
            print('\nThank you for playing!')
            break
