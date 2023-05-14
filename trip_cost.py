import ast

MAX_ATTEMPTS = 3


def get_distance():
    invalid_attempts = 0
    while invalid_attempts < MAX_ATTEMPTS:
        distance = input("Enter the total distance of your trip (in miles): ")

        try:
            # Evaluate the input as a mathematical expression
            distance = ast.literal_eval(distance)
            if isinstance(distance, (int, float)):
                return distance
            else:
                print("Invalid input! Please enter a valid numeric value.")
        except (SyntaxError, ValueError):
            # Attempt to evaluate as an equation using eval
            try:
                distance = eval(distance)
                if isinstance(distance, (int, float)):
                    return distance
                else:
                    print("Invalid input! Please enter a valid numeric value or equation.")
            except (SyntaxError, ValueError):
                print("Invalid input! Please enter a valid numeric value or equation.")

        invalid_attempts += 1
        if invalid_attempts >= MAX_ATTEMPTS:
            print("Too many invalid attempts. Starting over...")
            return None

    print("Too many invalid attempts. Starting over...")
    return None


def get_fuel_efficiency():
    invalid_attempts = 0
    while invalid_attempts < MAX_ATTEMPTS:
        mpg = input("Enter the fuel efficiency of your vehicle (in miles per gallon): ")
        if any(char in mpg for char in ['+', '-', '*', '/']):
            print("Invalid input! Please enter a valid fuel efficiency.")
            invalid_attempts += 1
        elif not mpg.replace('.', '', 1).isdigit():
            print("Invalid input! Please enter a numeric value for fuel efficiency.")
            invalid_attempts += 1
        else:
            return float(mpg)

    print("Too many invalid attempts. Starting over...")
    return None


def get_gas_type():
    invalid_attempts = 0
    while invalid_attempts < MAX_ATTEMPTS:
        print("\nWhat type of fuel do you use?")
        print("1. Regular unleaded")
        print("2. Unleaded Plus")
        print("3. Premium Unleaded")
        print("4. Diesel")
        fuel_type = input("Enter the number corresponding to your fuel type: ")

        try:
            fuel_type = int(fuel_type)
            if fuel_type not in [1, 2, 3, 4]:
                raise ValueError
            return fuel_type
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            invalid_attempts += 1

    print("Too many invalid attempts. Starting over...")
    return None


def get_gas_price(fuel_type):
    invalid_attempts = 0
    gas_price = None
    while invalid_attempts < MAX_ATTEMPTS:
        if fuel_type == 1:
            gas_price = input("Enter the price of regular unleaded gasoline per gallon: ")
        elif fuel_type == 2:
            gas_price = input("Enter the price of unleaded plus gasoline per gallon: ")
        elif fuel_type == 3:
            gas_price = input("Enter the price of premium unleaded gasoline per gallon: ")
        elif fuel_type == 4:
            gas_price = input("Enter the price of diesel fuel per gallon: ")

        try:
            gas_price = float(gas_price)
            return gas_price
        except ValueError:
            print("Invalid input! Please enter a numeric value for fuel price.")
            invalid_attempts += 1

        if invalid_attempts >= MAX_ATTEMPTS:
            print("Too many invalid attempts. Starting over...")
            return None

    print("Too many invalid attempts. Starting over...")
    return None


def calculate_trip_cost(distance, mpg, gas_price):
    total_cost = (distance / mpg) * gas_price
    return round(total_cost, 2)


def run_car_trip_cost_calculator():
    print("Welcome to the Car Trip Cost Calculator!")
    print("-----------------------------------------")

    while True:
        distance = get_distance()
        if distance is None:
            continue

        mpg = get_fuel_efficiency()
        if mpg is None:
            continue

        fuel_type = get_gas_type()
        if fuel_type is None:
            continue

        gas_price = get_gas_price(fuel_type)
        if gas_price is None:
            continue

        total_cost = calculate_trip_cost(distance, mpg, gas_price)
        print("\nThe total cost of your trip will be $" + str(total_cost) + ".")
        break


# Run the car trip cost calculator
run_car_trip_cost_calculator()
