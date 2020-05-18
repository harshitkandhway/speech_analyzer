from enchant.checker import SpellChecker
import nltk

chkr = SpellChecker("en_US")
VERB_CODES = {
    "VB",  # Verb, base form
    "VBD",  # Verb, past tense
    "VBG",  # Verb, gerund or present participle
    "VBN",  # Verb, past participle
    "VBP",  # Verb, non-3rd person singular present
    "VBZ",  # Verb, 3rd person singular present
}


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


def rate_grammar(data):
    words = data.split()
    count = 0
    for index, word in enumerate(words):
        if word == "has" or word=have:
            if is_VBN(words[index + 1], "VBN"):
                count = count + 1
    if count == 0:
        return 1
    if count >= 4:
        return 0
    if count >= 2:
        return 0.5
    if count == 1:
        return 0.7


def is_VBN(word, code):
    result = nltk.pos_tag(word.split())
    word_code = result[0][1]
    if word_code == code:
        return True
    return False


def rate_spelling(data, total_words):
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
