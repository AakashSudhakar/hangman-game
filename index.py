import random


# Function to load the secret word into the game
def load_word():
    # Initialize the word bank document
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    # Define list of words from bank
    words_list = words_list[0].split(' ')

    # Assign random choice from bank as secret word and return
    secret_word = random.choice(words_list)
    return secret_word


# Function to update guessed word in play
def update_word(secret_word, current_guess, word_reveal):
    i = 0

    # Loop that iterates through play word's length and updates guessed letters
    while i < len(secret_word):
        if current_guess.lower() == secret_word[i]:
            word_reveal[i] = current_guess.lower()
        i += 1

    # Returns joined string of guessed and empty letter values
    return "".join(word_reveal)


# Function to initialize and retrieve the selected secret word
def get_guessed_word(secret_word, letters_guessed):
    word_reveal = []

    # Loop that iterates through length of word and appends underscores for letter values
    for i in range(len(secret_word)):
        word_reveal.append("_")

    return word_reveal


# Function to retrieve and show letters that have not been guessed yet
# This function is unnecessary; letters can be visually represented otherwise.
# def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''


# Function to reset the game and secret word after success/failure
def reset_game():
    # Accept user input for whether to play again or not
    reset_parameter = raw_input("Dare to tempt fate again? (Y/N)   ")

    # If yes, reset game with new secret word from word bank
    if reset_parameter.lower().startswith("y"):
        print "\nInteresting choice...\n"
        hangman(load_word())
    # If no, exit out of game
    elif reset_parameter.lower().startswith("n"):
        print "\nFly, you fool...\n"
        exit()
    # If user response is unintelligible, accept new user input for game reset
    else:
        print "\nSo it seems the hangman's noose robbed your voice away? Try again...\n"
        reset_game()


# Function to generate and display helpful diagrams for current game state
# def game_image(wrong_guesses):
    # 


# Main function to initialize, start, and play hangman game
def hangman(secret_word):

    wrong_guesses = 0
    letters_guessed = ""

    # Introductory statement to teach rules to new player
    print "\n>> You have been sentenced to death by hanging. But perhaps fate does not wish you dead today... \n"
    print ">> Your only hope is guessing the letters of the secret word before you hang!\n"
    print ">> Guess the letters and try not to get youreself killed! After six (6) incorrect guesses, your fate is sealed!\n"

    # Reveal to player the length of the secret word
    word_reveal = get_guessed_word(secret_word, letters_guessed)
    print "\nThe secret word has " + str(len(secret_word)) + " letters. Dare to guess?\n"

    # Loop to allow for six wrong guesses
    while wrong_guesses < 6:
        # Print guessed letters so far and accept user input for letter guess
        current_guess = raw_input("Enter a letter here: ")

        # If guessed letter is valid and not duplicate, add to guessed letters and notify user of successful guess
        if (current_guess.lower() in secret_word) and (current_guess.lower() not in letters_guessed):
            print "\n******************************"
            print "\nGOOD guess! One step closer to victory and freedom!\n"
            letters_guessed += current_guess.lower() + ". "
            print "Your Guessed Letters: " + letters_guessed + "\n"
            print "Current Progress: " + update_word(secret_word, current_guess, word_reveal) + "\n"

        # If guessed letter is invalid and not duplicate, add to guessed letters, iterate wrong guesses, and notify user of unsuccessful guess
        elif (current_guess.lower() not in secret_word) and (current_guess.lower() not in letters_guessed) and (wrong_guesses <= 5):
            wrong_guesses += 1
            print "\n******************************"
            print "\nBAD guess! One step closer to failure and death...\n"
            letters_guessed += current_guess.lower() + ". "
            print "Your Guessed Letters: " + letters_guessed + "\n"
            print "Current Progress: " + update_word(secret_word, current_guess, word_reveal) + "\n"

        # If guessed letter is a duplicate or not a letter, scold user and notify them to try again
        else:
            print "\nPOOR guess. Try again and pick a letter you haven't already picked!\n"
            print "Your Guessed Letters: " + letters_guessed + "\n"
            print "Current Progress: " + update_word(secret_word, current_guess, word_reveal) + "\n"

        # If user has guessed all letters correctly without losing, notify them of game win and prompt a game reset
        if "".join(word_reveal) == secret_word:
            print "\n******************************"
            print "\nGood job escaping the hangman's noose! It seems fate favors you today."
            print "You win! But perhaps fate has more in store for you...\n"
            reset_game()
            # break

    # If user has guessed too many invalid guesses and lost, notify them of game loss and prompt a game reset
    if wrong_guesses == 6:
        print "\n******************************"
        print "\nThe noose tightens around your neck and darkness consumes you."
        print "You have failed! But fate may save you yet...\n"
        reset_game()


# Load secret word and start game
secret_word = load_word()
hangman(load_word())
