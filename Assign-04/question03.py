def format_name(name):
    return name.capitalize()  # Capitalizes the first letter, lowercase the rest

# Testing the function
name_input = input("Enter your name: ")
formatted_name = format_name(name_input)
print(f"Hello, {formatted_name}!")
