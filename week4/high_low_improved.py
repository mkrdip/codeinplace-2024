# https://docs.python.org/3/library/random.html
import random


# Constants
NUM_ROUNDS = 3


def generate_random_number():
    """Generates and returns a random number between 1 and 100."""
    return random.randint(1, 100)


def get_user_choice():
    """Prompts user to guess if their number is higher or lower than the computer's number."""
    choice = input("Do you think your number is higher or lower than the computer's?: ")
    while choice not in ["higher", "lower"]:
        choice = input("Please enter either 'higher' or 'lower': ")
    return choice


def compare_values(user_value, computer_value, user_choice):
    """
    Compares user's value against computer's based on the user's choice,
    and returns True if the user's guess is correct, otherwise False.
    """
    if (user_choice == "higher" and user_value > computer_value) or \
       (user_choice == "lower" and user_value < computer_value):
        return True
    return False


def main():
    # Strategic Pseudocode
    # Milestone 1: Initialize game and generate random numbers.
    # Milestone 2: Get user's guess.
    # Milestone 3: Compare user guess to actual values and update the score.
    # Milestone 4: Loop through the game rounds.
    # Milestone 5: Initialize user's score.
    # Extension 1: Safeguard user input
    # Extension 2: Conditional ending messages.

    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    my_score = 0  # Milestone 5

    for _ in range(NUM_ROUNDS):  # Milestone 4
        my_value = generate_random_number()  # Part of Milestone 1
        computer_value = generate_random_number()  # Part of Milestone 1
        print("Your number is", my_value)
        
        my_choice = get_user_choice()  # Milestone 2

        # Extension 1: Validation happens within get_user_choice()

        if compare_values(my_value, computer_value, my_choice):  # Milestone 3
            print("You are right! The computer's number was", computer_value)
            my_score += 1
        else:
            print("You are wrong! The computer's number was", computer_value)
        
        print("Your score is now", my_score)
        print('--------------------------------')

    # Extension 2: Conditional ending messages outside of the loop
    if my_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif my_score > NUM_ROUNDS / 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
