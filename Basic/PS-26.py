# Problem Statement
"""Q.26 Implement the 'Guess the number' game in Python. You will first set a particular integer as the final answer,
and then ask the user to guess the number by taking his input. If the guess of the user is less than the final answer,
print 'Your guess was less than the answer' and take input from the user again. Similarly, do the same if the guess is
greater than the answer.
If the guess is correct, print 'your guess is correct' and stop the program.
Your program should keep on asking the user for his guess as long as he doesnt get the guess right."""

def guess_the_number(n):
    guess = int(input("Enter your guess :"))
    while True:
        if guess > n:
            print("Guess is Greater than expected!!")
            guess = int(input("Enter your guess :"))
        elif guess < n :
            print("Guess is Lesser than expected!!")
            guess = int(input("Enter your guess :"))
        else:
            print("Your guess was correct!!")
            break

guess_the_number(52)

