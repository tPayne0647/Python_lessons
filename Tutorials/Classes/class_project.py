from datetime import time


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{name} menu available from {start} to {end}".format(
            name=self.name, start=self.start_time, end=self.end_time
        )

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return "Bill total: ${}".format(total_price)


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Brunch
brunch_items = {
    "pancakes": 7.50,
    "waffles": 9.00,
    "burger": 11.00,
    "home fries": 4.50,
    "coffee": 1.50,
    "espresso": 3.00,
    "tea": 1.00,
    "mimosa": 10.50,
    "orange juice": 3.50,
}

brunch = Menu("Brunch", brunch_items, time(11, 0), time(16, 0))


# Early Bird
early_bird_items = {
    "salumeria plate": 8.00,
    "salad and breadsticks (serves 2, no refills)": 14.00,
    "pizza with quattro formaggi": 9.00,
    "duck ragu": 17.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 1.50,
    "espresso": 3.00,
}

early_bird = Menu("Early Bird", early_bird_items, time(15, 0), time(18, 0))


# Dinner
dinner_items = {
    "crostini with eggplant caponata": 13.00,
    "caesar salad": 16.00,
    "pizza with quattro formaggi": 11.00,
    "duck ragu": 19.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 2.00,
    "espresso": 3.00,
}

dinner = Menu("Dinner", dinner_items, time(17, 0), time(23, 0))


# Kids
kids_items = {"chicken nuggets": 6.50, "fusilli with wild mushrooms": 12.00, "apple juice": 3.00}

kids = Menu("Kids", kids_items, time(11, 0), time(21, 0))


# Take a' Arepa
take_a_arepa_items = {
    "arepa pabellon": 7.00,
    "pernil arepa": 8.50,
    "guayanes arepa": 8.00,
    "jamon arepa": 7.50,
}

take_a_arepa_menu = Menu("Take a’ Arepa", take_a_arepa_items, time(10, 0), time(20, 0))

all_menus = [brunch, early_bird, dinner, kids]

# Creating new stores
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
arepas_place = Franchise("189 Fitzgerald Avenue", take_a_arepa_menu)


# Testing

# Test Brunch order
brunch_order = ["pancakes", "home fries", "coffee"]
brunch_order_bill = brunch.calculate_bill(brunch_order)
# print(brunch_order_bill)

# Test Early Bird order
early_bird_order = ["salumeria plate", "mushroom ravioli (vegan)"]
early_bird_bill = early_bird.calculate_bill(early_bird_order)
# print(early_bird_bill)

# Test available menus at flagship store at noon.
time_noon = time(12, 0)
# print(flagship_store.available_menus(time_noon))

# Test available menus at new installment at 5pm
time_five_pm = time(17, 0)
# print(new_installment.available_menus(time_five_pm))

# Create Business
basta_fazoolin = Business("Basta Fazoolin", [flagship_store, new_installment])

take_a_arepe = Business("Take a' Arepa", arepas_place)
