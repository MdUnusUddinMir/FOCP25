'''Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".'''

user_number = int(input("Enter a number between 0 and 12: "))

if 0 <= user_number <= 12:
    if user_number >= 0:
        for i in range(13):
            print(f"{i} x {user_number} = {i * user_number}")
elif user_number < 0:
        for i in range(12, -1, -1):
            print(f"{i} x {user_number} = {i * user_number}")
else:
    print("Entered number must be between 0 and 12.")


