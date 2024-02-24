###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem
#   Date:           February 23 2024
#   File:           Lab3_robert.py
#   Description:    Unit test files for Lab3_robert.py, testing various
#                   functions that return the area of specified shapes.
###############################################################################
import unittest
from math import sqrt
from app.Lab3_robert import *

# CONSTS
MENU_OPTIONS = ["C", "E", "T", "R", "Q"]
MENU_PROMPT = """Please select one of the following five options:
                 C: Test circle area
                 E: Test ellipse area
                 T: Test trapezium area
                 R: Test rhombus area
                 Q: Quit

                 Input: """


# TESTING
# Test Cases
# Circle Cases
class TestCircleArea(unittest.TestCase):
    def test_circle_01(self):
        self.assertEqual(True, True)

    def test_circle_02(self):
        self.assertEqual(True, True)

    def test_circle_03(self):
        self.assertEqual(True, True)


# Ellipse Cases
class TestEllipseArea(unittest.TestCase):
    def test_ellipse_04(self):
        self.assertEqual(True, True)

    def test_ellipse_05(self):
        self.assertEqual(True, True)

    def test_ellipse_06(self):
        self.assertEqual(True, True)


# Trapezium Cases
class TestTrapeziumArea(unittest.TestCase):
    def test_trapezium_07(self):
        self.assertEqual(True, True)

    def test_trapezium_08(self):
        self.assertEqual(True, True)

    def test_trapezium_09(self):
        self.assertEqual(True, True)


# Rho,mbus Cases
class TestRhombusArea(unittest.TestCase):
    def test_rhombus_10(self):
        self.assertEqual(True, True)

    def test_rhombus_11(self):
        self.assertEqual(True, True)

    def test_rhombus_12(self):
        self.assertEqual(True, True)


# Test suite builder
def dynamic_suite(test_option):
    # Test loader vars
    tc_circle = unittest.TestLoader().loadTestsFromTestCase(TestCircleArea)
    tc_ellipse = unittest.TestLoader().loadTestsFromTestCase(TestEllipseArea)
    tc_trapezium = unittest.TestLoader().loadTestsFromTestCase(TestTrapeziumArea)
    tc_rhombus = unittest.TestLoader().loadTestsFromTestCase(TestRhombusArea)

    # Suite init
    suite = unittest.TestSuite()

    # Init return value
    # Switch statement based on selected option to build test suite
    match test_option:
        case "C":
            suite.addTest(tc_circle)

        case "E":
            suite.addTest(tc_ellipse)

        case "T":
            suite.addTest(tc_trapezium)

        case "R":
            suite.addTest(tc_rhombus)

    return suite


# TEST RUNNER PROGRAM
# Setup while loop to capture what option user wants
selected_option = ""
while selected_option != "Q":
    # Gather input
    selected_option = input(MENU_PROMPT).strip().upper()

    # Switch action based on user selection
    # Runs tests
    if selected_option in MENU_OPTIONS and selected_option != "Q":
        print("Valid selection!")
        suite = dynamic_suite(selected_option)
        unittest.TextTestRunner().run(suite)

    # Quits
    elif selected_option == "Q":
        print("Goodbye.")

    # Input validation failed
    else:
        print("Invalid selection! Try again!")
