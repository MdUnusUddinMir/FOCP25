def find_factors(n):
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Example usage:
number = 12
factors_of_number = find_factors(number)
print(f"Factors of {number} are: {factors_of_number}")
