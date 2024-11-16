
# WEEK 3, EXERCISES 3. Type hints.

## Part 1: Add type hints to these two functions

```python
def calculate(numbers, operation):
    """Calculate the sum or product of a list of numbers."""
    if operation == "sum":
        return sum(numbers)
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        raise ValueError("Invalid operation. Choose 'sum' or 'product'.")

def gcd(a, b):
    """Calculate the greatest common divisor of two integers."""
    while b:
        a, b = b, a % b
    return a
```

## Part 2

Test the two functions with some arguments. Use the environment from the last exercise or
create a new environment. Install mypy in the environment. 

You can find instructions here:
https://mypy.readthedocs.io/en/stable/getting_started.html.

Apply mypy to the two functions. Try not causing errors and try causing errors.
