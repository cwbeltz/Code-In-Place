from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


# pre: beginning at the bottom/south end of column 1, facing east.
# post: ending at the bottom/south end of furthest column, facing east.
def main():
    while front_is_clear():
        repair_column()
        move_to_next_column()
    repair_column()


#pre: at bottom of un-repaired column, facing east
#post: at bottom of REPAIRED column, facing east
def repair_column():
    turn_left()
    while front_is_clear():
        repair_stone()
        move()
    repair_stone()
    do_180()
    return_to_column_bottom()
    turn_left()


#pre: at bottom of column facing east
#post: at bottom of next column facing east
def move_to_next_column():
    if front_is_clear():
        for i in range(4):
            move()


#pre: in a space either with or without a beeper
#post: in a space with a beeper
def repair_stone():
    if no_beepers_present():
        put_beeper()

#pre: facing original direction
#post: facing opposite direction (i.e., 180 degree turn)
def do_180():
    for i in range(2):
        turn_left()

#pre: at top/north end of column, facing south
#post: at bottom/south end of column, facing south
def return_to_column_bottom():
    while front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
