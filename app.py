from util.utils import total_words
from util.utils import rate_speech_on_fluency
from util.utils import read_file
from speech_converter import speech_to_text
from grammar_rater import rate_grammar

filename = "speech.txt"

data = read_file(filename)
rate_grammar(data)

# if speech_to_text(filename):
#     data = read_file(filename)
#     words_count = total_words(data)
#     print(words_count)
#     fluency_rating = rate_speech_on_fluency(words_count)
#     print(fluency_rating)
#     rate_grammar(data)
