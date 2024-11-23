# Exercises for section 1

## Dataclasses

Complete this data class for representing theatrical lighting fixtures, such as spotlights and
floodlights.

```python
from dataclasses import dataclass

@dataclass
class LightingEquipment:
    """
    Represents a piece of lighting equipment in a Play.
    """
    # Attributes:
    # - name: str - The name of the lighting equipment (e.g., "Spotlight").
    # - wattage: int - The power consumption of the equipment in watts.
    # - is_led: bool - Whether the equipment is LED (True for LED, False otherwise).
```
Create som objects of this class and check their string representation

### Add a method

Add a method for calculating power consumption in kilowatt-hours to the class with hours as
a parameter.

The calculation: ```(wattage/1000)*hours```

### Look at the docs

Browse the dataclasses documentation: https://docs.python.org/3/library/dataclasses.html

### Write your own dataclass

Challenge: Write a data class that can be sorted and confirm that it works.

## Properties

The class below represents a costume for an actor in a Play. It has a `color` property for
setting and getting the costumes color.

Add a property for the period of the costume. As for the color property, add the property itself
and a setter. 
* The getter returns the `_period` attribute. 
* The setter should validate that an incoming value for the costumes period should be one of the following: `["Victorian", "Modern", "Renaissance", "Futuristic"]`

```python
class Costume:
    """
    Represents a costume for an actor in a play.
    """
    def __init__(self, color: str, period: str):
        self._color = color
        self._period = period

    @property
    def color(self) -> str:
        """
        Returns the color of the costume.
        """
        return self._color

    @color.setter
    def color(self, value: str):
        if not value:
            raise ValueError("Color must be a non-empty string.")
        self._color = value
```
Create a couple of Costume objects and make sure the properties work as expected.