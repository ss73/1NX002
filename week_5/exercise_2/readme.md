# Exercises for TEST, lecture 2-3

## Part 1
Chapter 8 in the course book describes a number of Python gotchas.
https://inventwithpython.com/beyond/chapter8.html

Read through the section named _Don’t Copy Mutable Values Without copy.copy() and copy.deepcopy()_

This section (and the last video) describes how to copy mutable values.

Write test cases confirming the difference between copying mutable values (values that can
change) such as lists, and values that are not mutable, such as strings and integers. Make
sure that you see the difference (the resulting value of a) when doing:
```python
 a = 5
 b = a
 b = 8
```
and
```python
a = [5]
b = a
b[0] = 8
```
Note that the id() function can be used to check the identity of an object.

## Part 2
Write tests for confirming the behaviour of `deepcopy` which is described in the same
section. Make sure that you understand the difference between `copy` and `deepcopy`

## Part 3
Write additional test cases for some of the other gotchas described in chapter 8.