# Problem Statement
"""
Q.36 Display number of tries in Guess the number game. Also refer problem 26(Q.26)
"""


def guess_the_number(n):
    guess = int(input("Enter your guess :"))
    count = 0
    while True:
        if guess > n:
            count += 1
            print("Number of tries : {}\n Guess is Greater than expected!!\n".format(count))
            guess = int(input("Enter your guess :"))
        elif guess < n :
            count += 1
            print("Number of tries : {}\n Guess is Lesser than expected!!\n".format(count))
            guess = int(input("Enter your guess :"))
        else:
            count += 1
            print("Your guess was correct after {} tries".format(count))
            break

guess_the_number(52)