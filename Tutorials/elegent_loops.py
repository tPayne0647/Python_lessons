# # Add 10 points to each grade and print resulting grades
# grades = [90, 88, 62, 76, 74, 89, 48, 57]
# scaled_grades = [grade + 10 for grade in grades]
# print(scaled_grades)


# Double list of numbers and print out both lists using only 3 lines
numbers = [2,4,10,100,500,1000]
doubled = [i * 2 for i in numbers]
print(str(numbers) + "\n" + str(doubled))




# List comprehension: conditional - can only ride if taller than 161
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [i for i in heights if i > 161]
print(can_ride_coaster)