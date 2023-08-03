import speech_recognition as sr


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something :')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, 1)
        audio = r.listen(source)

        try:
            task = r.recognize_google(audio, language='en-us').lower()
            print(task)
        except sr.UnknownValueError:
            print('I cannot understand you')
            task = command()

        return task


command()
