# A simple script that asks user for weight of a package then prints the price for each option and tells user which option would be cheapest.


# Input given by user
weight = input("What is the weight in LBS of the package you want to ship?: ")


# Ground Shipping Premium 
cost_ground_premium = 125


# Ground Shipping
if float(weight) <= 2:
  cost_ground = (float(weight) * 1.50) + 20.00
  
elif float(weight) <= 6:
  cost_ground = (float(weight) * 3.00) + 20.00

elif float(weight) <= 10:
  cost_ground = (float(weight) * 4.00) + 20.00

else:
  cost_ground = (float(weight) * 4.75) + 20.00  


# Drone Shipping
if float(weight) <= 2:
  cost_drone = float(weight) * 4.50
  
elif float(weight) <= 6:
  cost_drone = float(weight) * 9.00

elif float(weight) <= 10:
  cost_drone = float(weight) * 12.00

else:
  cost_drone = float(weight) * 14.25

# Output

print("**********************************************************************")
print("\nGround Shipping Cost: " + "$" + str(cost_ground))
print("Ground Shipping Premium: $" + str(cost_ground_premium))
print("Drone Shipping Cost: $" + str(cost_drone))

# Find Cheapest method

cheapest_cost = min(cost_ground, cost_drone, cost_ground_premium)

if cheapest_cost == cost_ground:
    cheapest_option = "Ground Shipping"
elif cheapest_cost == cost_drone:
    cheapest_option = "Drone Shipping"
else:
    cheapest_option = "Ground Shipping Premium"
    
print("\nCheapest Shipping Option: " + cheapest_option)