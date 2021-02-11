# Problem Statement
# Q2.swap first and last digits of any number.
n = list(input("Enter a number: "))
n[0], n[-1] = n[-1], n[0]
print(int(''.join(n)))
