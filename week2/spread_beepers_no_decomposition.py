from karel.stanfordkarel import *

"""
Each row starts in front of a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. How can you solve this puzzle?
"""


def main():
    move() # go to the second column
    while beepers_present(): # when a beeper is present
        pick_beeper() # pick one beeper
        if beepers_present(): # second check if there is a beeper in the second column
            while beepers_present(): # keep moving while there is a beeper
                move()
            put_beeper() # when there is no beeper put one
            for i in range(2): # turn around
                turn_left()
            while front_is_clear(): # going east move until the wall 
                move()
            for i in range(2): # turn back to so it's ready to from east to west
                turn_left()
            move() # move to the second column
    put_beeper() # final beeper
    for i in range(2): # turn around towards east
        turn_left()
    move() # move to the first column
    for i in range(2): # back to original
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
