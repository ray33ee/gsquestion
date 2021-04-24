#  This code attempts to solve the Goldman-Sachs repeating decimal interview question.
#  The question is as follows:
#  Given a dividend and divisor, output a string containing the result expressing recurring decimals finitely.
#  For example
#  (1, 3) => 0.(3)
#  Since 1 / 3 = 0.3333..., and we represent the recurring segment in parenthesis (3). Other examples include
#  (10, 7) => 1.(428571)
#  (35, 5) => 7
#  (3, 4) => 0.75
#  (1, 6) => 0.1(6)
#  A few points worth noting are:
#  1. Reduce by taking (int)a / (int)b and a % b.
#  2. Take special cases (i.e. when a or b are 1 or 0)
#  1.
#  1.
#  1.
#  1.
#  1.
#  1.

import math

#  This function takes a division and returns a tuple containing
#  the whole part of the calculation (whole), a list of digits in the fractional part (quotients),
#  and the index pointing to the first digit in the repeating sequence.
def recurring(dividend, divisor):
    whole = dividend // divisor  # Whole part of the result
    remainder = dividend % divisor  #

    remain = [] #  List of all remainders
    quotients = ""

    while remainder not in remain:
        quotients += str((remainder * 10 // divisor))
        remain.append(remainder)
        remainder = remainder * 10 % divisor

    return whole, remain.index(remainder), quotients

#  This function takes the three parts representing a recurring decimal (see return values from
#  'recurring' function and returns the formatted string result
def to_string(whole, index, quotients):

    ans = str(whole)

    #  Set to true if the recurring part it just zero, i.e. 0.75000..., 3.0000..., 0.23432300000...., 0.00000..., etc.
    recurring_zero = quotients[quotients.__len__()-1] == "0" and index == quotients.__len__()-1

    non_recurring = quotients[:index]
    recurring = quotients[index:]

    #  If the result is a whole number, return str(whole)
    if non_recurring.__len__() == 0 and recurring_zero:
        return ans

    ans += "." + non_recurring

    if recurring.__len__() > 0 and recurring != "0":
        ans += "(" + recurring + ")"

    return ans


def recurring_string(dividend, divisor):
    #print("Calculation: " + str(dividend) + " / " + str(divisor))
    return to_string(*recurring(dividend, divisor))


# Function that takes a repeating decimal, and converts it in to fraction
def reverse(whole, non_recurring, recurring):
    n = len(non_recurring)
    m = len(recurring)

    if non_recurring == "":
        non_recurring_val = 0
    else:
        non_recurring_val = int(non_recurring)

    numerator = int(non_recurring + recurring) - non_recurring_val
    denominator = 10**n * (10**m - 1)

    return numerator + whole * denominator, denominator


#  Convert whole, non_recurring and recurring values into whole, index and quotients
#  values, suitable for to_string function.
def convert(whole, non_recurring, recurring):
    quotients = non_recurring + recurring
    index = len(non_recurring)
    return whole, index, quotients


# Takes a recurring decimal (as whole, non-recurring and recurring parts) and tests
# recurring_string function
def confirm(whole, non_recurring, recurring):

    conv = convert(whole, non_recurring, recurring)

    actual = (to_string(*conv))

    rev = reverse(whole, non_recurring, recurring)

    predicted = recurring_string(*rev)

    print("Input: " + actual + ", Predicted: " + predicted + ", Division: " + str(rev[0]) + " / " + str(rev[1]) + " = " + str(rev[0] / rev[1]) + ", Success?: " + str(actual == predicted))




print("    " + (recurring_string(3, 4)))
print("    " + (recurring_string(1, 917)))
print("    " + (recurring_string(3, 1)))
print("    " + (recurring_string(123, 999)))
print("    " + (recurring_string(11, 16)))
print("    " + (recurring_string(1, 3)))
print("    " + (recurring_string(1, 49)))
print("    " + (recurring_string(611, 4950)))
print("    " + (recurring_string(0, 1)))

print("Teest: " + str(confirm(5, "1", "23")))