import random

NUM_ROUNDS = 3

# milestone 1
# create variables
# my value, computer value 
# use random library
# print them

# milestone 2
# take an input from the user in a variable

# milestone 3
# if something and and something

# milestone 4
# use a for loop

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # milestone 5
    my_score = 0

    # milestone 4
    for i in range(NUM_ROUNDS):
        # milestone 1
        computer_value = random.randint(1, 100)
        my_value = random.randint(1, 100)
        print("Your number is", my_value)

        # milestone 2
        my_choice = input("Do you think your number is higher or lower than the computer's?: ")

        # extension 1
        while my_choice != "higher" and my_choice != "lower":
            my_choice = input("Please enter either higher or lower: ")

        if my_choice == "higher" and my_value > computer_value:
            print("You are right! The computer's number was", computer_value)
            my_score = my_score + 1
            # we can write it like this as well
            # my_score += 1
        elif my_choice == "lower" and my_value < computer_value:
            print("You are right! The computer's number was", computer_value)
            my_score = my_score + 1
        else:
            print("You are wrong! The computer's number was", computer_value)
            
        print("Your score is now", my_score)
        print('--------------------------------')


    if my_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif my_score > NUM_ROUNDS / 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
