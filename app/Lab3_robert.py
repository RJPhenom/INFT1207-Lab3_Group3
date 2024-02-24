###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem
#   Date:           February 23 2024
#   File:           Lab3_robert.py
#   Description:    App that calculates the area of various shapes.
###############################################################################
from math import pi


# Returns the area of a circle when provided the circle's radius
def circle_area(r: float):
    return pi * (r ** 2)


# Returns the area of an ellipse when provided its major and minor axes
def ellipse_area(major: float, minor: float):
    return pi * major * minor


# Returns the area of a trapezium when provided the length of its parallel sides and
# its height perpendicular
def trapezium_area(side_a: float, side_b: float, height: float):
    return 0.5 * (side_a + side_b) * height


# Returns the area of a rhombus when provided the length of a diagonal between opposite points
# and the length of the diagonal between its other two points
def rhombus_area(diagonal_a: float, diagonal_b: float):
    return diagonal_a * diagonal_b * 0.5

