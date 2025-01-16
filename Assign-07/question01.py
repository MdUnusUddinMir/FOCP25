# : Function to return a sorted list of unique letters in a string
def unique_sorted_letters(string):
    return sorted(set(string))

# Test Task 1
print(unique_sorted_letters("cheese"))  # Output: ['c', 'e', 'h', 's']
