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

    print "Guess letters and try not to hang yourself! You have six (6) guesses!"
    print "There are " + str(len(secret_word) - int(letters_guessed)) + " letters left!"

    while wrong_guesses < 6:
        current_guess = raw_input("Enter a letter here: ")

        if (current_guess is in secret_word) and (current_guess is in available_letters):
            print "Good guess! One step closer to victory and freedom!"
            letters_guessed += current_guess + ". "
            print "Current Progress: " + word_reveal #This will probably not work


        elif (current_guess is not in secret_word) and (current_guess is in available_letters):
            wrong_guesses += 1
            print "Bad guess! One step closer to failure and death..."
            print "Current Progress: " + word_reveal #This will probably not work

        else:
            print "Poor guess. Try again and pick a letter you haven't already picked!"
            print "Current Progress: " + word_reveal #This will probably not work

        if "".join(word_reveal) == secret_word:
            print "Good job escaping the hangman's noose!"
            print "You win!"
            break

secretWord = loadWord()
hangman(loadWord())
