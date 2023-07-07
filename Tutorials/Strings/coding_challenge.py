letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# Write your unique_english_letters function here:
def unique_english_letters(word):
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1
    return uniques


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


# Write your count_char_x function here:
def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
    splits = word.split(x)
    return len(splits) - 1


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return word[start_ind + 1 : end_ind]
    return word


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# Write your x_length_words function here:
def x_length_words(sentence, x):
    words = sentence.split()
    for word in words:
        if len(word) < x:
            return False
    return True


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


def check_for_name(sentance, name):
    lowercase_name = name.lower()
    if lowercase_name in sentance.lower():
        return True
    else:
        return False


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# Write your every_other_letter function here:
def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


def reverse_string(word):
    return word[::-1]


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# Write your add_exclamation function here:
def add_exclamation(word):
    while len(word) < 20:
        word += "!"
    return word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
