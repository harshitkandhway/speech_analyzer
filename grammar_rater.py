from enchant.checker import SpellChecker

chkr = SpellChecker("en_US")


def rate_grammar(data, total_words):
    chkr.set_text(data)
    count = 0
    for err in chkr:
        print("ERROR:", err.word)
        count = count + 1
    if (total_words / 2 - count) <= 0:
        return 0
