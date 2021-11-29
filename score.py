"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status
"""

# Check your boundary conditions (e.g. >= 50 should be a pass, not just > 50)
# Think about efficiency and nesting; use the fewest number of if/elif
# "The Zen of Python" says, "Flat is better than nested."
# https://www.python.org/dev/peps/pep-0020/
# Also note that here we only have one path for "Invalid score" (DRY principle)
# You want to make sure the last path is "else", not "elif" as we always want a result here,
# so there should be no final condition (if it wasn't one of the earlier possibilities,
# it must be the last thing, no need to check if it is)


import random
from unittest import result


def main():
    number = int(input("Enter number you need :"))
    get_random(number)


def get_random(number):
    OUTPUT_FILE = 'results.txt'
    out_file = open(OUTPUT_FILE, 'w')
    for i in range(number):
        result = random.randint(0, 100)
        if result >= 90:
            print(format(result), "is Excellent", file=out_file)
        elif result >= 50:
            print(format(result), "is Passable", file=out_file)
        else:
            print(format(result), "is Bad", file=out_file)
    out_file.close()


main()
