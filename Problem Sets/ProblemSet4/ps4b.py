from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score_so_far = 0

    # Create a new variable to store the best word seen so far (initially None)
    best_word_so_far = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):

            # Find out how much making that word is worth
            score = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if score > max_score_so_far:

                # Update your best score, and best word accordingly
                max_score_so_far = score
                best_word_so_far = word


    # return the best word you found.
    return best_word_so_far


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total = 0

    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand)>0):

        # Display the hand
        print "Current Hand: ",
        displayHand(hand)

        # Ask user for input
        word = compChooseWord(hand, wordList, n)

        # If the input is None
        if word == None:

            # End the game (break out of the loop)
            break


        # Otherwise (the input is not a None):
        else:
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word, please try again.'
                print

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total += getWordScore(word, n)
                print '"' + word + '" ' + 'earned ' + str(getWordScore(word,n)) + ' points. Total: ' + str(total) + ' points'
                print

                # Update the hand
                hand = updateHand(hand, word)


    # Game is over, so tell user the total score

    print 'Total score: ' + str(total) + ' points.'
    print

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    # Really not the best organized, but oh well
    command = ''
    player = ''
    trigger = True

    while(True):
        # Ask the user what they would like to do
        command = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

        # Check if command is legal
        if not (command in {'e', 'r', 'n'}):
            print 'Invalid command.'
            print
        else: # The command is good
            if command == 'e': # Must exit, so break out of game loop
                break
            if command == 'r': # Make sure this isn't the first hand
                try:
                    hand
                except NameError:
                    print 'You have not played a hand yet. Please play a new hand first!'
                    print

                    # Don't want game to continue to ask for player, so disable that while loop
                    trigger = False

            print

            while(trigger):

                # Ask for the player
                player = raw_input('Enter u to have yourself play, c to have the computer play: ')

                # Check if player choice is legal
                if not (player in {'u', 'c'}):
                    print 'Invalid command.'
                    print
                else: # It's a legal choice
                    if command == 'n': # New hand
                        hand = dealHand(HAND_SIZE)
                        if player == 'u':
                            playHand(hand,wordList,HAND_SIZE)
                        elif player == 'c':
                            compPlayHand(hand, wordList, HAND_SIZE)
                    elif command == 'r': # Replay last hand
                        if player == 'u':
                            playHand(hand,wordList,HAND_SIZE)
                        elif player == 'c':
                            compPlayHand(hand,wordList,HAND_SIZE)
                    break


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

