#Problem Statement
#Given a getCube() function, create a list with the cubes of the first 20 numbers.

#Input
#An empty list

#Output
#An updated list with the cube of each value in the list

def getCube():
  l1 = [x**3 for x in range(1,21)] 
  return l1
l1 = getCube()
print(l1)