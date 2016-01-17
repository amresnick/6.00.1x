import math

def polysum(n,s):
  """
  polysum takes an integer number of sides, n, and integer length of each side, s. It computes the area and perimeter of a regular polygon with n sides of length s and adds the area and the square of the perimeter. Function returns this sum, rounded to 4 decimal places.
  """
  sum = area(n, s) + perimeter(n,s)**2
  sum = round(sum,4) #round sum to 4 decimal places
  return sum

def area(n,s):
  """
  Computes the area of a regular polygon with n sides, each of lenght s.
  """
  return (0.25*n*s**2)/(math.tan(math.pi/n))

def perimeter(n,s):
  """
  Computes the perimeter of something with n sides, each of which are of length s.
  """
  return n*s
