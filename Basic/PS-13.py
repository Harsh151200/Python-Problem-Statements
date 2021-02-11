# Problem Statement
# Q13. Write a program that prints the next 20 leap years.
#A leap year is exactly divisible by 4 except for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400. For example:
# 2017 is not a leap year
# 1900 is a not leap year
# 2012 is a leap year
# 2000 is a leap year
from datetime import date

# date object of today's date
current_year = int(date.today().year)
print("Current Year is : ",current_year)
print("Series of next leap year is as follows: ")
count = 0
while True:
    current_year += 1
    if (current_year%4 == 0 and current_year%100 != 0) or (current_year%400 == 0):
        print(current_year)
        count += 1
    if count == 20:
        break
