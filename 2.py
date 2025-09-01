#2 პაროლის შეფასება
# ამოცანა: მომხმარებლის შეყვანილი პაროლი შეაფასე 0–10 შკალით: სიგრძე, ციფრები, სიმბოლოები,
# დიდი/პატარა ასოები, განმეორებადი სიმბოლოების არსებობა.
# მოთხოვნები: გამოიტანე “weak/medium/strong”.
import string

def evaluate_password_strength(password : str):
    score = 0

    length = len(password)
    if length >= 14:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    print(score)
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    print(score)
    repeated = len(password) - len(set(password))
    if repeated > 2:
        score -= 1
    elif 0 < repeated <= 2:
        score += 2
    else:
        score += 3
    print(score)
    score = max(0, min(10, score))
    print(score)
    if score <= 3:
        strength = "weak"
    elif score <= 6:
        strength = "medium"
    else:
        strength = "strong"

    return score, strength

