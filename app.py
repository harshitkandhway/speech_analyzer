from util import utils
from speech_converter import speech_to_text
from grammar_rater import rate_grammar
from grammar_rater import rate_unnecessary_fillers

filename = "speech.txt"


if speech_to_text(filename):
    data = utils.read_file(filename)
    words_count = utils.total_words(data)
    print(words_count)
    fluency_rating = utils.rate_speech_on_fluency(words_count)
    print(fluency_rating)
    grammar_rating = rate_grammar(data, words_count)
    print(grammar_rating)
    filler_rating = rate_unnecessary_fillers(data)
    print(filler_rating)
    total_rating = fluency_rating + grammar_rating + filler_rating
    print(total_rating)
