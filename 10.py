#10 მომხმარებელს შეჰყავს წინადადება,
# ამოცანა: გამოიანგარიშე თითოეული სიტყვის სიგრძე და დააბრუნე dictionary
# მაგალითად: "Python is fun" → {"Python": 6, "is": 2, "fun": 3}

def calculate_word_lengths(sentence):
    words = sentence.split()
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths

while True:
    user_input = input("\nEnter a sentence (or 'quit' to exit): ").strip()
    result = calculate_word_lengths(user_input)
    print(f"\nDictionary: {result}")