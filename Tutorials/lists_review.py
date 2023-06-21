inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Length of inventory.
inventory_len = len(inventory)

# First item in inventory.
first = inventory[0]

# Last item in inventory.
last = inventory[-1]

# Select index 2 to 6, not including 6.
inventory_2_6 = inventory[2:6]

# Select first 3 items of inventory
first_3 = inventory[:3]

# How many twin beds?
twin_beds = inventory.count("twin bed")

# Remove 5th item
removed_item = inventory.pop(4)

# Add item to 11th element
inventory.insert(10, "19th Century Bed Frame")

# Sort Inventory
inventory = sorted(inventory)
print(inventory)