# Real-Time Speech Language Detection and Transcription

## Table of Contents 
- [Overview](#overview) 
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview
This project provides a Python-based application that performs real-time speech-to-text transcription and language detection using pre-trained machine learning models. It features a user-friendly graphical interface built with PyQt5 and is designed for seamless real-time processing.

---

## Features
- **Real-time Speech Recognition**: Converts spoken words into text.
- **Language Detection**: Identifies the language of the spoken words.
- **Graphical User Interface (GUI)**: Built with PyQt5 for ease of use.
- **Multi-threading**: Ensures smooth audio processing without freezing the UI.

---

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/avinesh-masih/Real-Time-Speech-Language-Detection-and-Transcription.git
   ```



2. Install the required dependencies:

   ```bash
   pip install SpeechRecognition
   pip install PyQt5
   pip install langdetect
   pip install pyaudio
   pip install google-api-python-client
   ```

---

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Use the buttons in the GUI:
   - **Start Recording**: Begins recording audio from the microphone.
   - **Stop Recording**: Ends the recording session.

3. View transcriptions in the text area of the GUI.

---

## Code Structure

### Main Components

- **`GUI` Class**: 
  - Defines the application layout and logic.
  - Handles user interactions (button clicks).

- **Audio Handling**:
  - Utilizes `speech_recognition.Recognizer` and `speech_recognition.Microphone` for capturing and processing audio input.
  - Incorporates ambient noise adjustment for better transcription quality.

---

## Troubleshooting

1. **"No module named PyQt5"**:
   - Ensure PyQt5 is installed:
     ```bash
     pip install PyQt5
     ```

2. **"No module named speech_recognition"**:
   - Install the library:
     ```bash
     pip install speech_recognition
     ```

3. **Issues with Audio Input**:
   - Verify your microphone is connected and configured correctly.
   - Use `pyaudio` for better microphone support:
     ```bash
     pip install pyaudio
     ```

---

## Contributing

Contributions are welcome! Fork the repository and create a pull request with your changes.

---

## License

This project is protected under a custom license. Unauthorized use, modification, distribution, or reproduction of the code and any associated materials is strictly prohibited without explicit written permission from the author.

---

## Contact

For inquiries or permissions or contribute to this project, please reach out via:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/avineshlko/)[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=githubpages&logoColor=white)](https://avinesh-masih.github.io/)[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:skmasih11@gmail.com)
