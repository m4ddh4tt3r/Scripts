import ast

MAX_ATTEMPTS = 3


def get_distance():
    """
       Prompts the user to enter the total distance of the trip in miles.
       Validates the input and returns the distance as a float value.
       If the user exceeds the maximum number of invalid attempts, it returns None.

       Returns:
           float: The total distance of the trip in miles.
           None: If the user exceeds the maximum number of invalid attempts.
       """
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
    """
        Retrieves the fuel efficiency of the vehicle from the user, expressed in miles per gallon.
        Validates the input and returns the fuel efficiency as a float value.
        If the user exceeds the maximum number of invalid attempts, it returns None.

        Returns:
            float: The fuel efficiency of the vehicle in miles per gallon.
            None: If the user exceeds the maximum number of invalid attempts.
        """
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
    """
        Prompts the user to select the type of fuel used by the vehicle.
        Presents a menu of options and validates the input.
        Returns the selected fuel type as an integer (1, 2, 3, or 4) corresponding to the options provided.
        If the user exceeds the maximum number of invalid attempts, it returns None.

        Returns:
            int: The number corresponding to the selected fuel type.
            None: If the user exceeds the maximum number of invalid attempts.
        """
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
    """
        Retrieves the price of the selected fuel type per gallon from the user.
        Takes the fuel type as an argument to determine the specific prompt for the fuel type.
        Validates the input and returns the price as a float value.
        If the user exceeds the maximum number of invalid attempts, it returns None.

        Args:
            fuel_type (int): The number corresponding to the selected fuel type.

        Returns:
            float: The price of the selected fuel type per gallon.
            None: If the user exceeds the maximum number of invalid attempts.
        """
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
    """
       Calculates the total cost of the trip based on the distance, fuel efficiency, and gas price.
       Takes these three parameters and returns the total cost as a rounded float value.

       Args:
           distance (float): The total distance of the trip in miles.
           mpg (float): The fuel efficiency of the vehicle in miles per gallon.
           gas_price (float): The price of the selected fuel type per gallon.

       Returns:
           float: The total cost of the trip.
       """
    total_cost = (distance / mpg) * gas_price
    return round(total_cost, 2)


def run_car_trip_cost_calculator():
    """
        Serves as the entry point for running the car trip cost calculator.
        Displays a welcome message and a separator line.
        Calls the other functions in a loop to collect the necessary information from the user and calculate the trip cost.
        If all the required inputs are valid, it displays the total cost of the trip.
        The loop continues until a valid trip cost is calculated.
        """
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
