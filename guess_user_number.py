import random


def guess(x):
    low = 1
    high = x
    answer = ''
    print(f"I'll guess between 1 and {x}")

    while answer != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low

        print(f"My guess is {computer_guess}")
        answer = input("correct(C), Too high(H), Too low(L):").lower()

        if answer == 'h':
            high = computer_guess - 1
        elif answer == 'l':
            low = computer_guess + 1

    print("I've successfully guessed your number!")


guess(100)
