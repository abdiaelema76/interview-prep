"""_summary_
    Problem Statement
Use the calculateSinCosTan() function; it takes a number x as a parameter and shows the result of the sine, cosine, and tangent of the number.

Input
A number

Output
Calculate the sine, cosine, and tangent of that number

Sample Input
0

Sample Output
[0, 1, 0]
    """
import math
def calculateSinCosTan(x):
  #write your function here
  sine =math.sin(x)#calculate sine
  cos = math.cos(x)#calculate cosine
  tan = math.tan(x)#calculate tangent 
  return [sine, cos, tan]
print("sine, cos, tan:", calculateSinCosTan(-1))
print("sine, cos, tan:", calculateSinCosTan(0))
print("sine, cos, tan:", calculateSinCosTan(1))