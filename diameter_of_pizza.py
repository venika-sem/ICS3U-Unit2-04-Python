#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Sep 2022
# This program calculates the cost of pizza per diameter

import constants


def main():
    # this function calculates the cost of pizza

    # input
    diameter = int(input("Enter the diameter of the pizza (inch): "))

    # process
    sub_total = (diameter * constants.COST_PER_INCH) + constants.LABOR + constants.RENT
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))

    print("\nDone.")


if __name__ == "__main__":
    main()
