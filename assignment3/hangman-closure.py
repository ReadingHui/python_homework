# Task 4: Closure Practice
def make_hangman(secret_word):
    guess = []
    def hangman_closure(letter):
        nonlocal guess
        if len(letter) != 1:
            print('The guess is not a single letter!')
            return False
        if not letter.isalpha():
            print('The guess is not a letter!')
            return False
        if letter in guess:
            print('You already guessed this letter!')
            return False
        guess.append(letter.lower())
        guessed_word = ''.join([c if c.lower() in guess else '_' for c in secret_word])
        print(guessed_word)
        if guessed_word == secret_word:
            return True
        else:
            return False
    return hangman_closure

def main():
    secret_word = input('What is your secret word?')
    game = make_hangman(secret_word=secret_word)
    guess = input('Your guess!')
    while not game(guess):
        guess = input('Your guess!')
    print(f'Congratulations! You guessed the correct word "{secret_word}"!')

if __name__ == '__main__':
    main()
