# Problem Statement
# Q6. Sum of all odd numbers between 1 to n excluding n

n = int(input("Enter a number: "))
sum = 0
for i in range(1,n): #if Sum of all odd numbers between 1 to n excluding n use range(1,n+1)
    if i%2 == 0:
        sum += i
print("Sum : ",sum)
