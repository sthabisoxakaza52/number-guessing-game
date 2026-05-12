import random


def number_guessing_game():

    secret_number = random.randint(1, 1000)
    max_guesses = 5
    guess_count = 0

    print("Welcome to the Number Guessing Game!")

    user_response = input(
        "Do you want to play the game? (yes/no): "
    ).lower().strip()

    if user_response != "yes":
        print("Okay, goodbye!")
        return

    print("\nI have chosen a number between 1 and 1000.")
    print(f"You have {max_guesses} guesses.\n")

    while guess_count < max_guesses:

        user_input = input(
            "Enter your guess (1 - 1000) or 'quit' to exit: "
        ).lower().strip()

        if user_input in ["quit", "exit"]:
            print(f"\nGame exited. The number was {secret_number}.")
            return

        if not user_input.isdigit():
            print("Please enter a valid number.\n")
            continue

        user_guess = int(user_input)
        guess_count += 1

        if user_guess > secret_number:
            print("Too High! Try Again.\n")

        elif user_guess < secret_number:
            print("Too Low! Try Again.\n")

        else:
            print(f"\nCorrect! You guessed the number in {guess_count} tries!")
            return

    print(f"\nYou ran out of guesses. The number was {secret_number}.")


number_guessing_game()