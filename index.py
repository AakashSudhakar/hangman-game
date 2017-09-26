import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   # secret_letters = list(secret_word)
   return secret_word

def is_word_guessed(secret_word, current_guess, word_reveal):

    i = 0

    while i < len(secret_word):
        if current_guess == secret_word[i]:
            word_reveal[i] = current_guess
        i += 1

    return "".join(word_reveal)

def get_guessed_word(secret_word, letters_guessed):

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

    # I don't think this function is necessary...

    """available_letters = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(letters_guessed)):
        if (letters_guessed[i] is in available_letters):
            """

def hangman(secret_word):

    wrong_guesses = 0
    letters_guessed = ""

    print "Guess letters and try not to hang yourself! You have six (6) wrong guesses!"
    # print "There are " + str(len(secret_word) - int(letters_guessed)) + " letters left!"

    word_reveal = get_guessed_word(secret_word, letters_guessed)
    print "The secret word has " + str(len(secret_word)) + " letters. Dare to guess?\n"

    while wrong_guesses < 6:
        current_guess = raw_input("Enter a letter here: ")

        if (current_guess in secret_word) and (current_guess not in letters_guessed):
            print "Good guess! One step closer to victory and freedom!\n"
            letters_guessed += current_guess + ". "
            print "Current Progress: " + is_word_guessed(secret_word, current_guess, word_reveal) #This will probably not work


        elif (current_guess not in secret_word) and (current_guess not in letters_guessed) and (wrong_guesses <= 5):
            wrong_guesses += 1
            print "Bad guess! One step closer to failure and death...\n"
            letters_guessed += current_guess + ". "
            print "Current Progress: " + is_word_guessed(secret_word, current_guess, word_reveal) #This will probably not work

        else:
            print "Poor guess. Try again and pick a letter you haven't already picked!\n"
            print "Current Progress: " + is_word_guessed(secret_word, current_guess, word_reveal) #This will probably not work

        if "".join(word_reveal) == secret_word:
            print "Good job escaping the hangman's noose!\n"
            print "You win!"
            break

    if wrong_guesses == 6:
        print "The noose tightens around your neck and darkness consumes you."
        print "You have failed! But fate may save you yet...\n"
        reset_game = raw_input("Dare to try again? ")

        if (reset_game == "y") or (reset_game == "Y") or (reset_game == "yes") or (reset_game == "YES"):
            print "\nInteresting choice...\n"
            hangman(load_word())
        elif (reset_game == "n") or (reset_game == "N") or (reset_game == "no") or (reset_game == "NO"):
            print "\nBetter luck next time...\n"


secret_word = load_word()
hangman(load_word())
