'''
Build a basic calculator that can perform addition, subtraction, multiplication, and division.
'''

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=input("Enter operator (+,-,*,/):")
match c:
    case "+":
        print(f"THE ADDITION IS {a+b}")
    case "-":
        print(f"THE SUBRACTION IS {a-b}")
    case "*":
        print(f"THE MULTIPLICATION{a*b}")
    case "/":
        print(f"THE DIVISION IS {a/b}")
    case _:
        print("Invalid operator") 