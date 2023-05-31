"""This is an example Python module.

Python module is a text file with the .py extension. It contains Python code.

main.py is a common name for the main Python module of a repository (an entry point) - the module the users are supposed
to execute.
"""
from utilities.math_utils import add_two_numbers
from pandas_example.read_fixed_width_table import main as read_table


# define a function
def print_hi(name):
    """This function greets the provided name.

    :param name: str; name to greet
    """
    print(f'Hi, {name}')


# The content of the following if-clause is only executed if this module is the module directly executed by Python.
#  E.g. if we only imported the print_hi() function from this module, the content of this if-clause would not be
#  executed.
#
# The if-clause indicates that this Python module is intended to be used as a script - i.e. it is intended to be
#  directly executed. Other Python modules might not be intended for execution and might serve just as a library
#  of Python objects to be imported into other modules.
#
# Using the if __name__ == '__main__' clause is not compulsory, however, it is a good indication to the user of
#  your repository that this file is a script that can be executed.
#
# Some guides go even further and propose to wrap everything under __name__ == '__main__' into a main() function.
#  See more on this topic here: https://www.youtube.com/watch?v=g_wlZ9IhbTs
if __name__ == '__main__':
    print_hi('IL')
    b = add_two_numbers(2, 'asdf')
    c = read_table()
