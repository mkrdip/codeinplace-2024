from karel.stanfordkarel import *


"""
Bonus: Do it for unlimited number of rows
Each row starts in front of a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. How can you solve this puzzle?
"""

"""
Strategy
move karel
while there is a beeper
    pick_beeper()
    move karel 
    put_beeper()
    turn_around (left turn twice)
    while front is clear keep moving
    turn_around (left turn twice)
"""

def main():
    move() # move to next column
    do_one_row()
    # post condition
    fix_fence_post()
    turn_left()
    while front_is_clear():
        move()
        turn_right()
        move()
        do_one_row()
        fix_fence_post()
        turn_left()
    turn_around()
    move_to_wall()
    turn_left()


def do_one_row():
    while beepers_present(): 
        pick_beeper() # pick one beeper
        if beepers_present(): # when there is any beeper present
            move_to_last_beeper()
            put_beeper() # putting beeper in blank
            back_to_base()
            move()



def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_to_last_beeper():
    while beepers_present():
        move()


def fix_fence_post():
    put_beeper()
    back_to_base()


def back_to_base():
    turn_around()
    move_to_wall()
    turn_around()


def turn_around():
    for i in range(2):
        turn_left()


def move_to_wall():
    while front_is_clear():
        move()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
