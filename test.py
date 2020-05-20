import speech_recognition as sr


def speech_to_text(filename):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        print("okay")
    try:
        text = r.recognize_google(audio)
        print(f"You spoke: {text}")
        f = open(filename, "a+")
        f.write("\n" + text)
        f.close
        return True

    except:
        return False


def generate_default_words(seconds):
    normal = 60
    t = 60 / seconds
    print(150 / t)


generate_default_words(25)

# test
