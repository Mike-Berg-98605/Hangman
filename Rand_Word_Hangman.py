import random

def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman. Do your Best to guess the word.')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
            print('Good guess! Way to use your noodle!')
        else:
            wrong_guesses += 1
            print('Uh-Oh, not a good choice!')
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('Congratulations! You won the game! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('Awww shucks, you lost! The word was: {}'.format(word))

hangman()
