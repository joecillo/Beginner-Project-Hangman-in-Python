
def check_letter(letter, random_word, guessed_letters):
    if letter in random_word.lower():
        if letter in guessed_letters:
            return 'already guessed'
        else:
            return letter.lower()
    else:
        return False
    
