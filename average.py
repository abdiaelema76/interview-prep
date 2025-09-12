#Problem Statement
#Given a getAverage() function, create a list named l with the following values:

#[1, 4, 9, 10, 23]

#Calculate the average value of all values in the list.

#Input
#A list of integers

#Output
#An average of values in the list

#Sample Input
#[1, 4, 9, 10, 23]

#Sample Output
#9.4

def getAverage():
    l = [1, 4, 9, 10, 23]
    avg = sum (l) / len(l)
    return avg
print(getAverage())