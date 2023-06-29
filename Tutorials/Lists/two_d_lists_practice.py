customer_data = [
    ["Ainsley", "Small", True],
    ["Ben", "Large", False],
    ["Chani", "Medium", True],
    ["Depak", "Medium", False],
]
print(customer_data)

# change chani to false
customer_data[2][2] = False
print(customer_data)

# remove false from ben
customer_data[1].remove(False)
print(customer_data)

# Add new list to existing list
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
