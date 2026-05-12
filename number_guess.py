import random

def number_guessing_game():
    """
    Play a number guessing game.

    The computer picks a random number between 1 and 100. 
    The player keeps guessing until they find the correct number.
    After each guess, the function prints feedback:
        - "Too high!" if the guess is larger than the target
        - "Too low!" if the guess is smaller than the target
        - "Correct!" if the guess matches the target
    """
    secret_number = random.randint(1,1000)

    print("  Welcome to the Number Guessing Game!  ")

    user_response = input("Do you want to play the game? (yes/no): ")
    user_response = user_response.lower()

    if user_response != "yes":
        print("Okay , goodbye!\n")
        exit()

    guess_count = 0

    while True:
        user_input = input("Enter your guess (1 - 1000)  or 'quit' to exit: ")

        if user_input.lower() == "quit":
            print(f"\nGame exited. The number was {secret_number}.")
            break

        try:
             user_guess = int(user_input)
        except ValueError:
             print("Enter a valid number or 'quit': ")
             continue

        guess_count += 1
        max_guesses = 5
    
        if user_guess > secret_number:
            print("Too High! Try Again.\n")
        elif user_guess < secret_number:
                print("Too Low! Try Again.\n")
        else:
            print("Correct!\n")
            break

        if guess_count == max_guesses:
             print(f"You ran out of guesses. The number was {secret_number}.")
             break
       
    print(f"You guessed the number in {guess_count} tries!\n")
number_guessing_game()            











