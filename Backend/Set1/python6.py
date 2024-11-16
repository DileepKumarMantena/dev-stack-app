'''

Write a program to print a multiplication table for a given number up to 10
'''

number=int(input("Enter a number for the multipication table:"))

for i in range(1,11):
    print(number,"*",i,"=",number*i)