'''
Write a program that takes a number as input and checks if it’s odd or even.
'''


try:
    input_number=int(input("ENTER A NUMBER:"))
except Exception as e:
    print(f"Invalid input{e}")
else :
    match input_number%2==0:
        case True:
            print(f"Even Number{input_number}")
        case False:
            print(f"Odd Number{input_number}")
