# Task 4: Program to report the six most common letters
def six_most_common_letters(message):
    from collections import Counter
    
    message = message.lower()
    letter_counts = Counter(char for char in message if char.isalpha())
    most_common = letter_counts.most_common(6)
    
    for letter, count in most_common:
        print(f"{letter}: {count}")

# Test Task 4
message = "This is an example message to test frequency analysis."
six_most_common_letters(message)
