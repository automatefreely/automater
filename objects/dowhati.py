import time
from pynput.keyboard import Listener as KeyboardListener, Key
from pynput.mouse import Listener as MouseListener
from objects.ActionObjects import *

from handler.storage.mainObject import MainObject

from handler.models.display import Point
from handler.models.mouse import MouseButton

class Listener():
    def __init__(self):
        self.mainObject = MainObject()

    def start(self):
        self.tic = time.perf_counter()
        self.mouseListener = MouseListener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.mouseListener.start()
        self.keyboardListener = KeyboardListener(on_press=self.on_press, on_release=self.on_release)
        self.keyboardListener.start()
        self.mouseListener.join()
        self.keyboardListener.join()

    # def stop(self):
    #     self.mouseListener.stop()
    #     self.keyboardListener.stop()
        # print("\n"+"*"*50)
        # for action in self.mainObject.actionList():
        #     print(action)
        # print("*"*50)
    def on_move(self, x, y):
        MoveMouse().directRecord(point=Point(x, y)).saveTo(self.mainObject)
        self.timegap()

    def on_click(self, x, y, button, pressed):
        MouseClick().directRecord(button = MouseButton(button)).saveTo(self.mainObject)
        self.timegap()

    def on_scroll(self, x, y, dx, dy):
        Scroll().directRecord(y = dy).saveTo(self.mainObject) #check
        self.timegap()

    def on_press(self, key):
        if key == Key.esc:
            self.mouseListener.stop()
            return False
            # self.stop()
        PressKey().directRecord(key = key).saveTo(self.mainObject)
        self.timegap()

    def on_release(self, key):
        ReleaseKey().directRecord(key = key).saveTo(self.mainObject)
        self.timegap()


    def timegap(self):
        tac = time.perf_counter()
        timegap, self.tic = tac - self.tic, tac
        Wait().directRecord(time = timegap).saveTo(self.mainObject)
