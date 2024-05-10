"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

# Plan
# Take input on earth
# Take the name of the planet input
# Use If Else
# if planet name == "Mars":
#    planetary_weight = earth_weight * 0.378
# elif


# Use uppercase for CONSTANTS
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.360
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.140


def main():
    # prompt user for inputs
    earth_weight_input = input("Enter a weight on Earth: ")
    planet_name_input = input("Enter a planet: ")

    # cast weight on earth from string to float
    earth_weight = float(earth_weight_input)

    # initilize the variable
    planetary_weight = 0

    # calculate weight on the specified planet
    if planet_name_input == "Mercury":
        planetary_weight = earth_weight * MERCURY_GRAVITY
    elif planet_name_input == "Venus":
        planetary_weight = earth_weight * VENUS_GRAVITY
    elif planet_name_input == "Mars":
       planetary_weight = earth_weight * MARS_GRAVITY
    elif planet_name_input == "Jupiter":
        planetary_weight = earth_weight * JUPITER_GRAVITY
    elif planet_name_input == "Saturn":
        planetary_weight = earth_weight * SATURN_GRAVITY
    elif planet_name_input == "Uranus":
        planetary_weight = earth_weight * URANUS_GRAVITY
    elif planet_name_input == "Neptune":
        planetary_weight = earth_weight * NEPTUNE_GRAVITY
    else: 
        print("Please type planet's name in right format, e.g. Mars")
    
    planetary_weight_rounded = round(planetary_weight, 2)
    
    # print the calculated planetary weight
    print("The equivalent weight on", planet_name_input, ": ", planetary_weight_rounded)


if __name__ == "__main__":
    main()
