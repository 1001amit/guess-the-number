import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("welcome to the guess number game")
    print("I have chosen a number between 1 to 100")

    while True:
        user_guess= input("Enter your guess: ")

        try:
            user_guess= int(user_guess)
        except ValueError:
            print("Please Enter a valid number")
            continue

        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number correct.")
            print(f"you guess the number in {attempts} attempts")
            break

guess_the_number()
