import random


def play():
    choice = input("Choose Rock(R), Paper(P), Scissors(S),: ").lower()
    c_choice = random.choice(["r", "p", "s"])
    if choice == c_choice:
        print(f"It's a tie!Both of us chose {choice}")
    else:
        result = win_lose(choice, c_choice)
        if result:
            print("You won!")
        elif not result:
            print("You lost!")
            print(f"I chose {c_choice}")


def win_lose(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (
            player == "p" and opponent == "r"):
        return True


def madlib():
    verb = input("Verb:")
    verb2 = input("Verb:")
    adjective = input("Adjective")
    adjective2 = input("Adjective")

    madlib = f"Last night I went to the store and bought a {adjective} ice cream cone.\n" \
             f" It was so {adjective2} that it made my mouth water! \n" \
             f"As I ate it, I thought about how much fun it would be to go on an adventure with my friends.\n" \
             f" We could {verb} new places, try out different activities, and {verb2} lots of delicious food.\n" \
             f" What a great way to spend the day!"
    print(madlib)


def guess1(x):
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


choice = 0
while True:

    print("Welcome to my game collection!")
    print("What would you like to do?")
    print("1. Play Madlibs")
    print("2. Play Guess the number!(Computer)")
    print("3. Play Guess the number!(User)")
    print("4. Play Rock, Paper, Scissors!")
    print("5. Exit")
    choice = int(input("Enter:"))

    if choice == 1:
        print("Welcome to Madlibs!")
        madlib()

    elif choice == 2:
        print("Guess the number!(Computer)")
        guess(10)

    elif choice == 3:
        print("Guess the number!(User)")
        guess1(100)

    elif choice == 4:
        print("Welcome to Rock Paper Scissors!")
        play()

    elif choice == 5:
        print("Thanks for using this, Bye!")
        break

    else:
        print("Error, invalid choice!")
