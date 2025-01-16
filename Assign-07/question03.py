def manage_countries_and_capitals():
    countries = {}
    while True:
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip().lower()
        if country == 'exit':
            break

        if country in countries:
            print(f"The capital of {country.title()} is {countries[country]}.")
        else:
            capital = input(f"What is the capital of {country.title()}? ").strip()
            countries[country] = capital
            print(f"Added {country.title()} with capital {capital}.")

# Call the function
if __name__ == "__main__":
    manage_countries_and_capitals()
