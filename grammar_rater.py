from enchant.checker import SpellChecker

chkr = SpellChecker("en_US")


def rate_unnecessary_fillers(data):
    # yeah,you know,like
    words = data.split()
    count = 0
    for word in words:
        if word.lower() == "like".lower():
            count = count + 1
    if count >= 3:
        return 0
    if count == 2:
        return 0.6
    else:
        return 1


def rate_grammar(data, total_words):
    chkr.set_text(data)
    misspelled_words = 0
    for err in chkr:
        print("ERROR:", err.word)
        misspelled_words = misspelled_words + 1
    error_per = misspelled_percentage(total_words, misspelled_words)
    return rate_misspelled_percentage(error_per)


def misspelled_percentage(total_words, misspelled_words):
    return round(misspelled_words / total_words * 100, 2)


def rate_misspelled_percentage(error_per):
    if error_per >= 50:
        return 0
    if error_per >= 30 and error_per < 50:
        return 0.5
    if error_per >= 20 and error_per < 30:
        return 1
    if error_per >= 10 and error_per < 20:
        return 1.5
    if error_per >= 5:
        return 1.7
    else:
        return 2
