"""
Problem Statement
Implement the findMaximum function that receives two numbers as arguments x and y and returns the maximum of the numbers.

Input
Two numbers x and y

Output
The maximum of two numbers x and y

Sample Input
x = 2, y = 3

Sample Output
3
"""
def findMaximum(x, y):
  max2 = 0
  if(x > y):
    max2 = x
  else:
    max2 = y
  return max2
print(findMaximum(3, 9))

