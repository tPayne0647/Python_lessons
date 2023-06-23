import sys
sys.path.append('/home/tpayne/Python_lessons')

from Ascii_art.tripcalc import trip_calc

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = int(car_rental_rate) * int(trip_time)
  hotel_total = int(hotel_rate) * int(trip_time) - 10
  print("Total Trip Price: " + str(car_rental_total + hotel_total + int(plane_ticket_price)))

plane_ticket_price = input("Price of plane ticket?: ")
car_rental_rate = input("Car rental rate?: ")
hotel_rate = input("Hotel rate?: ")
trip_time = input("What is the total trip time?: ")

trip_calc()
calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time)