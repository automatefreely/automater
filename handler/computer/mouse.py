from pynput.mouse import Controller as MouseController
from pynput import mouse

from handler.models.mouse import MouseButton
from handler.models.display import Point

class Mouse:
    """docstring for Mouse"""
    def __init__(self) -> None:
        self.mouse_ctrl=mouse.Controller()

    def moveTo(self, point: Point) -> None:
        self.mouse_ctrl.position = (point.x, point.y)

    def click(self, button: MouseButton) -> None:
        self.mouse_ctrl.click(button=button.value)

    def scrollBy(self, x: int, y: int) -> None:
        self.mouse_ctrl.scroll(-x, -y)

    def press(self, button: MouseButton) -> None:
        self.mouse_ctrl.press(button=button.value)

    def release(self, button: MouseButton) -> None:
        self.mouse_ctrl.release(button=button.value)

    @staticmethod
    def getMouseButton() -> MouseButton:
        with mouse.Events() as events:
            for event in events:
                try:
                    return MouseButton(event.button)
                except AttributeError:
                    continue

























    # def mouse(button, press) -> None:

    #     if button.type=="left" and press==True:
    #         self.mouse_ctrl.press(button='left')
    #     if button.type=="left" and press==False:
    #         self.mouse_ctrl.release(button='left')
    #     if button.type=="right" and press==True:
    #         self.mouse_ctrl.press(button='right')
    #     if button.type=="right" and press==False:
    #         self.mouse_ctrl.release(button='right')
    #     if button.type=="middle" and press==True:
    #         self.mouse_ctrl.press(button='middle')
    #     if button.type=="middle" and press==False:
    #         self.mouse_ctrl.release(button='middle')

		