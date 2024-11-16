'''
Write a program that takes two numbers as input, casts them to integers, and displays their sum.
'''

a=input("ENTER THE  A NUMBER:")
b=input("ENTER THE B NUMBER:")
if a.isdigit() and b.isdigit():
    print("The sum of the two numbers is: ",int(a)+int(b))
else:
    print("INVALID SELECTION")