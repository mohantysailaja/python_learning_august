# Function to convert Fahrenheit to Celsius





# This program converts temperature from Fahrenheit to Celsius

# Ask the user to enter a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert the temperature to Celsius using the formula
celsius = (fahrenheit - 32) * 0.556

# Print the result
print(f"The temperature in Celsius is: {celsius:.2f}")





print("THIS PROGRAM WILL CONVERT DEGREES FARENHEIT")

def fahrenheit_to_celsius(F):
    Celsius = (F - 32) * 0.556
    return Celsius

# Input from user
F = float(input("THE NUMBER YOU HAVE ENTERED IS: "))

# Conversion
C = fahrenheit_to_celsius(F)

# Output the result
print(f"{F} Fahrenheit is equal to {C:.2f} Celsius")