#9 მომხმარებელი შეჰყავს ნებისმიერი ტექსტი, მოძებნე,
# რომელი სიტყვა მეორდება ტექსტში ყველაზე მეტჯერ.
# მაგ: "Python is great and python is easy" → ყველაზე ხშირია
# "python". თუ ორი ან მეტი სიტყვაა ტოლი, დააბრუნე ყველა.

def find_most_frequent_words(text):
    words = text.lower().split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    if not word_count:
        return []

    max_frequency = max(word_count.values())
    most_frequent = [word for word, count in word_count.items() if count == max_frequency]

    return most_frequent, max_frequency


while True:
    user_input = input("\nEnter text (or 'quit' to exit): ").strip()

    if user_input.lower() == 'quit':
        break

    most_frequent, frequency = find_most_frequent_words(user_input)

    if len(most_frequent) == 1:
        print(f"Most frequent word: '{most_frequent[0]}' (appears {frequency} times)")
    else:
        print(f"Most frequent words (each appears {frequency} times):")
        for word in most_frequent:
            print(f"  '{word}'")

