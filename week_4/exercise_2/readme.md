# Exercises for section 2

## Magic numbers
Rewrite this piece of code for calculating a ticket price for Hamlet so that it does not contain
magic numbers

```python
def calculate_ticket_price(age, seat_type):
    if age < 12:
        price = 10
    elif age < 60:
        price = 20
    else:
        price = 15

    if seat_type == "VIP":
        price += 30
    elif seat_type == "Balcony":
        price += 20
    elif seat_type == "Regular":
        price += 10
    
    return price
```

## Duplicate code

This code snippet can be used to determine if staff at the theatre should get a bonus or not
depending on the number of shows they have participated in. Your task is to restructure this
code and remove duplicate code. Perhaps we also smell a magic number here.

```python
def is_actor_eligible(performances):
    if performances > 20:
        return True
    return False

def is_director_eligible(performances):
    if performances > 20:
        return True
    return False

def is_technician_eligible(performances):
    if performances > 20:
        return True
    return False
```
In the example above, all roles, actor, director and technician, gets bonuses after 20 shows.
How could the code be rewritten to allow for different bonus thresholds?

## Long method

This function does a lot. It assigns roles, rehears scenes, and sets the stage. Rewrite this.
Create smaller functions responsible for each part, and call each function.

```python
def prepare_performance(actors, script, props):
    roles = script["roles"]
    cast = {}
    for role, actor in zip(roles, actors):
        cast[role] = actor
    print(f"Cast: {cast}")

    scenes = script["scenes"]
    for scene in scenes:
        print(f"Rehearsing scene: {scene}")
        for role, line in scene.items():
            print(f"{cast[role]} says: {line}")
    
    print("Setting the stage with props...")
    for prop in props:
        print(f"Placing prop: {prop}")
    
    print("Performance is ready!")
```

## Identify code smells

This code snippet contains some code smells. Try to identify them, and describe why they
are a problem. Suggest improvements.

```python
def process_reservation(user_type, tickets, show_date):
    if user_type == "celebrity":
        print("Celebrity access granted.")
        return "Celebrity processed"

    available_tickets = 50
    if tickets > available_tickets:
        print("Not enough tickets available.")
        return "Reservation failed"

    print(f"Reserving {tickets} tickets for {show_date}.")
    if show_date == "Friday" or show_date == "Saturday":
        print("Weekend show surcharge applied.")
        price = tickets * 15
    else:
        price = tickets * 10

    print(f"Total price is {price}.")
    return "Reservation successful"
```