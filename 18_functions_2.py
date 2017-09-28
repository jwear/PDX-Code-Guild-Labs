"""

>>> combine(7, 4)
11

>>> combine(42)
42

>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

>>> choose_longest("Greg", "Rooney")
'Rooney'

>>> choose_longest("Greg", "Rooney", "Philip", "Maximus", "Gabrielle")
'Gabrielle'

>>> choose_longest("Greg", [0, 0, 0, 0, 4])
[0, 0, 0, 0, 4]

"""

# Return the Sum of two or less elements using a default argument of zero.
def combine(*args, elements=0):
    if len(args) <= 2:
        sum_args = sum(args)
        return sum_args

# Return the sum of any number of integers passed using *args.
def combine_many(*args):
    sum_args = sum(args)
    return sum_args

# Return the longest input argument.
def choose_longest(*args):
    return max(args, key=len)
