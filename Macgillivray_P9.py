# MacGillivray_P8
# # Programmer: Noah MacGillivray
# EMail: nmacgillivray@cnm.edu
# Purpose: Extends from P7 and practices using exceptions.
# This program instantiates two base GPS locations via the
# GeoPoint class, takes input from the user

from GeoPoint import GeoPoint

user_continue = True  # Condition to continue program loop


# Header function
def header():
    print(
        "This program finds the distance between two predetermined locations (LA & NYC) and the location you provide.\n"
    )


# Instantiates base locations
base_distance1 = GeoPoint(34.0522, -118.2437, "Los Angeles")
base_distance2 = GeoPoint()
base_distance2.SetPoint((40.7128, -74.0060))
base_distance2.SetDescription("NYC")

# Testing
# print(base_distance1.point)
# distance = GeoPoint.calc_distance(base_distance1.point, base_distance2.point)
# print(distance)


# Asks user for location name.
def get_location_name():

    while True:
        user_input = input("Enter the location name: ")

        if user_input:
            return user_input
        print("Nothing was entered; please provide a name.")


# Asks user for location; converts the input from string to float and stores in a tuple
def get_location():
    while True:
        user_input = input(
            "Enter your latitude and longitude (in decimal degrees) separated by a space: "
        )
        try:
            lat_long = user_input.split()

            if len(lat_long) != 2:
                raise ValueError(
                    "Please enter exactly two values only separated by a space."
                )

            lat_long = tuple(map(float, lat_long))

            return lat_long
        except ValueError:
            print(
                "Invalid input; please enter two separate coordinates separated by a space."
            )


# Program loop that uses other functions to get locations,
# calculate distance, print the results and ask user to continue.
try:
    while user_continue == True:
        header()
        # GPS and locations name variables
        user_lat, user_long = get_location()
        user_location_name = get_location_name()
        user_input = GeoPoint(user_lat, user_long, user_location_name)

        # Calculate distance from first predetermined location
        distance_one = GeoPoint.calc_distance(user_input.point, base_distance1.point)
        print()
        print(
            f"The distance between {user_input.description} and {base_distance1.description} is {distance_one:.2f}km\n"
        )
        # Calculate distance from second predetermined location
        distance_two = GeoPoint.calc_distance(user_input.point, base_distance2.point)
        print(
            f"The distance between {user_input.description} and {base_distance2.description} is: {distance_two:.2f}km\n"
        )
        # Determines if user location is closer to predetermined location one or two
        if distance_one > distance_two:
            print(f"You are closer to: {base_distance2.description}")
        else:
            print(f"You are closer to: {base_distance1.description}")
        print()

        compute_another = (
            input("Would you like to compute another? Enter yes or no: ")
            .strip()
            .lower()
        )
        if compute_another == "yes":
            continue
        else:
            print()
            print("Thanks for using the program, have a nice day!")
            user_continue = False
except Exception as e:
    print("Something went wrong: ", e)

    compute_another = (
        input("Would you like to compute another? Enter yes or no: ").strip().lower()
    )
    if compute_another == "yes":
        compute_another = True
    else:
        print()
        print("Thanks for using the program, have a nice day!")
        user_continue = False
