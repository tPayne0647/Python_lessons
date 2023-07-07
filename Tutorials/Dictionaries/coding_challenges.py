# Write your sum_values function here:
def sum_values(my_dictionary):
    counter = 0
    for i in my_dictionary.values():
        counter += i

    return counter


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6


def sum_even_keys(my_dictionary):
    total = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            total += my_dictionary[key]
    return total


# should print 6


# Write your add_ten function here:
def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}


# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
    result = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            result.append(value)
    return result


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]


# Write your max_key function here:
def max_key(my_dictionary):
    max_value = float("-inf")
    max_key = None
    for key, value in my_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"


# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}


# Write your unique_values function here:
def unique_values(my_dictionary):
    unique_values_set = set(my_dictionary.values())
    return len(unique_values_set)


# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1


def count_first_letter(names):
    letters = {}
    for key in names:
        first_letter = key[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[key])
    return letters
