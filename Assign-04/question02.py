def count_case_letters(s):
    uppercase_count = 0
    lowercase_count = 0
    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return uppercase_count, lowercase_count

# Testibg the function
test_string = "Hello World!"
upper, lower = count_case_letters(test_string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
