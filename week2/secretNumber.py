print "Please think of a number between 0 and 100!"
high = 100
low = 0
guess = 50
isCorrect = False

while not isCorrect:
  print "Is your secret number " + str(guess) + "?"

  response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

  if response == 'h':
    high = guess
    guess = int(0.5 * (high + low))
  elif response == 'l':
    low = guess
    guess = int(0.5 * (high + low))
  elif response == 'c':
    print "Game over. Your secret number was: " + str(guess)
    isCorrect = True
  else:
    print "Sorry, I did not understand your input."
