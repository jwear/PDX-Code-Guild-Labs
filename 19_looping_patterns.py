"""

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4

>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""

# Returns a with its index vertically
def display_indexes(a):
    for index, e in enumerate(a):
        print(e, index)

# Returns two lists paired vertically
def parallel(a, b):
    for a, b in zip(list(a), b):
        print(a, b)
