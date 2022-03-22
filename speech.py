import speech_recognition as sr 

r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        audio = r.recognize(source)
        return audio

def audio_to_text(audio):
    text = ''
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print ("don't understood")
    except sr.RequestError:
        print ("API Error")
    return text

if __name__ == "__main__":
    a = get_audio()
    print (audio_to_text(a))
    





