Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_birth_year():
...     """
...     Prompt the user to enter their birth year and return the input.
...     """
...     while True:
...         try:
...             birth_year = int(input("Enter your birth year: "))
...             return birth_year
...         except ValueError:
...             print("Invalid input. Please enter a valid year.")
... 
... def calculate_age(birth_year):
...     """
...     Calculate the age based on the entered birth year and return it.
...     """
...     current_year = 2024  # Assuming the current year is 2024
...     age = current_year - birth_year
...     return age
... 
... def get_height():
...     """
...     Ask the user to provide their height in meters and return the input.
...     """
...     while True:
...         try:
...             height = float(input("Enter your height in meters (e.g., 1.75): "))
...             return height
...         except ValueError:
...             print("Invalid input. Please enter a valid height.")
... 
... def main():
...     # Step i: Get the birth year from the user
...     birth_year = get_birth_year()
... 
...     # Step ii: Calculate the age based on the entered birth year
...     age = calculate_age(birth_year)
... 
    # Step iii: Get the height from the user
    height = get_height()

    # Step iv: Determine and display the data type of each input
    print(f"\nData Type Information:")
    print(f"Birth Year: {type(birth_year)}")
    print(f"Age: {type(age)}")
    print(f"Height: {type(height)}")

    # Step v: Determine and display the size of each input
    print(f"\nSize Information (in bytes):")
    print(f"Birth Year: {birth_year.bit_length() // 8}")
    print(f"Age: {age.bit_length() // 8}")
    print(f"Height: {height.__sizeof__()}")

if __name__ == "__main__":
    main()
