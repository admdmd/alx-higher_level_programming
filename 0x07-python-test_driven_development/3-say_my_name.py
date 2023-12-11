#!/usr/bin/python3
"""function that prints first and last name."""

def say_my_name(first_name, last_name=""):
    """print a name.
       
    Args:
         first_name (str): the first name to print.
         last name (str): the last name to print.
    Raises:
         TypeError: If either of first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
