from time import sleep
from typing import Union

from handler.models.keyboard import Key
from handler.models.display import Region, Point
from pynput import keyboard
from pynput import mouse
from handler.models.mouse import MouseButton
class Time:
    """docstring for Time"""
    @staticmethod
    def wait(time: Union[int, float]) -> None:
        sleep(time)
    
    @staticmethod
    def wait_untill_key(key: Key, press: bool):
        with keyboard.Events() as events:
            for event in events:
                if event.key == key and isinstance(event, keyboard.Events.Press) == press:
                    break
    
    @classmethod
    def waitUntillKeyPress(cls, key: Key) -> "Time":
    	return cls.wait_untill_key(key, True)
    
    @classmethod
    def waitUntillKeyRelease(cls, key: Key) -> "Time":
        return cls.wait_untill_key(key, False)

    @staticmethod
    def wait_untill_mouse(mouseButton: MouseButton = MouseButton.LEFT, press: bool = True, region: Region = Region()) -> "Time":
        with mouse.Events() as events:
            for event in events:
                try:
                    if event.button == mouseButton.value and event.pressed == press and Point(event.x, event.y).is_in(region):
                        break
                except Exception as e:
                    continue
    @classmethod
    def waitUntillMousePress(cls, mouseButton: MouseButton = MouseButton.LEFT, region: Region = Region()) -> "Time":
        return cls.wait_untill_mouse(mouseButton, True, region)
    
    @classmethod
    def waitUntillMouseRelease(cls, mouseButton: MouseButton = MouseButton.LEFT, region: Region = Region()) -> "Time":
        return cls.wait_untill_mouse(mouseButton, False, region)