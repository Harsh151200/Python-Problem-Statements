# Problem Statement
# Q4. Check if a number is divisible by three or seven
n = int(input("enter a number:"))
if (n % 3 == 0) and (n % 7 == 0):
    print("The number is divisible by both three and seven")
else:
    print("The number is not divisible by three and seven")
