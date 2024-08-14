# Function to convert Fahrenheit to Celsius


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