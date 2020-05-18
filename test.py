def print_word(word):
    print(word)


data = "I have"
words = data.split()
for index, word in enumerate(words):
    if word == "have":
        print_word(words[index + 1])
    # print(index, word)
