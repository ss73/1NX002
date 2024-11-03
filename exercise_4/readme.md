# Exercises 4

## Class variable or instance variable

The class `LibraryBook` has an instance variable `late_fee`. The fee should be the same
for all library books and the `late_fee` variable could therefore be a class variable instead of an instance variable. Rewrite the class with `late_fee` as a class variable. 

Create a library book object to make sure that it is possible to calculate the fee.

```Python
class LibraryBook:

    def __init__(self, title, author, checked_out):
        # Instance variables for each book's specific information
        self.title = title
        self.author = author
        self.checked_out = checked_out
        self.late_fee = 5
    
    def calculate_late_fee(self, days_late):
        return days_late * self.late_fee
```

## String representation

Add a `__str__` and a `__repr__` method to the LibraryBook class. Remember that the
`__str__` method should look nice and the `__repr__` method should be detailed.

## Equal books

Implement the `__eq__` method for a LibraryBook. What should make two books equal?

## Some optional extra assignments

### Sorting books

`LibraryBook`'s are often sorted. Add sorting dunder methods to LibraryBook.

### Default list
Add a list of borrowers to the class. This could be a list of names of all library visitors who have borrowed this specific book.

Add the borrowers as a default argument in the `__init__` method set to `None`.

In the `__init__` method: Check if borrowers is `None`. If it is, set `self.borrowers = []`. Else set `self.borrowers = borrowers`.

Try this out by creating books with and without borrowers. Think about how you can make
sure this works as expected.

### Extra optional

Why not set the default argument to be an empty list?
