# ------------------------------------------------------------------
# The list below is used for the two functions that follow
lst = [56, 57, 58, 59, 60]

# Reverse the input iterable and return it
def reverse(lst):
    lst.reverse()
    return lst

print(reverse(lst))


# Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
def maximum(lst):
    max_num = max(lst)
    first_number = int(str(max_num)[0])
    new_list = []
    for i in lst:
        if str(first_number) in str(i):
            new_list.append(max_num)
        else:
            new_list.append(i)
    return new_list

print(maximum(lst))


# ------------------------------------------------------------------
# The two lists below are used for several functions that follow

list3 = ['maine coon', 'Siamese', 'abyssinian', 'burmese', 'sphynx']
list4 = ['maine coon', 'somali', 'bengal', 'ragdoll', 'persian']

# Given two lists, return True of the first two items are the equal.
def compare_first_element(list3, list4):
    return list3[0] == list4[0]

print(list3)
print(list4)
print(compare_first_element(list3, list4))


# Return True if the first letter of the second element in each list is equal. (Case Insensitive)
def compare_second_word(list1, list2):
    return list1[1][0].lower() == list2[1][0].lower()

print(compare_second_word(list3, list4))


# Given two lists, return one list, with all of the items of the first list, then the second
def extend(list3, list4):
    list3.extend(list4)
    return list3

print(extend(list3, list4))


# Use a default argument to allow the user to reverse the order!
def combine_reverse(list3, list4):
    new_combined_reversed_list = list3 + list4
    new_combined_reversed_list.reverse()
    return new_combined_reversed_list

print(combine_reverse(list3, list4))
