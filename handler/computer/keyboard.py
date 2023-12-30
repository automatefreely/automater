from pynput import keyboard

from handler.models.text import Text
from handler.models.keyboard import Key

from handler.computer.time import Time

class Keyboard:
    """docstring for Keyboard"""

    def __init__(self) -> None:
        self.keyboard_ctrl = keyboard.Controller()

    def press(self, key: Key) -> None:
        self.keyboard_ctrl.press(key)

    def release(self, key: Key) -> None:
        self.keyboard_ctrl.release(key)

    def fastWrite(self, text: Text) -> None:
        self.keyboard_ctrl.type(str(text))

    def write(self, text: Text, interval: float) -> None:
        [(self.fastWrite(Text(letter)), Time.wait(interval)) for letter in str(text)]

    @staticmethod
    def get_key(pressed=True) -> None:
        with keyboard.Events() as events:
            for event in events:
                if isinstance(event, keyboard.Events.Press) == pressed:
                    return event.key
                elif isinstance(event, keyboard.Events.Release) != pressed:
                    return event.key

    def getKeyPressed(self) -> Key:
        return self.get_key(True)

    def getKeyReleased(self) -> Key:
        return self.get_key(False)