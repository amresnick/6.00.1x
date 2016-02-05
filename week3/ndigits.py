def ndigits(x):
  """
  INPUT: A positive or negative integer x (zero is neither of these).
  OUTPUT: An integer which is the number of digits in the input integer.
  ALGORITHM: Recursion. Dividing the integer x by 10 reduces the number of digits in x by 1. Thus, for each division by 10, we should add 1 to our running count of the number of digits. Each division by 10 is accomplished by a recursive call to ndigits with an argument of x/10. The absolute value function is used to allow for negative integers, ex -510 and 510 both have the same number of digits.
  """
  #use this to keep track of the number of digits
  number_of_digits = 0

  if x == 0:
      # base case, return 0
      return number_of_digits
  else:
      # recursive step, see ALGORITHM section of docstring
      # use absolute value to allow for negative inputs
      number_of_digits = 1 + ndigits(abs(x/10))
      return number_of_digits
