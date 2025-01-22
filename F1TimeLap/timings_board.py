import sys
import os
from tabulate import tabulate

def read_file(file_path):
    """
    Reads the input file and parses its contents.
    The file is expected to contain:
    - The first line: Race location
    - Subsequent lines: Lap times in the format 'DRIVER_CODE LAP_TIME'
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if not lines:
        raise ValueError("File is empty.")

    race_location = lines[0].strip()  # First line is the race location
    lap_times = [line.strip() for line in lines[1:]]  # Remaining lines are lap times

    return race_location, lap_times

def parse_lap_times(lap_times):
    """
    Parses lap times into a structured dictionary.
    Each driver code is used as a key, and their lap times are stored as a list of floats.
    """
    driver_data = {}

    for entry in lap_times:
        driver_code = entry[:3]  # First 3 characters are the driver code
        lap_time = float(entry[3:])  # Remaining part is the lap time

        if driver_code not in driver_data:
            driver_data[driver_code] = []

        driver_data[driver_code].append(lap_time)

    return driver_data

def calculate_statistics(driver_data):
    """
    Calculates statistics for each driver and overall.
    - Finds the fastest lap for each driver.
    - Calculates the average lap time for each driver and overall.
    """
    fastest_driver = None
    fastest_time = float('inf')
    overall_times = []

    driver_statistics = []

    for driver, times in driver_data.items():
        fastest_lap = min(times)  # Fastest lap for the driver
        average_lap = sum(times) / len(times)  # Average lap time for the driver

        overall_times.extend(times)  # Collect all lap times for overall statistics

        if fastest_lap < fastest_time:  # Update the fastest driver if necessary
            fastest_time = fastest_lap
            fastest_driver = driver

        driver_statistics.append((driver, fastest_lap, average_lap))

    overall_average = sum(overall_times) / len(overall_times)  # Average lap time overall

    return fastest_driver, fastest_time, overall_average, driver_statistics

def display_results(race_location, fastest_driver, fastest_time, overall_average, driver_statistics):
    """
    Displays the race results in a user-friendly format.
    Includes:
    - Race location
    - Fastest driver and their lap time
    - Overall average lap time
    - Table of driver statistics sorted by fastest lap times
    """
    print(f"Race Location: {race_location}\n")
    print(f"Fastest Driver: {fastest_driver} with a time of {fastest_time:.3f} seconds\n")
    print(f"Overall Average Lap Time: {overall_average:.3f} seconds\n")

    # Sort statistics by fastest lap time (ascending)
    sorted_statistics = sorted(driver_statistics, key=lambda x: x[1])
    table = [(driver, f"{fastest:.3f}", f"{average:.3f}") for driver, fastest, average in sorted_statistics]

    print("Driver Statistics:")
    print(tabulate(table, headers=["Driver Code", "Fastest Lap", "Average Lap"], tablefmt="grid"))

def main():
    """
    Main function to execute the program.
    - Reads input file provided via command line.
    - Processes lap time data.
    - Displays race results.
    """
    if len(sys.argv) < 2:
        print("Usage: python timings_board.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]  # Get file path from command-line arguments

    try:
        race_location, lap_times = read_file(file_path)  # Read file contents
        driver_data = parse_lap_times(lap_times)  # Parse lap times into a dictionary
        fastest_driver, fastest_time, overall_average, driver_statistics = calculate_statistics(driver_data)  # Calculate stats
        display_results(race_location, fastest_driver, fastest_time, overall_average, driver_statistics)  # Display results
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
