# Returns count of numbers in list that are divisible by 10
def divisible_by_ten(nums):
    count = 0
    for number in nums:
        if number % 10 == 0:
            count += 1
    return count


print(divisible_by_ten([20, 25, 30, 35, 40]))


# Returns a new list with the string "Hello, " before each name in the list
def add_greetings(names):
    new_list = []
    for name in names:
        new_list.append("Hello, " + name)

    return new_list


print(add_greetings(["Owen", "Max", "Sophie"]))


# Returns a new list with the first even numbers removed
def delete_starting_evens(my_list):
    while len(my_list) > 0 and my_list[0] % 2 == 0:
        my_list = my_list[1:]

    return my_list


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
print(delete_starting_evens([2, 4, 6, 8, 9, 10, 12, 14]))


# Returns a new list of every odd index
def odd_indices(my_list):
    new_list = []
    for index in range(1, len(my_list), 2):
        new_list.append(my_list[index])

    return new_list


print(odd_indices([4, 3, 7, 10, 11, -2]))


# Returns a new list of exponents
def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base**power)

    return new_list


print(exponents([2, 3, 4], [1, 2, 3]))


# Gets sum of each list of numbers, returns list with greater sum. If list sum is equal, return list1
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number in lst1:
        sum1 += number
    for number in lst2:
        sum2 += number
    if sum1 > sum2 or sum1 == sum2:
        return lst1
    else:
        return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))


# Goes through and adds up numbers on a list. stops when value reaches over 9000
def over_nine_thousand(lst):
    sum = 0
    for number in lst:
        sum += number
        if sum > 9000:
            break
    return sum


print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([100, 100, 100, 100, 100, 100, 100]))


# Returns the highest number in list
def max_num(nums):
    maximum = nums[0]
    for number in nums:
        if number > maximum:
            maximum = number
    return maximum


print(max_num([50, -10, 0, 75, 20]))


# Return a new list with index values of matching numbers from two lists
def same_values(lst1, lst2):
    new_list = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_list.append(index)
    return new_list


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
