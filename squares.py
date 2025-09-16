#Problem Statement
#Given a getSquare() function, create a list with the squares of the first 10 numbers, i.e., in the range from 1-10.

#Input
#An empty list

#Output
#An updated list with the square of each value in the list

def getSquare():
  l1 = [x*x for x in range(1, 11)] 
  return l1
l1 = getSquare()
print(l1)