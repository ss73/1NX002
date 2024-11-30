import unittest

class TestAsserts(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(3, 2+1)

    def test_subtraction(self):
        # TASK 1
        # add a test case testing subtraction
        # use self.assertEqual
        self.assertEqual(1, 2-1)
        pass

    # TASK 2
    # add a test case (a method with a name starting with test_)
    # and use self.assertIn to test if a number appears in a list of numbers
    # try both passing and failing the test
    def test_member(self):
        self.assertIn(1, [3, 2, 0, 1, 5])
        self.assertNotIn(1, [3, 2, 0, "1", 5])
        # Uncomment the line below to fail a test
        # self.assertNotIn(1, [3, 2, 0, 1, 5])

    # TASK 3
    # write additional test cases using other asserts
    # check the documentation for inspiration:
    # https://docs.python.org/3/library/unittest.html

    def test_exceptions(self):
        self.assertRaises(TypeError, lambda: 1+"2")
        self.assertRaises(KeyError, lambda: {}[1])

    def test_instance(self):
        self.assertIsInstance(ValueError(), Exception)

    def test_misc(self):
        EMAIL_REGEX = '^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$'
        self.assertAlmostEqual(1.00000001, 1)
        self.assertRegex('name@example.com', EMAIL_REGEX)
        self.assertNotRegex('name@host', EMAIL_REGEX)
        self.assertNotRegex('%4ea%4de@example.de', EMAIL_REGEX)

    if __name__ == "__main__":
        unittest.main()