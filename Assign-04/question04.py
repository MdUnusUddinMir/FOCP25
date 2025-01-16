def remove_last_character(s):
    if len(s) > 1:
        return s[:-1]
    return s

# Testing the function
test_string = "Hello!"
print(remove_last_character(test_string))  # Should print "Hello"
print(remove_last_character("A"))  # Should print "A" as it's only one character
