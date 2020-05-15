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
        return true

    except:
        return false