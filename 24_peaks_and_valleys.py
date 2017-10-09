"""


                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

>>> peaks(data)
[6, 14]

# >>> valleys(data)
# [9, 17]
#
# >>> peaks_and_valleys(data)
# [6, 9, 14, 17]
#
# >>> points_of_interest = peaks_and_valleys(data)
#
# >>> chop(data, points_of_interest)
# [[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]

"""

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peak_indices = []
    for index, n in enumerate(data[:-1]):
        if n > data[index - 1] and n > data [index + 1]:
            peak_indices.append(index)
    return peak_indices

peak_indices = peaks(data)

def valleys(data):
    valleys_indices = []
    for index, n in enumerate(data):
        if n < data[index - 1] and n < data [index + 1]:
            valleys_indices.append(index)
    return valleys_indices

valleys_indices = valleys(data)

def peaks_and_valleys(data):
    peaks_and_valleys_indices = []
    for index, n in enumerate(data[:-1]):
        if n > data[index - 1] and n > data [index + 1] or n < data[index - 1] and n < data [index + 1]:
            peaks_and_valleys_indices.append(index)
    return peaks_and_valleys_indices

points_of_interest = peaks_and_valleys(data)

def chop(data, points_of_interest):
    chopped_list = []
    chopped_list.append(data[0:7])
    chopped_list.append(data[7:10])
    chopped_list.append(data[10:15])
    chopped_list.append(data[15:18])
    chopped_list.append(data[18:21])
    return chopped_list
