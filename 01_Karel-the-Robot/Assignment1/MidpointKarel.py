from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    create_beeper_X()
    remove_one_beeper_everywhere()
    # find_remaining_middle_beeper()
    # remove_middle_beeper_goto_bottom()
    # put_beeper()


#pre: Karel is in SW corner (bottom row) facing east; world is empty
#post: Karel is in NW corner (top row) facing east; world has an "X" of beepers with 2 in middle position
def create_beeper_X():
    diagonal_to_NE()
    go_to_SE_corner()
    diagonal_to_NW()


#pre: Karel is in NW corner (top row) facing east; world has an "X" of beepers with 2 in middle position
#post: Karel is in the NE corner (top row) facing east; world has only 1 beeper in the world located
# in the middle position
def remove_one_beeper_everywhere():
    while front_is_clear():
        clear_column_beeper()
        do_180()
        return_to_start()
        move()
    clear_column_beeper()
    do_180()
    return_to_start()

#pre:
#post:
def clear_column_beeper():
    while front_is_clear():
        turn_right()
        while front_is_clear():
            safe_pick()
            move()
        safe_pick()


def return_to_start():
    while front_is_clear():
        move()
    do_180()
    turn_left()


def diagonal_to_NE():
    while front_is_clear():
        put_beeper()
        move()
        turn_left()
        move()
        turn_right()
    put_beeper()


def go_to_SE_corner():
    turn_right()
    while front_is_clear():
        move()
    turn_right()


def diagonal_to_NW():
    while front_is_clear():
        put_beeper()
        move()
        turn_right()
        move()
        turn_left()
    put_beeper()
    do_180()


def safe_pick():
    if beepers_present():
        pick_beeper()


# pre: facing original direction
# post: facing opposite direction (i.e., 180 degree turn)
def do_180():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
