# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(secretWord) == 1:
        return secretWord in lettersGuessed
    elif len(lettersGuessed) == 0:
        return False
    else:
        return (secretWord[0] in lettersGuessed) and isWordGuessed(secretWord[1:], lettersGuessed)




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''
    if len(secretWord) == 1:
        if secretWord in lettersGuessed:
            s += secretWord
            return s
        else:
            s += ' _ '
            return s
    else:
        if secretWord[0] in lettersGuessed:
            s += secretWord[0] + getGuessedWord(secretWord[1:], lettersGuessed)
            return s
        else:
            s += ' _ ' + getGuessedWord(secretWord[1:], lettersGuessed)
            return s






def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    allLetters = string.ascii_lowercase
    returnString = ''

    for letter in range(len(allLetters)):
        if allLetters[letter] not in lettersGuessed:
            returnString += allLetters[letter]

    return returnString
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game Hangman!"
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'

    numGuesses = 8
    lettersGuessed = []

    while (not isWordGuessed(secretWord, lettersGuessed)) or numGuesses > 0:
        print '-----------'
        print 'You have ' + str(numGuesses) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()

        oldWordState = getGuessedWord(secretWord, lettersGuessed)
        oldGuessState = getAvailableLetters(lettersGuessed)
        lettersGuessed.append(guess)
        newWordState = getGuessedWord(secretWord, lettersGuessed)
        newGuessState = getAvailableLetters(lettersGuessed)

        if oldGuessState == newGuessState:
            print "Oops! you've already guessed that letter: " + oldWordState
        elif oldWordState == newWordState:
            print 'Oops! that letter is not in my word: ' + newWordState
            numGuesses -= 1
            if numGuesses <= 0:
                break
        else:
            print 'Good guess: ' + newWordState
            if isWordGuessed(secretWord, lettersGuessed):
                break

    if isWordGuessed(secretWord, lettersGuessed):
        print '-----------'
        print "Congratulations, you won!"
    else:
        print '-----------'
        print "Sorry, you ran out of guesses. The word was " + secretWord + "."





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'sea'
#secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
