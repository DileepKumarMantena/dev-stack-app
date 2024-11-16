'''
Write a function that takes a list of numbers and returns the largest number.

'''
def find_largest_number(numbers):
    return max(numbers),min(numbers)

list=find_largest_number([5,7,8,2,5])
print(list)