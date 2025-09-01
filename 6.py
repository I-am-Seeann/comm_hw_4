#6 სორტირება
# მომხმარებელს შემოჰყავს რიცხვები თითო გამოტოვებით,
# (ულიმიტოდ რამდენიც უნდა)
# პროგრამა სთავაზობს როგორ უნდა რომ დაუსორტირდეს აღნიშნული:
# კლებადობით, ზრდადობით, random-ად,
# მხოლოდ უნიკალური მონაცემები დატოვოს.
# რომელსაც აირჩევს უნდა გამოვიდეს ზუსტად ისე დალაგებული სია.

import random

def get_numbers_from_user():
    while True:
        user_input = input("Enter numbers separated by spaces: ").strip()

        try:
            numbers = [float(num) for num in user_input.split()]
            return numbers
        except ValueError:
            print("Error: Please enter only numbers separated by spaces.")


def sort_numbers(numbers, choice):
    if choice == 1:  # Ascending
        return sorted(numbers)
    elif choice == 2:  # Descending
        return sorted(numbers, reverse=True)
    elif choice == 3:  # Random
        random.shuffle(numbers)
        return numbers
    elif choice == 4:  # Unique only
        return set(numbers)
    else:
        return numbers


numbers = get_numbers_from_user()

print("\nHow would you like to sort these numbers?")
print("1. Ascending order")
print("2. Descending order")
print("3. Random order")
print("4. Unique values only")

while True:
    try:
        choice = int(input("\nEnter your choice (1-4): "))
        if 1 <= choice <= 4:
            break
        else:
            print("Please enter a number between 1 and 4.")
    except ValueError:
        print("Please enter a valid number.")

result = sort_numbers(numbers, choice)
print(result)