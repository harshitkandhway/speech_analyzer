from util import utils
from speech_converter import speech_to_text
from grammar_rater import rate_spelling
from grammar_rater import rate_unnecessary_fillers
from grammar_rater import rate_grammar

filename = "speech.txt"
line_format = "==============================================="

if speech_to_text(filename):
    data = utils.read_file(filename)
    words_count = utils.total_words(data)
    print(line_format)
    print("total spoken words                     -> ", words_count)
    print(line_format)
    fluency_rating = utils.rate_speech_on_fluency(words_count)
    print("fluency rating              (out of 1) -> ", fluency_rating)
    spelling_rating = rate_spelling(data, words_count)
    print("spelling rating             (out of 2) -> ", spelling_rating)
    filler_rating = rate_unnecessary_fillers(data)
    print("unnecessary fillers rating  (out of 1) -> ", filler_rating)
    grammar_rating = rate_grammar(data)
    print("grammar rating              (out of 1) -> ", grammar_rating)
    print(line_format)
    total_rating = fluency_rating + spelling_rating + filler_rating + grammar_rating
    print("overall rating              (out of 5) -> ", total_rating)
    print(line_format)