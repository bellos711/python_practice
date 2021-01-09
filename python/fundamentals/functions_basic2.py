# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# list1 = []
# list1.append(1)
# list1.append(2)
# list1.append(3)
# print(list1)

myArr = []
def countdown(n):
    for i in range(n, -1, -1):
        myArr.append(i)

countdown(5)
print(myArr, "\n\n")


# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(arr):
    print(arr[0], end=" ")
    return arr[1]

print_and_return_num = print_and_return([1,2])
print(print_and_return_num, "\n\n")


# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(arr):
    return arr[0] + len(arr)
    
print(first_plus_length([1,2,3,4,5]),"\n\n") 


# Values Greater than Second - Write a function that accepts a list and creates a new list containing 
# only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

#PSEUDOCODE for values greater than second
#declare function
#declare an empty array secondArray
#declare a highNum variable and set it to 0
#loop through list by 2s
#compare current index and index+1
#make if statement to set if current index is greater than index+1 if so, max = current index, else max = index+1
#append max to secondArray
#set max back to 0
#after for loop, return secondArray

def values_greater_than_second(arr):
    if(len(arr)==1 or len(arr)%2!=0):
        return False
    else:
        secondArray=[]
        highNum = 0
        for i in range(0, len(arr), 2):
            if(arr[i] > arr[i+1]):
                highNum = arr[i]
            elif (arr[i] == arr[i+1]):
                highNum = arr[i]
            else:
                highNum = arr[i+1]
            secondArray.append(highNum)
            highNum = 0;
        print("Your new array has a length of", len(secondArray))
        return secondArray
    
myOgArray = [5,2,3,2,1,4]
print("Your OG array is", myOgArray)
print(values_greater_than_second(myOgArray), "\n\n")


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(theLength, theValue):
    length_and_value_array = []
    for i in range(0, theLength):
        length_and_value_array.append(theValue) 
    return length_and_value_array

print(length_and_value(4,7))
print(length_and_value(6,2))




