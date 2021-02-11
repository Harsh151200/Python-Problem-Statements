# Problem Statement
# Q15. Write a program that prints a multiplication table for numbers up to 12.

for a in range(1,13):
    print("\n---------------------Table of ",a,"---------------------------")
    for b in range(1,13):
        print(a, 'x', b, '=', a * b)