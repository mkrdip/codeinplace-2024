"""
Program: Hospital Karel
Karel traverses 1st street from west to east, building hospitals
wherever it encounters a beeper.
"""
from karel.stanfordkarel import *


def main():
    while front_is_clear():
        move()
        if beepers_present():
            build_hostpital()

# building the hospital
def build_hostpital():
    pick_beeper()
    do_one_column()
    move()
    do_one_column()

# doing one column
def do_one_column():
    turn_left()
    put_three_beepers()
    move_to_base()
    turn_left()

# put three beepers using a loop but move only once
def put_three_beepers():
    for i in range(2):
        put_beeper()
        move()
    put_beeper()

# after putting beeper, come back to the base
def move_to_base():
    turn_left()
    turn_left()
    while front_is_clear():
        move()


if __name__ == '__main__':
    main()
