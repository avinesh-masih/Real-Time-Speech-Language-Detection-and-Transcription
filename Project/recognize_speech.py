import speech_recognition as sr
from speech_recognition import Recognizer, AudioData

class SpeechToText:
    def __init__(self):
        self.recognizer = Recognizer()

    def transcribe(self, audio):
        """
        Transcribe audio to text using Google Web Speech API.
        """
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError:
            return "Could not request results from service"