#1 დაწერეთ პაროლის გენერატორი.
# დავალების შესრულებაში დაგეხმარებათ: random მოდული, while ან for ციკლი, list,
# სტრიქონის ფორმატირება.
# input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა
# სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ
# არა სიმბოლოები, რიცხვები, დიდი/პატარა ასოები (ლათინურად) თუ ქართულს შემოიტანს
# უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”
import string
import random


def generate_password():
    final_chars = ""
    for param, value in params.items():
        if info[param]:
            final_chars += value
    if final_chars == "":
        return "\nარ გირჩევთ ამ პაროლის გამოყენებას!"
    password = ""
    for _ in range(length):
        password += random.choice(final_chars)

    return password

def get_user_input():
    print("მომდევნო შეკითხვებზე გთხოვთ გასცეთ პასუხი: კი (yes, y) ან არა (no, n)")

    for param in params.keys():
        info[param] = choose(param)

def get_password_length():
    while True:
        try:
            length = int(input("სასურველი პაროლის სიგრძე: "))
            if length <= 0:
                print("პაროლის სიგრძე უნდა იყოს დადებითი რიცხვი!")
                continue
            return length
        except ValueError:
            print("სიგრძე უნდა იყოს მთელი რიცხვი!")

def choose(param):
    while True:
        has_param = input(f"გსურთ, რომ პაროლში შედიოდეს {param}?\n").lower()
        if has_param in ("yes", "y"):
            return True
        elif has_param in ("no", "n"):
            return False
        else:
            print("პასუხი უნდა შემოიყვანოთ ლათინური ასოებით!")

info = {}
params = {
    "სიმბოლოები" : string.punctuation,
    "რიცხვები" : string.digits,
    "დაბალი რეგისტრის ასოები" : string.ascii_lowercase,
    "მაღალი რეგისტრის ასოები" : string.ascii_uppercase
}

print("პაროლის დასგენერირებლად დაგვჭირდება რამდენიმე პარამეტრის თქვენთან ერთად არჩევა.")
print("გთხოვთ, უპასუხოთ შემდეგ შეკითხვებს:")
length = get_password_length()
get_user_input()
print(f"თქვენი დაგენერირებული პაროლია: {generate_password()}")