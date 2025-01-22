import langdetect

class LanguageDetector:
    def __init__(self):
        pass

    def detect_language(self, text):
        """
        Detect the language of the given text.
        """
        try:
            language = langdetect.detect(text)
            return language
        except langdetect.lang_detect_exception.LangDetectException:
            return "Language detection failed"