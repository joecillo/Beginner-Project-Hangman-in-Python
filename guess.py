
def guessed_word(random_word):
    guess_the_word = input('\nWhat is the word?: ')
    if guess_the_word == random_word:
        return True
    else:
        return False
    
