import random



def run():
    """
    Manages game instance.
    """
    f = open("hangman_dictionary.txt", "r")
    words = f.read().split()
    f.close()

    # The status of each letter in the randomly chosen word is tracked by a dict.
    # Unguessed letters are False, others are true.
    # Currently, everything is unguessed, so everything is False.
    random_word = random.choice(words)
    word = dict((letter, False) for letter in random_word)

    guesses = []
    num_guesses = 6     # 2 arms, 2 legs, body, head

    print "Let's play Hangman!"

    while num_guesses > 0:
        print "_____________________________________\n"
        print "You have", num_guesses, "wrong guess(es) left."

       # Error checking: user might enter a non-alpha character, more than one character, or a previous guess.
        while True:
            letter = raw_input("Guess a letter: ")
            if len(letter) != 1 or letter.isalpha() == False:
                print "Oops! That's not a letter. Try again."
                print ""
                print "You have", num_guesses, "wrong guess(es) left."
            elif letter in guesses:
                print "You already guessed that. Guess again!"
                print ""
                print "You have", num_guesses, "wrong guess(es) left."
            else:
                guesses.append(letter)
                break

        if letter in word:
            word[letter] = True
            print_word(word, random_word)
            if check_win(word):
                print "You win! No hangings today..."
                break
            print "Good job, that's a letter!"
        else:
            num_guesses -= 1
            print_word(word, random_word)
            print "Oh no, that's not a letter in the word! One step closer...\n"
            draw(num_guesses)

    if num_guesses == 0:
        print "Sorry, but the man hangs! The word was", random_word, "."

    while True:
        go_again = raw_input("Do you want to play again (Y or N)?")
        if go_again in ["y", "Y", "yes", "Yes"]:
            run()
        else:
            print "OK, bye!"
            break


def print_word(word, letters):
    """
     Prints word each time a guess is made so player can see progress.
    """

    # Need to use a string to place letters because dicts are unordered.
    # So, for each letter in the word, if the letter's value in word (a dict) is True, print the letter.
    # Otherwise, print an underscore.
    for letter in letters:
        if word[letter]:
            print letter,
        else:
            print "_",
    print "\n"


def check_win(word):
    """
    Return True if word is complete, False otherwise.
    """
    # If every letter in word (a dict) has been guessed (and thus has a value of True), return True.
    if False not in word.values():
        return True
    return False


# Because I can't TKinter.
def draw(state):
    """
    Draws the hangman on each valid guess!
    """
    if state == 5:
        print "|-----"
        print "|  O  "
        print "|     "
        print "|     "
    elif state == 4:
        print "|-----"
        print "|  O  "
        print "|  |  "
        print "|     "
    elif state == 3:
        print "|-----"
        print "|  O  "
        print "| -|  "
        print "|     "
    elif state == 2:
        print "|-----"
        print "|  O  "
        print "| -|- "
        print "|     "
    elif state == 1:
        print "|-----"
        print "|  O  "
        print "| -|- "
        print "| /   "
    elif state == 0:
        print "|-----"
        print "|  O  "
        print "| -|- "
        print "| /\\ "


run()



