
def remaining_letters(random_word_listed, guessed_letters):
    for letter in random_word_listed:
        if letter.lower() in ''.join(guessed_letters):
            print(letter, end = ' ')
        else:
            print(' _ ', end = ' ')
            
