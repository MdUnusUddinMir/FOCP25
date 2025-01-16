def is_valid_number(num):
    # TO check if the number is in the range 0 to 100
    if 0 <= num <= 100:
        return True
    else:
        return False

# Testing the function
test_numbers = [25, -5, 105, 50, 100, 0]
for num in test_numbers:
    print(f"Is {num} valid? {is_valid_number(num)}")
