import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout
import speech_recognition as sr
import threading

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.is_listening = False

    def initUI(self):
        """
        Initialize the user interface.
        """
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Real-Time Audio Processing')

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        start_button = QPushButton('Start Recording')
        start_button.clicked.connect(self.start_recording)
        layout.addWidget(start_button)

        stop_button = QPushButton('Stop Recording')
        stop_button.clicked.connect(self.stop_recording)
        layout.addWidget(stop_button)

        self.setLayout(layout)

    def start_recording(self):
        """
        Start recording audio.
        """
        self.is_listening = True
        threading.Thread(target=self.listen_to_audio).start()

    def stop_recording(self):
        """
        Stop recording audio.
        """
        self.is_listening = False

    def listen_to_audio(self):
        while self.is_listening:
            try:
                with self.microphone as source:
                    audio = self.recognizer.listen(source)
                    text = self.recognizer.recognize_google(audio)
                    self.text_edit.append(text)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Error requesting speech recognition results: {e}")

def main():
    app = QApplication(sys.argv)  # Create QApplication instance here
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()