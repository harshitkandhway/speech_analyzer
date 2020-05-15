def total_words(data):
    words = data.split()
    count = 0
    for word in words:
        if word != "." and word != ",":
            count = count + 1
    return count


def read_file(filename):
    try:
        file = open(filename, "rt")
        data = file.read()
        return data
    except FileNotFoundError:
        print(f"No file found with name {filename}")


def rate_speech_on_fluency(words_count):
    avg_words = 45
    if abs(avg_words - words_count) <= 5:
        return 1
    if words_count >= 70 or words_count <= 30:
        return 0
    if words_count >= 60 or words_count <= 35:
        return 0.5
    if words_count >= 55 or words_count <= 40:
        return 0.7
