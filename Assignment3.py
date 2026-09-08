# Homework 3
# Author: Leslie Fong
# Date: September 7, 2026

# Define a function to handle the reports' messaging.
# Illogical to name any (primary of auxiliary) highway as numbered 0.
# However some exist as states' highways ending 00, breaking that assumption!
# Consequently specially treat those - 100, 200, 300...
#
# Otherwise caller validates the int argument being in range 1 - 999.
# Report uses the same terminology of problem assignment, without trying
# to validate being a highway vs interstate for its official designation

def report_highway(highway):
    even = highway % 2 == 0
    primary = highway % 100 # E.g. NXX serves highway XX

    is_aux = highway >= 100 and primary != 0

    # direction not available to report for aux of primary
    if even:
        direction = "east/west"
    else:
        direction = "north/south"

    print(f"Interstate {highway} ", end = '')
    if is_aux:
        print(f"is an auxiliary highway serving I-{primary}, which ", end = '')
    elif primary == 0:
        print(f"can not be auxiliary. Interstate {highway} ", end = '')
    print(f"runs {direction}.")
    return None

# Main processing for extracting the user input of a highway.
# Input actions split for potential future handling not an int 1-999.
user_string = input("Enter a highway number: ") # between 1 and 999
user_highway = int(user_string)
if user_highway >= 1 and user_highway <= 999:
    # Input number was in the valid range at least.
    report_highway(user_highway)
else:
    print("Invalid highway number.")
    # "Try running it again, Sam!"

# Run extra tests on interesting and corner cases.
print("\n\nTesting in range numbers, without user input:")
test_set = [1, 37, 92, 99, 100, 101, 280]
for i in range(len(test_set)):
    print(f"  Test of {test_set[i]:3d} - ", end='')
    report_highway(test_set[i])
