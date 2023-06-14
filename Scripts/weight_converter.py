import sys

while True:
    try:
        weight = float(input("Weight: "))
        unit = input("(K)g or (L)bs: ")

        if unit.upper() == "K":
            converted = weight / 0.45
            print("Weight in Lbs: " + str(converted))
            sys.exit()
        
        elif unit.upper() == "L":
            converted = weight * 0.45
            print("Weight in Lbs: " + str(converted))
            sys.exit()
            
        else:
            print("Invalid input, Please enter 'K' or 'L'.")
            
    except ValueError:
        print("Invalid weight. Please only enter numeric value.")
