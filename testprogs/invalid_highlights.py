""" Demonstrates cases where the nodes do not have increasing line:col positions whlie
    walking the tree depth first.

    See: https://github.com/titusjan/astviewer/issues/1
"""

# Dictionaries
d = {'one': 1, "two": 2}

# Function with defaults
def f(one=1, two=2):
    pass

# Inline test
a = 5 if True else 6

