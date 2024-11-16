# Docstring style guide
Based on :
https://numpydoc.readthedocs.io/en/latest/format.html

## Method and function docstring format:

```python
"""One line summary without variable or function names.

Optional extended description clarifying functionality.

Parameters
----------
name : type
    Description of `name`

param_with_default : bool, default True
    Specify default argument values

Do not include `self` in method docstring.

Returns
-------
return_type
    Description of the returned value.

Raises
--------
ExceptionType
    Description of condition for raising exception
"""
```

## Class docstring format:

```python
"""One line summary.
Optional extended description. If the class is a subclass, its
relationship with the superclass should be described.

Attributes
---------------
List attributes in the same format as for method parameters.
Attributes are the attributes of the class itself.

Parameters
----------
List attributes in the same format as for method parameters. Parameters
are the parameters for the __init__ method. Exclude `self` from the
parameters.
"""
```
One line summaries should be full sentences.
