"""
Problem Statement
Create a sumList function that receives a list as a parameter and returns the sum of all the elements in the list.

Input
A list

Output
Sum of elements in the list

Sample Input
[1, 2, 3, 4, 5]

Sample Output
15
"""

def sumList(l):
    sum = 0
    for x in l:
        sum += x
    return sum
l = [1, 2, 3, 4, 5]
print(sumList(l))