"""
Problem Statement
Implement a sum_N_Numbers recursive function to compute the sum of the n natural numbers (where (n) is a function parameter). Start by thinking about the base case (the sum of the first 1 integers is?) and then think about the recursive case.

Note: Natural Numbers start from 1, i.e., 1, 2, 3, 4, 5, …

Input
A natural number n

Output
The sum of all numbers from 1 upto that input natural number n

Sample Input
7

Sample Output
28
"""
def sum_N_Numbers (n):
  # Write code here
  if n <= 1:
    return 1
  else:
   return sum_N_Numbers(n-1) + n
print(sum_N_Numbers(5))