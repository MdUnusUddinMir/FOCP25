'''Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password1 = input("Enter a password (8-12 characters): ")

    if not (8 <= len(password1) <= 12):
        print("Error:Password must be between 8 and 12 characters long.")
        continue

    if password1 in BAD_PASSWORDS:
        print("Error:Bad Password")
        continue

    password2 = input("Re-enter your password to confirm: ")
    if password1 != password2:
        print("Error: Passwords do not match.")
        continue

    print("Password Set")
    break
