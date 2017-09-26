import random

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
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

    # This function is unnecessary; letters can be visually represented otherwise.

def reset_game():
    reset_parameter = raw_input("Dare to tempt fate again? (Y/N)   ")

    if reset_parameter.lower().startswith("y"):
        print "\nInteresting choice...\n"
        hangman(load_word())
    elif reset_parameter.lower().startswith("n"):
        print "\nFly, you fool...\n"
        exit()
    else:
        print "\nIt seems the noose robbed your voice away, eh? Try again...\n"
        reset_game()

def hangman(secret_word):

    wrong_guesses = 0
    letters_guessed = ""

    print "\nGuess letters and try not to hang yourself! You have six (6) wrong guesses!\n"

    word_reveal = get_guessed_word(secret_word, letters_guessed)
    print "The secret word has " + str(len(secret_word)) + " letters. Dare to guess?\n"

    while wrong_guesses < 6:
        current_guess = raw_input("Enter a letter here: ")

        if (current_guess in secret_word) and (current_guess not in letters_guessed):
            print "\nGood guess! One step closer to victory and freedom!\n"
            letters_guessed += current_guess + ". "
            print "Current Progress: " + is_word_guessed(secret_word, current_guess, word_reveal) + "\n"


        elif (current_guess not in secret_word) and (current_guess not in letters_guessed) and (wrong_guesses <= 5):
            wrong_guesses += 1
            print "\nBad guess! One step closer to failure and death...\n"
            letters_guessed += current_guess + ". "
            print "Current Progress: " + is_word_guessed(secret_word, current_guess, word_reveal) + "\n"

        else:
            print "\nPoor guess. Try again and pick a letter you haven't already picked!\n"
            print "Current Progress: " + is_word_guessed(secret_word, current_guess, word_reveal) + "\n"

        if "".join(word_reveal) == secret_word:
            print "\nGood job escaping the hangman's noose! It seems fate favors you today."
            print "You win! But perhaps fate has more in store for you...\n"
            reset_game()
            # break

    if wrong_guesses == 6:
        print "The noose tightens around your neck and darkness consumes you."
        print "You have failed! But fate may save you yet...\n"
        reset_game()



secret_word = load_word()
hangman(load_word())
