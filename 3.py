#3 დაწერე ფუნქცია (ფიბონაჩის რიგი) - *რა არის ფიბონაჩი - ბოლო ორი ელემენტის ჯამით ვამატებთ
# ახალ რიცხვს*, სანამ სიგრძე არ გახდება მომხმარებლის მიერ შემოყვანილი რიცხვი, აუცილებლად
# უნდა შემოიტანოს რიცხვი, სხვა რამის შემოტანის დროს უნდა შემოწმდეს რა შემოიტანა
# მომხმარებელმა და უნდა დაუსახელო აღნიშნული და უთხრა რომ მხოლოდ რიცხვი შემოიტანოს. მაგ:
# შემოიტანა სიმბოლო, უნდა უთხრა შენ შემოიტანე სიმბოლო არასწორია, მხოლოდ რიცხვი!

def f():
    while True:
        user_input = input("Please enter a number: ").strip()

        if not user_input:
            print("You entered nothing. Please enter a number!")
            continue

        if user_input.isdigit():
            n = int(user_input)
            if n > 0:
                break
            else:
                print("Please enter a positive number greater than 0!")
        else:
            if any(char.isalpha() for char in user_input):
                print(f"You entered text/symbols '{user_input}'.\nOnly numbers are allowed!")
            elif any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in user_input):
                print(f"You entered special characters '{user_input}'.\nOnly numbers are allowed!")
            else:
                print(f"Invalid input '{user_input}'. Please enter only numbers.")

    f_nums = []

    if n >= 1:
        f_nums.append(0)
    if n >= 2:
        f_nums.append(1)

    for i in range(2, n):
        next = f_nums[i - 1] + f_nums[i - 2]
        f_nums.append(next)

    return f_nums

print(f())