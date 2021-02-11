#Problem Statement:
#Q11. Take input from user as number (say n). Now find sum of all the numbers between 1-n,
#which are multiples of 3 and 5

n = int(input('Enter a the final range in number : '))
sum = 0
for i in range(n):
    if i%3 == 0 or i%5 == 0 :
        sum += i
print('The sum of numbers between 1 and {} and also which are divisible by 3 or 5 is {}'.format(n,sum))
