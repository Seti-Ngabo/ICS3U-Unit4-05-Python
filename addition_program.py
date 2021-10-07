#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program uses a for loop
#   with user input


def main():
    # this function uses a for loop
    counter = 0
    total = 0

    # input
    user_number_as_string = input("How many numbers are you going to add: ")
    print("")

    # process & output
    try:
        user_number_as_integer = int(user_number_as_string)
        for counter in range(user_number_as_integer + 1):
            counter = counter + 1
            second_input_str = input("Enter the number: ")
            print("")
            second_input_int = int(second_input_str)
            if second_input_int < 0:
                continue
            total = total + second_input_int

        print("The sum of just the positive numbers is = {0}".format(total))

    except Exception:
        print("Oops invalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
