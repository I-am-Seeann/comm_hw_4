#4 პალინდრომი
# ამოცანა: შეამოწმე, არის თუ არა შეყვანილი ტექსტი პალინდრომი
# (მხოლოდ ასოები/ციფრები).
# თუ არაა, შესთავაზე ყველაზე ახლო პალინდრომი ერთი სიმბოლოს ჩასმით/წაშლით.

def is_palindrome(text):
    cleaned = ''.join(char for char in text if char.isalnum()).lower()
    return cleaned == cleaned[::-1]


def find_closest_palindrome(text):
    for i in range(len(text)):
        new_text = text[:i] + text[i+1:]
        if is_palindrome(new_text):
            return new_text

    return text
while True:
    user_input = input("\nEnter text: ").strip()

    if not user_input:
        print("You entered nothing.")
        continue

    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")

        closest = find_closest_palindrome(user_input)

        if closest != user_input:
            print(f"Closest palindrome is: '{closest}'")


