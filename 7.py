#7 ტექსტის ფილტრი
# მომხმარებელი შეჰყავს ტექსტი.
# ამოცანა: პროგრამამ უნდა წაშალოს ყველა ციფრი და სიმბოლო, დატოვოს მხოლოდ ასოები და
# სივრცეები.

def f(text):
    print("".join(char for char in text  if char.isalpha() or char.isspace()))

f('asdfghjn cgbn x g fg13423r fd^*  ^*  ygy gadd 42 r')