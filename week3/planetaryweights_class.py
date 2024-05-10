"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""


# Constants for gravitational forces relative to Earth
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.360
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.140


def main():
    # Prompt user for input
    earth_weight = float(input("Enter a weight on Earth: "))
    planet_name = input("Enter a planet: ")

    # Calculate weight on the specified planet
    if planet_name == "Mercury":
        planetary_weight = earth_weight * MERCURY_GRAVITY
    elif planet_name == "Venus":
        planetary_weight = earth_weight * VENUS_GRAVITY
    elif planet_name == "Mars":
        planetary_weight = earth_weight * MARS_GRAVITY
    elif planet_name == "Jupiter":
        planetary_weight = earth_weight * JUPITER_GRAVITY
    elif planet_name == "Saturn":
        planetary_weight = earth_weight * SATURN_GRAVITY
    elif planet_name == "Uranus":
        planetary_weight = earth_weight * URANUS_GRAVITY
    elif planet_name == "Neptune":
        planetary_weight = earth_weight * NEPTUNE_GRAVITY
    else:
        print("Invalid planet name. Please type the planet's name in the correct format, e.g., 'Mars'.")
        return

    # Print the calculated planetary weight
    print(f"The equivalent weight on {planet_name}: {planetary_weight:.2f}")


if __name__ == "__main__":
    main()
