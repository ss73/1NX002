# Exercises 2

## Add attributeas to a class

This class represents a person. Add a couple of attributes to the class, and instantiate some
objects of the class with these new attributes. The attributes should be printed in the
`display_info` method.

```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person = Person("Alice", 30)
person.display_info()
```

## Add a method to a class

Add a method called increase_age to the class. The method should age the person by one
year. Create a person object and age it.

## Write your own class

Look around you to find some object. What attributes describe this object? What functionality
does it have? Write a class representing the object. The class should have an
`__init__` method, with self as the first parameter, and at least one other method. Try first
to do it without looking at the class example above, and without getting hints from an IDE.

## Instantiate objects

Create some objects of the class you just wrote, and call its method(s).

## Write another class

Practice makes perfekt. Repeat the two steps: write a class, create som objects, do
something with the objects.