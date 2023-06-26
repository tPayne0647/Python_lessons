sales_data = [[102, 342, 97], [98, 43, 110], [400, 123, 666]]
total_sales = 0

for locations in sales_data:
    print(locations)
    for i in locations:
        total_sales += i

print(total_sales)
