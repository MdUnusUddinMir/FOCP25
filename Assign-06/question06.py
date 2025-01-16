import random
import string

# Function to encrypt the message by inserting random characters at a random interval
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

# Function to decrypt the encrypted message by removing random characters
def decrypt_message(encrypted_message, interval):
    decrypted_message = []
    
    # Iterate through the encrypted message, picking every 'interval' character
    for i in range(len(encrypted_message)):
        if (i + 1) % (interval + 1) == 0:
            continue  # Skip the random character inserted during encryption
        decrypted_message.append(encrypted_message[i])
    
    # Join the list into a string to form the decrypted message
    return ''.join(decrypted_message)

# Example usage:
message = "send cheese"

# Encrypt the message
encrypted_message, interval = encrypt_with_random_interval(message)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Random interval: {interval}")

# Decrypt the message using the same interval
decrypted_message = decrypt_message(encrypted_message, interval)
print(f"Decrypted message: {decrypted_message}")
