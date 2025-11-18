"""
Problem Statement 2
Modify the previous findMaximumValueIndex(list) function such that it returns a list with the first element being the index of the maximum value in the list and the second being the maximum value. Besides keeping the maximum value found so far, you also need to keep the position where it occurred.

Input
A list

Output
Maximum number and index of the number in the list

Sample Input
[1, 4, 23, 10, 9]

Sample Output
max = 23

index = 2
"""

def findMaximumValueIndex(list):
    max_value = list[0]
    max_index = 0

    for i in range(1, len(list)):
        if list[i] > max_value:
            max_value = list[i]
            max_index = i

    return [max_index, max_value]


# Example usage:
data = [1, 4, 23, 10, 9]
result = findMaximumValueIndex(data)

print("max =", result[1])
print("index =", result[0])
