# def generate_trip_greeting(location):
#   print("Looks like you are planning a trip to visit " + location)

# generate_trip_greeting("Germany")


# def custom_greeting(name, age, location):
#     print("Hello " + name + "!")
#     print("You are: " + age + " years old.")
#     print("You are currently located in: " + location)

# name = input("What is your name?: ")
# age = input("What is your current age?: ")
# location = input("What state are you located currently?: ")

# custom_greeting(name, age, location)


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = int(car_rental_rate) * int(trip_time)
    hotel_total = int(hotel_rate) * int(trip_time) - 10
    print("Total Trip Price: " + str(car_rental_total + hotel_total + int(plane_ticket_price)))


plane_ticket_price = input("Price of plane ticket?: ")
car_rental_rate = input("Car rental rate?: ")
hotel_rate = input("Hotel rate?: ")
trip_time = input("What is the total trip time?: ")


calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time)
