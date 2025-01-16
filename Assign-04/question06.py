# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function that takes input as Celsius string and converts to Fahrenheit
def convert_celsius_to_fahrenheit(temp_str):
    if temp_str.endswith("C"):
        try:
            temp_c = float(temp_str[:-1])  # Remove the 'C' and convert to float
            temp_f = celsius_to_fahrenheit(temp_c)
            return f"{temp_f:.1f}F"
        except ValueError:
            return "Invalid input: not a valid number"
    else:
        return "Invalid input: should end with 'C'"

# Testing the program
temp_input = input("Enter temperature in Celsius (e.g., 25C): ")
print(convert_celsius_to_fahrenheit(temp_input))
