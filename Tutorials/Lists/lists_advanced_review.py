# Returns a list of every 3rd number between start and 100. IF start is >100, returns an empty list
def every_three_nums(start):
    return list(range(start, 101, 3))


print(every_three_nums(91))
print(every_three_nums(102))


#  return a list where all elements in my_list with an index between start and end have been removed.
def remove_selection(my_list, start, end):
    return my_list[:start] + my_list[end + 1 :]


print(remove_selection([4, 8, 15, 16, 23, 42], 1, 3))
print(remove_selection([100, 30, 23, 13, 67, 89, 34], 2, 5))


# Return either item1 or item2 depending on which item appears more often in my_list.
def more_frequent_item(my_list, item1, item2):
    if my_list.count(item1) >= my_list.count(item2):
        return item1
    else:
        return item2


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# Returns my_list with selected index doubled
def double_index(my_list, index):
    if index >= len(my_list):
        return my_list
    else:
        my_new_list = my_list[0:index]
    my_new_list.append(my_list[index] * 2)
    my_new_list = my_new_list + my_list[index + 1 :]
    return my_new_list


print(double_index([2, 28, 34, 98, 74, 23, 10], 1))


# Returns middle element if my_list has odd number of elements. If number of elements is even, returns average of middle 2 elements.
def middle_element(my_list):
    if len(my_list) % 2 == 0:
        sum = my_list[int(len(my_list) / 2)] + my_list[int(len(my_list) / 2) - 1]
        return sum / 2
    else:
        return my_list[int(len(my_list) / 2)]


print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 5, 5, 6, 5, 5, 5]))
