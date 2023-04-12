import random


def guess(x):
    random_number = random.randint(1, x)
    number = 0
    print(f"Guess the number between 1 and {x}")
    while number != random_number:
        number = int(input("Enter:"))

        if random_number > number:
            print("Guess again it's higher")
        elif random_number < number:
            print("Guess again it's lower")
    print(f"You have successfully guessed the number {random_number}!")


guess(10)
