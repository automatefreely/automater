from dataclasses import dataclass
import pyttsx3

from handler.models.text import Text
@dataclass
class Speaker:
    """docstring for Speaker"""
    @staticmethod
    def speak(text: Text) -> "Speaker":
        engine = pyttsx3.init()
        engine.say(str(text))
        engine.runAndWait()