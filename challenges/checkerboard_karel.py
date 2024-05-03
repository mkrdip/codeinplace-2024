from karel.stanfordkarel import *

"""
  Get Karel to create a checkerboard pattern of beepers inside an empty rectangular world.
  Your code should work in any world size, e.g 3x1, 3x5, 6x6, 8x7.
  Note: Karel should end up where she starts.
  Link to the Challenge: https://codeinplace.stanford.edu/cip4/ide/a/checkerboard
"""

def main():
    fill_odd_row()  # Fill the first row starting with a beeper at the first position
    while left_is_clear():  # Continue if there is another row above
        move_up()  # Move up to the next row
        fill_even_row()  # Fill the row starting with a space
        if left_is_clear():  # Check again if there is yet another row above
            move_up()  # Move up
            fill_odd_row()  # Fill the row starting with a beeper
    return_to_base()


def fill_odd_row():
    """ Fills a row starting with a beeper in the first position. """
    put_beeper()  # Place a beeper at the first position
    while front_is_clear():
        move()
        if front_is_clear():  # Check if there's enough space for another beeper
            move()
            put_beeper()  # Place another beeper
    move_to_row_start()  # Move back to the start of the row


def fill_even_row():
    """ Fills a row skipping a beeper in the first position. """
    if front_is_clear():
        move()
        put_beeper()  # Place a beeper if there's space
    while front_is_clear():
        move()
        if front_is_clear():  # Check if there's enough space for another beeper
            move()
            put_beeper()  # Place another beeper
    move_to_row_start()  # Move back to the start of the row


def move_to_row_start():
    """ Moves Karel to the start of the row facing East. """
    turn_around()  # Turn around to face West
    while front_is_clear():
        move()  # Move until reaching the wall
    turn_around()  # Turn back to face East


def move_up():
    """ Moves Karel up to the next row if possible, starting from the west-most corner. """
    turn_left()  # Turn to face North
    if front_is_clear():
        move()  # Move up if there's space
        turn_right()  # Turn to face East


def turn_right():
    """ Turns Karel right using three left turns. """
    for _ in range(3):
        turn_left()  # Perform three left turns to turn right


def turn_around():
    """ Turns Karel around 180 degrees. """
    turn_left()  # Perform two left turns to turn around
    turn_left()


def return_to_base():
    # Move Karel back to the starting position
    if left_is_blocked():  # Check if Karel is at the left edge
        turn_right()  # Turn right to start moving towards the base
        while front_is_clear():
            move()  # Move towards the base
    turn_left()  # Face East before finishing


if __name__ == "__main__":
    main()
