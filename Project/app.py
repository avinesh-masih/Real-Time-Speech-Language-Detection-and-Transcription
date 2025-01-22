import sys
from PyQt5.QtWidgets import QApplication
from speech_recognition import Recognizer
from recognize_speech import SpeechToText
from language_detection import LanguageDetector
from gui import GUI

class Application:
    def __init__(self):
        self.speech_recognizer = Recognizer()
        self.speech_to_text = SpeechToText()
        self.language_detector = LanguageDetector()
        self.gui = GUI()

    def run(self):
        """
        Run the application.
        """
        app = QApplication(sys.argv)
        self.gui.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    application = Application()
    application.run()