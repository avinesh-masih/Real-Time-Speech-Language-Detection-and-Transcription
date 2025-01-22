import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_audio(self):
        with sr.Microphone() as source:
            try:
                audio = self.recognizer.record(source)
                return audio
            except sr.RequestError:
                return "Could not request results from the service"
            except sr.UnknownValueError:
                return "Could not understand the audio"