def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Testing the functions
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}C is {temp_f}F")

temp_f_input = 77
temp_c_output = fahrenheit_to_celsius(temp_f_input)
print(f"{temp_f_input}F is {temp_c_output:.2f}C")
