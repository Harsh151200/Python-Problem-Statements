# Problem Statement
# Q8. Print multiplication table and ask range from user

a, b = int(input("Which multiplicand value : ")), int(input("Enter final multiplier value :"))
for i in range(b + 1):
    print(a, 'x', i, '=', a * i)
