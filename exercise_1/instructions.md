# EXCERCISES 1

## Improve the past
Have a look at some of your own previous Python code and try to make some
improvements. You could look for the following issues:

### NAMING
- Not following naming conventions
- Using unclear names

### FORMATTING
- Inconsistent layout and use of whitespace

### PYTHONIC CODE
- Not following conventions for Python code

## Naming
This class describes a Person. Try to improve the naming in this code snippet. The names
should follow naming conventions and be understandable.
```python
class person:
    def __init__(self, persons_name, a, addr):
        self.persons_name = persons_name
        self.a = a
        self.addr = addr
        self.age_when_old = 18

    def printStuff(self):
        print(f"Name: {self.persons_name}")
        print(f"Age: {self.a}")
        print(f"Lives at: {self.addr}")

    def update_address(self, new_addr):
        self.addr = new_addr
        print(f"{self.name}'s address updated to: {self.addr}")

    def adult(self):
        return self.a >= self.age_when_old

p1 = person("Alice", 25, "123 First Street")
p1.printStuff()
p2 = person("Bob", 7, "456 First Street")
```

## Loops etc
```python
apples = ["Golden delicious", "Fuji", "Honeycrisp", "Gala"]
# rewrite this loop using enumerate and set start index to 1
for i in range(len(apples)):
    print(f"Apple number {i} is: {apples[i]}")

order = ["First", "Second", "Third", "Fourth"]
apples = ["Golden delicious", "Fuji", "Honeycrisp", "Gala"]
pears = ["Bartlett", "Red Anjou", "Concorde", "Starkrimson"]

# combine a loop with zip and print a message regarding the apples, pears and their orderings
```
What happens if you zip two lists with different lengths?

Write a dict comprehension. Add the apples as keys and pears as values. A zip could be useful.

Here, apples are added to apple_over_pears if they fulfil the condition apple > pear.
Can you rewrite this loop as a list comprehension?

```python
apple_over_pear = []
for apple, pear in zip(apples, pears):
    if apple > pear:
        apple_over_pear.append(apple)
```
Is the loop or the comprehension more readable?

## Dicts

`dict.get(key, default)` returns the value of key if key
is in the dict, otherwise it returns the default value.
`dict.setdefault(key, default)` returns the value of key
if key is in the dict, otherwise it adds the key with the default
value to the dict, and returns the default. Add and get some additional
fruits to/from the apples-pears dict using these methods.

🍎 Jonagold, Empire, Cortland

🍐 Seckel, Forell, Bosc

## Simplify these simple statements

Simplify the redundant comparisons in this code snippet
```python
some_numbers = {1, 2, 3}
x = 5
result = x != 1 and x != 2 and x != 3

if result == False:
    a_list = [y for y in some_numbers if y % 3 == 2]
    if len(a_list) > 0:
        print("Some result is true, and som list has elements")
    else:
        print("No, the list is empty")
else:
    some_set = {1, 2, 3}
    difference = some_set - some_numbers
    if len(difference) == 0:
        x = 175 % 34 < 7
    else:
        x = 175 % 34 > 7
if x == True:
    print("who knew?")
```