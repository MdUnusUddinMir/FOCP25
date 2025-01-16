'''Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive.'''

user_number = int(input("Enter a number between 0 and 12: "))
if 0 <= user_number <= 12:
    for i in range(13):
        print(f"{i} x {user_number} = {i * user_number}")
else:
    print("Entered number must be between 0 and 12.")
