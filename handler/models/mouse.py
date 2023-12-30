from pynput.mouse import Button
from enum import Enum

class MouseButton(Enum):
    """docstring for ButtonType"""
    LEFT = Button.left
    MIDDLE = Button.middle
    RIGHT = Button.right

