# Problem Statement:
# Q1. Find sum of first and last digit of a number
# UseCase - input : 12354 ; output : 5

n = input("Enter a number: ")

print("Addition of {} and {} is {}".format(n[0], n[-1], (int(n[0]) + int(n[-1]))))
