#!/usr/bin/env python3
# Created by: minab berhane
# Created on: oct, 3, 2022
# this program is used to calculate the surface area and volume of a Octahedron

import math


def main():
    # Introduces game to user
    print("\033[1;35;34mHello user, welcome to virtual calculator")
    print(
        "\033[1;35;30mWe will be calculating the surface area and volume of an Octahedron"
    )
    print()
    # Get user input
    user_input = float(input("Please input the length of the side: "))
    user_unit = input("What unit would you like to use: ")
    user_choice = int(
        input(
            "Please input 1 if you would like to find area, 2 for volume and 3 for both: "
        )
    )

    # Calculate Surface area and volume
    if user_choice == 1:
        area = 2 * math.sqrt(3) * (user_input**2)
        print("The area is= {:.2f} {}^2".format(area, user_unit))
        print("Thank you for playing!")
    elif user_choice == 2:
        volume = ((math.sqrt(2)) / 3) * (user_input**3)
        print("The volume is= {:.2f} {}^2".format(volume, user_unit))
        print("Thank you for playing!")
    elif user_choice == 3:
        area = 2 * math.sqrt(3) * (user_input**2)
        volume = ((math.sqrt(2)) / 3) * (user_input**3)
        # Print answer
        print("The area is= {:.2f} {}^2".format(area, user_unit))
        print("The volume is= {:.2f} {}^2".format(volume, user_unit))
        print("Thank you for playing!")
    else:
        print("Sorry {} is not an option try again".format(user_choice))


if __name__ == "__main__":
    main()
