import sys

# Ensure arguments are provided
if len(sys.argv) > 1:
    try:
        # Convert command-line arguments to floats
        temperatures = [float(arg) for arg in sys.argv[1:]]
        
        # Calculate max, min, and mean temperatures
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)

        # Print the results
        print(f"Max Temperature: {max_temp}C")
        print(f"Min Temperature: {min_temp}C")
        print(f"Mean Temperature: {mean_temp:.2f}C")

    except ValueError:
        # Handle the case where non-numeric data is provided
        print("Please provide valid numeric temperatures.")
else:
    print("No temperatures provided.")
