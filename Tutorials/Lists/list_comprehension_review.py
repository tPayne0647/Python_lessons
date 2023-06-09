hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# Get sum of all prices
for price in prices:
    total_price += price

# Get and print average price
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# Subtract each price by 5 and print new prices
new_prices = [i - 5 for i in prices]
print("New Prices: " + str(new_prices))

# Get total revenue from last week sales
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

# Get and print average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))


# Find all cuts under 30 and print their names from hairstyles
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
print(cuts_under_30)
