def encrypt_message(message):
    # Remove spaces from the message and reverse the resulting string
    encrypted_message = message.replace(" ", "")[::-1]
    return encrypted_message

# Example usage:
message = "Hello world this is a test"
encrypted = encrypt_message(message)
print(f"Original message: {message}")
print(f"Encrypted message: {encrypted}")
