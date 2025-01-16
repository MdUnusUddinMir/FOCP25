import random
import string

def encrypt_with_random_interval(message):
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Remove spaces from the message for proper encryption
    message = message.replace(" ", "")
    
    encrypted_message = []
    for i, letter in enumerate(message):
        # Add the current letter to the encrypted message
        encrypted_message.append(letter)
        
        # Add random letters at the specified interval
        if (i + 1) % interval == 0 and i != len(message) - 1:
            random_char = random.choice(string.ascii_lowercase)
            encrypted_message.append(random_char)
    
    # Convert the list to a string
    encrypted_message = ''.join(encrypted_message)
    
    return encrypted_message, interval

# Example usage:
message = "send cheese"
encrypted, interval = encrypt_with_random_interval(message)
print(f"Original message: {message}")
print(f"Encrypted message: {encrypted}")
print(f"Random interval: {interval}")
