def to_binary(n):
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    return bin(n)[2:]

# Example usage:
number = 10
binary_representation = to_binary(number)
print(f"Binary representation of {number} is: {binary_representation}")
