def get_temperatures():
    temperatures = []
    for i in range(6):
        temp_str = input(f"Enter temperature {i + 1} in Celsius (e.g., 25C): ")
        if temp_str.endswith("C"):
            temp_c = float(temp_str[:-1])
            temperatures.append(temp_c)
        else:
            print("Invalid input. Please use Celsius format (e.g., 25C).")
    return temperatures

def calculate_statistics(temps):
    max_temp = max(temps)
    min_temp = min(temps)
    mean_temp = sum(temps) / len(temps)
    return max_temp, min_temp, mean_temp

# Testing the program
temperatures = get_temperatures()
max_temp, min_temp, mean_temp = calculate_statistics(temperatures)

print(f"Max Temperature: {max_temp}C")
print(f"Min Temperature: {min_temp}C")
print(f"Mean Temperature: {mean_temp:.2f}C")
