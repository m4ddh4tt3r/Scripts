print("Welcome to the Car Trip Cost Calculator!")
print("-----------------------------------------")

# Get user input for trip distance
distance = input("Enter the total distance of your trip (in miles): ")

# Check if distance input includes a math formula
if any(char in distance for char in ['+', '-', '*', '/']):
    try:
        # Evaluate the math formula and assign the result to distance
        distance = str(eval(distance))
    except (NameError, SyntaxError):
        # If the math formula is invalid, print an error message and exit
        print("Invalid math formula! Please enter a valid math formula.")
        exit()

# Get user input for fuel efficiency
mpg = input("Enter the fuel efficiency of your vehicle (in miles per gallon): ")

# Get user input for fuel type and price per gallon
print("\nWhat type of gasoline do you use?")
print("1. Regular unleaded")
print("2. Unleaded Plus")
print("3. Premium Unleaded")
print("4. Diesel")
fuel_type = int(input("Enter the number corresponding to your gasoline type: "))
if fuel_type == 1:
    gas_price = input("Enter the price of regular unleaded gasoline per gallon: ")
elif fuel_type == 2:
    gas_price = input("Enter the price of unleaded plus gasoline per gallon: ")
elif fuel_type == 3:
    gas_price = input("Enter the price of premium unleaded gasoline per gallon: ")
elif fuel_type == 4:
    gas_price = input("Enter the price of diesel gasoline per gallon: ")

# Convert user input to floats
try:
    distance = float(distance)
    mpg = float(mpg)
    gas_price = float(gas_price)
except ValueError:
    print("Invalid input! Please enter only numeric values.")
    exit()

# Calculate the total cost of the trip
total_cost = (distance / mpg) * gas_price

# Print the result
print("\nThe total cost of your trip will be $" + str(round(total_cost, 2)) + ".")
