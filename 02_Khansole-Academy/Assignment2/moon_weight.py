"""
File: moon_weight.py
--------------------
Add your comments here.
"""

MOON_MULTIPLE = 0.165 #this a GLOBAL CONSTANT

def main():
    earth_weight_str = input("Enter a weight on earth: ")

    #type casting
    earth_weight = float(earth_weight_str)

    #lhs = rhs
    # '=' assignment operator

    #moon_weight = 0.165 * earth_weight
    moon_weight = MOON_MULTIPLE * earth_weight

    print("Equivalent weight on moon: " + str(moon_weight)) #to concatenate, both sides need to be strings



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
