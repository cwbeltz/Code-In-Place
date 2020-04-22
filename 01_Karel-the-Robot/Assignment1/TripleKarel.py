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


#pre: all three buildings are un-painted; Karel starts on the NE corner of building one
#post: all three buildings are painted on three sides; Karel is on the NW corner of building three
def main():
    paint_building_one()
    paint_building_two()
    paint_building_three()


#pre:building one is un-painted; Karel starts on the NE corner
#post: north, west, and south sides are painted on building one; Karel is on the SE corner
# of building one abutting building two
def paint_building_one():
    paint_and_move()
    turn_left()
    move()
    paint_and_move()
    turn_left()
    move()
    paint_and_move()


#pre: building two is un-painted; Karel starts on NW corner of building two
#post: west, south, and east sides of building two are painted; Karel is on the NE corner of building two
# abutting building three
def paint_building_two():
    turn_right()
    paint_and_move()
    turn_left()
    move()
    paint_and_move()
    turn_left()
    move()
    paint_and_move()


#pre: building three is un-painted; Karel stands on the SW corner of building three
#post: south, east, and north sides of building three are painted; Karel is on the NW corner of building three
def paint_building_three():
    turn_right()
    paint_and_move()
    turn_left()
    move()
    paint_and_move()
    turn_left()
    move()
    paint_and_move()


#pre: Karel is on the corner of a building with an un-painted wall on his left
#post: Karel is on the next corner of the building with a painted wall behind him
def paint_and_move():
    while left_is_blocked():
        put_beeper()
        move()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
