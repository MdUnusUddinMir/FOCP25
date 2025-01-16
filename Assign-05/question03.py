import sys

# Ensure arguments are provided
if len(sys.argv) > 1:
    # Sort arguments by length
    shortest_argument = min(sys.argv[1:], key=len)
    print(f"The shortest argument is: {shortest_argument}")
else:
    print("No arguments provided.")
