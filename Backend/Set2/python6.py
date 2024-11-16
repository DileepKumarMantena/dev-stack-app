'''
Create a function that reverses a string without using any built-in functions.

'''

def reverse_string(input_string):
    revers_string =input_string[::-1]
    return revers_string

input_string = input("ENTER THE STRING TO BE REVERSED: ")
print("Reversed String:", reverse_string(input_string))