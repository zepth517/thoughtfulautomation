from enum import Enum
import os
import sys

R_VOLUME = 1000000
R_DIMENSIONS = 150
R_MASS = 20

def sort(width, height, length, mass):

    _volume = 0
    _dimensions = 0
    _mass = 0
    _bulky = False
    _heavy = False

    _volume = width * height * length
    _dimensions = width + height + length
    _mass = mass
    
    if _volume >= R_VOLUME or _dimensions >= R_DIMENSIONS:
        _bulky = True

    if _mass >= R_MASS:
        _heavy = True

    if _bulky and _heavy:
        return "REJECTED"

    if not _bulky and not _heavy:
        return "STANDARD"
    
    if _bulky or _heavy:
        return "SPECIAL"


if __name__ == "__main__":
    # print(sort(10, 10, 100000000, 10))
    # print(sort(10, 10, 100000000, 25))
    # print(sort(10, 10, 10, 25))
    # print(sort(10, 10, 10, 10))

    if len(sys.argv) == 5:
        
        width = sys.argv[1]
        height = sys.argv[2]
        length = sys.argv[3]
        mass = sys.argv[4]


        if width.isnumeric() and height.isnumeric() and length.isnumeric() and mass.isnumeric():
            print(sort(float(width), float(height), float(length), float(mass)))
        else:
            print('please enter the correct inputs: python sort.py width height length mass')

    else:
        print('please enter the correct inputs: python sort.py width height length mass')
