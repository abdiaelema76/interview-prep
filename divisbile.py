"""
Problem Statement
Implement a function named isDivisible that receives two parameters (named x and y) and only returns true if “x” can be divided by “y”(and false otherwise).

A number is divisible by another when the remainder of the division is zero. Use the modulo operator ("%").

Input
Two numbers x and y

Output
Returns true if x is divisible by y and false otherwise

Sample Input
x = 4, y = 2

Sample Output
True
"""
def isDivisible(x, y):
  # Write code here!
  if x % y == 0:
   return True
  else:
      return False
print(isDivisible(9,3))
print(isDivisible(24, 7))