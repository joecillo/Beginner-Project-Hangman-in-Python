
def guessed_word(random_word):
    guess_the_word = (input('\nWhat is the word?: ')).lower()
    if guess_the_word == random_word.lower():
        return True
    else:
        return False

