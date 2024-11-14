'''
Write a program that calculates the area of a circle given the radius.

pi r2
'''

pi_value=3.14159
radius=int(input(("Enter radius value:")))
area_of_circle=pi_value*(radius*radius)
print(f"The Area of the Circle is:{round(area_of_circle)}")