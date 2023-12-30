from dataclasses import dataclass
from abc import ABC, abstractmethod
from tkinter import messagebox

from handler.models.display import Point, Region
from handler.models.image import Image
from handler.models.mouse import MouseButton
from handler.models.text import Text

from handler.computer.mouse import Mouse
from handler.computer.keyboard import Keyboard
from handler.computer.display import Display
from handler.computer.speaker import Speaker
from handler.computer.time import Time
from handler.computer.speaker import Speaker

from handler.checker.display import DisplayChecker

from handler.storage.objsVariables.action import Actions


mouse=Mouse()
keyboard=Keyboard()


class MoveMouse(Actions):
    """docstring for MoveMouse"""
    def record(self) -> "MoveMouse":
        messagebox.askquestion('askquestion', 'navigate to the point you want to click after cliking ok')
        self.point = Display.getMousePoint()
        return self
    
    def directRecord(self, point: Point) -> None:
        self.point = point
        return self
    
    def run(self):
        mouse.moveTo(self.point)


class FindImage(Actions):
    """docstring for FindImage"""  
    def record(self, grayscale: bool = False, confience: float = 0.9):
        self.grayscale      = grayscale
        self.confience      = confience
        messagebox.askquestion('askquestion', 'now select the area of image')
        region_of_image = Display.regionSelector(askForFullScreen=False)
        messagebox.askquestion('askquestion', 'click yes to conform')
        self.image = Display.screenshot(region=region_of_image)
        messagebox.askquestion('askquestion', 'now select the area to FindImage it')
        self.region=Display.regionSelector()
        return self
    
    def directRecord(self, image : Image, grayscale: bool, confience: float, region: Region):
        self.image          = image
        self.grayscale      = grayscale
        self.confience      = confience
        self.region         = region
        return self
    
    def run(self):
        region = False
        while not region:
            region = Display.checkImage(image = self.image, grayscale = self.grayscale, confience = self.confience, region = self.region)
        mouse.moveTo(region.center())


class FindImageScrolling(Actions):
    """docstring for ScrollFindImageer"""
    def directRecord(self, image_name, grayscale, confience, region, point, scrollby):
        self.image           = image_name
        self.region          = region
        self.clspoint           = point
        self.grayscale       = grayscale
        self.confience       = confience
        self.scrollby        = scrollby
        self.scroll_direction= 1
        self.scroll_time     = 0.2
        return self
    
    def record(self, grayscale: bool, confience: float, x_scroll: int, y_scroll: int, scroll_time: float):
        self.grayscale = grayscale
        self.confience = confience
        self.x_scroll = x_scroll
        self.y_scroll = y_scroll
        self.scroll_time = scroll_time
        messagebox.askquestion('askquestion', 'now select the area of image')
        region_of_image = Display.regionSelector(askForFullScreen=False)
        messagebox.askquestion('askquestion', 'click yes to conform')
        self.image = Display.screenshot(region=region_of_image)
        messagebox.askquestion('askquestion', 'now select the area to Find Image while Scrolling')
        self.region = Display.regionSelector(askForFullScreen=True)
        messagebox.askquestion('askquestion', 'navigate to the point you want to put mouse to scroll')
        self.point = Display.getMousePoint()
        return self
    
    def run(self):
        mouse.moveTo(self.point)
        region = False
        while not region:
            mouse.scrollby(self.x_scroll, self.y_scroll)
            Time.wait(self.scroll_time)
            region = Display.checkImage(image = self.image, grayscale = self.grayscale, confience = self.confience, region = self.region)
        mouse.moveTo(region.center())


class Wait(Actions):
    """docstring for Wait"""
    def directRecord(self, time):
        self.time = time
        return self
    
    record = directRecord
    
    def run(self):
        Time.wait(self.time)


class Speak(Actions):
    """docstring for Wait"""
    def directRecord(self, text: Text):
        self.text = text
        return self

    record = directRecord

    def run(self):
        Speaker.speak(self.text)


class MouseClick(Actions):
    """docstring for MouseClick
       button which button left right or middle
    """
    def directRecord(self, button: MouseButton ,clicks: int = 1, interval: float = 0):
        self.button = button
        self.clicks = clicks
        self.interval = interval
        return self

    def record(self, clicks: int = 1, interval: float = 0):
        self.clicks=clicks
        self.interval=interval
        messagebox.askquestion(
            'Mouse Button selector', 
            'click the desired Mouse Button to record it\nafter clicking ok')
        self.button=mouse.getMouseButton()
        return self

    def run(self):
        for i in range(self.clicks):
            mouse.click(button=self.button)
            Time.wait(self.interval)

    def __str__(self):
        return f'MouseClick({self.button},{self.clicks},{self.interval})'
    def __repr__(self):
        return f'MouseClick({self.button},{self.clicks},{self.interval})'


class Scroll(Actions):
    """docstring for Scroll"""
    def directRecord(self, x: int = 0, y: int = 0): 
        self.x = x
        self.y = y
        return self

    record=directRecord

    def run(self):
        mouse.scrollBy(self.x, self.y)


class Write(Actions):
    """docstring for Write"""
    def directRecord(self, text: Text, interval: float):
        self.text = text
        self.interval = interval
        return self

    record = directRecord

    def run(self):
        keyboard.write(self.text, self.interval)
    

class PressKey(Actions):
    """docstring for Press"""
    def directRecord(self,key):
        self.key = key
        return self

    def record(self):
        self.key = keyboard.getKeyPressed()
        return self

    def run(self):
        keyboard.press(self.key)


class ReleaseKey(Actions):
    """docstring for Release"""
    def directRecord(self,key):
        self.key = key
        return self

    def record(self):
        self.key = keyboard.getKeyReleased()
        return self

    def run(self):
        keyboard.release(self.key)


class Screenshot(Actions):
    """docstring for Screenshot"""
    def directRecord(self,save_by_name, region):
        self.save_by_name = save_by_name
        self.region = region

    def record(self,save_by_name):
        self.save_by_name = save_by_name
        messagebox.askquestion('askquestion', 'now select the area to take Screenshot')

    def run(self):
        Display.screenshot(name=self.save_by_name, region=self.region)