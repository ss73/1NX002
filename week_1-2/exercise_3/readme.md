# EXERCISES 3

## HAS-A

The `Person` class from the last exercise wants a pet. Write a `Pet` class and add it as an attribute to the Person class. A pet could perhaps have a name, a favourite food and be able to do a trick. Add a method `describe_pet` to the `Person` class. This method returns a description of a persons pet. The `describe_pet` method can call a `get_info method` in the `Pet` class to get accurate information about the pet.

Create some pet and person objects and call the method `describe_pet` to make sure
everything works.

## IS-A

Add a couple of subclasses to the Pet class inheriting from `Pet`. The subclasses should
have some attributes and methods extending the characteristics of `Pet`. Create some
objects now as well. Create a person object with a subclass-pet.

## OVERRIDING METHODS

When a method exists in a superclass but not in a subclass inheriting from the superclass, the subclass inherits the method from the superclass. But it is possible for a subclass to override a method in a superclass by implementing its own version of the method. If an overridden method is called using an object of the subclass, the implementation in the subclass will be executed, and not the implementation in the superclass.

For example, if the superclass `Pet` has a method `do_trick` , one or more of its subclasses can override the method.

Try this out.

## PROGRAMMING PRINCIPLES

Explain the Liskov substitution principle to an old friend or house plant.
