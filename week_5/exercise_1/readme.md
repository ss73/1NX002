# Exercises TEST lecture 1

The goal of this exercise is to get started with unit testing in Python.

## Part 1
Start by running the code below in you IDE or in a terminal using python -m unittest -v

## Part 2
Do the three tasks listed in the code.

```python
import unittest

class TestAsserts(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(3, 2+1)

    def test_subtraction(self):
        # TASK 1
        # add a test case testing subtraction
        # use self.assertEqual
        pass

    # TASK 2
    # add a test case (a method with a name starting with test_)
    # and use self.assertIn to test if a number appears in a list of numbers
    # try both passing and failing the test

    # TASK 3
    # write additional test cases using other asserts
    # check the documentation for inspiration:
    # https://docs.python.org/3/library/unittest.html

if __name__ == "__main__":
unittest.main()
```

## Notes
Configure tests in Visual Studio Code: 
* Press CMD+SHIFT+P
* Type or select `Python: Configure Tests`
* Select `unittest`
* Select `. Root directory`
* Select `test_*.py`

If there is an error output relating to loading `pytest`, try reloading the editor

### Running from the command line
Run the unittest module: `python -m unittest test_asserts`