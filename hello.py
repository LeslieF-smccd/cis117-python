# This is my first Python programming assignment
# Author: Leslie Fong
# Date: August 31, 2026

name = input("What is your name? ")
print("Hello,", name)

# Additional req 1 and 2 - setup an arbitrary 7 digit int variable. 
# Print it using f-string in 4 formats.
my_id = 1134469
print(f"Variable my_id as padded 8 zeros integer: {my_id:08d}")
print(f"Variable my_id as 2 digit precision float: {float(my_id):.2f}") # format can auto convert
print(f"Variable my_id as binary integer: {my_id:b}")
print(f"Variable my_id as hexadecimal integer: {my_id:#x}")

# Additional req 3 and 4: extract digits using // and % operators instead of str[].
# The first and last digits of arbitrary number match my student ID number.
my_str = str(my_id)
my_len = len(my_str)
magnitude = 10 ** (my_len - 1)
first = my_id // magnitude
last = my_id % 10

print(f"Sum of the first and last digits is {first + last}")