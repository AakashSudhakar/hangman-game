import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   secret_letters = list(secret_word)
   return secret_word

def is_word_guessed(secret_word, letters_guessed):

    # Check for single false case, rest simply passes as true
    i = 0

    while i < len(secret_word):
        if current_guess == secret_word[i]:
            word_reveal[i] = current_guess
        i += 1

def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    word_reveal = []

    for i in range(len(secret_word)):
        word_reveal.append("_")

    return word_reveal

# def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    # I don't think this is necessary...

    """available_letters = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(letters_guessed)):
        if (letters_guessed[i] is in available_letters):
            """

def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''

    wrong_guesses = 0

    print "Guess letters and try not to hang yourself! You have six (6) guesses!"
    print "There are " + str(len(secret_word) - int(letters_guessed)) + " letters left!"

    while wrong_guesses < 6:
        current_guess = raw_input("Enter a letter here: ")

        if (current_guess is in secret_word) and (current_guess is in available_letters):
            print "Good guess! One step closer to victory and freedom!"

        elif (current_guess is not in secret_word) and (current_guess is in available_letters):
            wrong_guesses += 1
            print "Bad guess! One step closer to failure and death..."

        else:
            print "Poor guess. Try again and pick a letter you haven't already picked!"

        if "".join(word_reveal) == secret_word:
            print "Good job escaping the hangman's noose!"
            print "You win!"
            break

secretWord = loadWord()
hangman(loadWord())
