from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    paint_building_one()
    move_to_next_building()
    paint_building_two()
    move_to_next_building()
    paint_building_three()


def paint_building_one():
    paint_north_side()
    paint_west_side()
    paint_south_side()


def paint_north_side():
    while left_is_blocked():
        put_beeper()
        move()


def paint_west_side():
    if facing_west():
        turn_left()

    else:
        turn_right()


def turn_right():
    for i in range (3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
