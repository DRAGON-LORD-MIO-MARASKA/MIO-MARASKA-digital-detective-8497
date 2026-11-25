# number_converter.py
# A simple program that converts a decimal number to binary and hexadecimal.

user_input = input("Enter a decimal number: ")
number = int(user_input)

binary_result = bin(number)
hex_result = hex(number)

print(f"Decimal: {number}")
print(f"Binary:  {binary_result}")
print(f"Hexadecimal: {hex_result}")
