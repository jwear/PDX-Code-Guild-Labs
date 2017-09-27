"""

>>> arb(1, 2, 3, 4, 5, True, None, False, 'Python')
The 9 args are: (1, 2, 3, 4, 5, True, None, False, 'Python')

>>> arb(1, None)
The 2 args are: (1, None)

>>> stats(1, 67, 88, 44, 55, 33, 44, 22, 55, 7, 88, 9, 55, 66, 44, 33, 876)
Sum: 1587
Max: 876
Min: 1
Avg: 93
Range: 875
Entries: 17

"""
# Returns the number of arguments
def arb(*args):
    count_args = len(args)
    print('The {} args are: {}'.format(count_args, args))

# Returns the sum, max, min, average, ranges, and total entries of the arguments
def stats(*args):
    sum_args = sum(args)
    print('Sum: {}'.format(sum_args))
    max_args = max(args)
    print('Max: {}'.format(max_args))
    min_args = min(args)
    print('Min: {}'.format(min_args))
    avg_args = int(sum_args / len(args))
    print('Avg: {}'.format(avg_args))
    range_args = max_args - min_args
    print('Range: {}'.format(range_args))
    print('Entries: {}'.format(len(args)))
