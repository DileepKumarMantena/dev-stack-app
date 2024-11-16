'''
Create a program that converts a given number of days into years, weeks, and days.
The program should take the number of days as input and output the equivalent years, weeks, and days
'''

def converting_days_into_years(total_days):
    years = total_days // 365
    remaining_days = total_days % 365
    weeks = remaining_days // 7
    days = remaining_days % 7
    
    return years, weeks, days

total_days=int(input("ENTER THE TOTAL DAYS:"))
years, weeks, days=converting_days_into_years(total_days)
print(f"{total_days} days is equivalent to {years} years, {weeks} weeks, and {days} days.")