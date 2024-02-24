###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem
#   Date:           February 23 2024
#   File:           Lab3_robert.py
#   Description:    Unit test files for Lab3_robert.py, testing various
#                   functions that return the area of specified shapes.
###############################################################################
import unittest
from math import *
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

# --NOTE REGARDING EXPECTED FAILURES--
# Expected failures are caused by recommended test case for imaginary numbers throwing an error
# before the assertRaises can consume it. Since the domain error is thrown in the execution of parameters passed
# to the function, the function does not have an opportunity to return or throw an exception itself, causing
# the assertRaises to fail.

# Circle Cases
class TestCircleArea(unittest.TestCase):
    def test_circle_01(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(5), 25 * pi)

    def test_circle_02(self):
        self.assertEqual(circle_area(-1), pi)

    @unittest.expectedFailure
    def test_circle_03(self):
        self.assertRaises(circle_area(sqrt(-1)), ValueError)
        self.assertRaises(circle_area(True), TypeError)
        self.assertRaises(circle_area("radius"), TypeError)


# Ellipse Cases
class TestEllipseArea(unittest.TestCase):
    def test_ellipse_04(self):
        self.assertEqual(ellipse_area(-1, -1), pi)
        self.assertEqual(ellipse_area(-1, 1), -1 * pi)

    def test_ellipse_05(self):
        self.assertEqual(ellipse_area(0, 1), 0)
        self.assertEqual(ellipse_area(1, 1), pi)
        self.assertEqual(ellipse_area(2, 5), 10 * pi)

    @unittest.expectedFailure
    def test_ellipse_06(self):
        self.assertRaises(ellipse_area(sqrt(-1), 1), ValueError)
        self.assertRaises(ellipse_area(True, 1), TypeError)
        self.assertRaises(ellipse_area("major", 1), TypeError)


# Trapezium Cases
class TestTrapeziumArea(unittest.TestCase):
    def test_trapezium_07(self):
        self.assertEqual(trapezium_area(-1, -1, -1), 1)
        self.assertEqual(trapezium_area(-1, -1, 1), -1)
        self.assertEqual(trapezium_area(-1, 1, 1), 0)

    def test_trapezium_08(self):
        self.assertEqual(trapezium_area(0, 1, 1), 0.5)
        self.assertEqual(trapezium_area(1, 1, 1), 1)
        self.assertEqual(trapezium_area(2, 3, 4), 10)

    @unittest.expectedFailure
    def test_trapezium_09(self):
        self.assertRaises(trapezium_area(sqrt(-1), 1, 1), ValueError)
        self.assertRaises(trapezium_area(True, 1, 1), TypeError)
        self.assertRaises(trapezium_area("value", 1, 1), TypeError)


# Rho,mbus Cases
class TestRhombusArea(unittest.TestCase):
    def test_rhombus_10(self):
        self.assertEqual(rhombus_area(-1, -1), 0.5)
        self.assertEqual(rhombus_area(-1, 1), -0.5)

    def test_rhombus_11(self):
        self.assertEqual(rhombus_area(0, 1), 0)
        self.assertEqual(rhombus_area(1, 1), 0.5)
        self.assertEqual(rhombus_area(2, 3), 3)

    @unittest.expectedFailure
    def test_rhombus_12(self):
        self.assertRaises(rhombus_area(sqrt(-1), 1), ValueError)
        self.assertRaises(rhombus_area(True, 1), TypeError)
        self.assertRaises(rhombus_area("major", 1), TypeError)


# Test suite builder
def dynamic_suite(test_option):
    # Test loader vars
    tc_circle = unittest.TestLoader().loadTestsFromTestCase(TestCircleArea)
    tc_ellipse = unittest.TestLoader().loadTestsFromTestCase(TestEllipseArea)
    tc_trapezium = unittest.TestLoader().loadTestsFromTestCase(TestTrapeziumArea)
    tc_rhombus = unittest.TestLoader().loadTestsFromTestCase(TestRhombusArea)

    # Suite init
    return_suite = unittest.TestSuite()

    # Init return value
    # Switch statement based on selected option to build test suite
    match test_option:
        case "C":
            return_suite.addTest(tc_circle)

        case "E":
            return_suite.addTest(tc_ellipse)

        case "T":
            return_suite.addTest(tc_trapezium)

        case "R":
            return_suite.addTest(tc_rhombus)

    return return_suite


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
