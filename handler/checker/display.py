import pyautogui

from handler.models.image import Image
from handler.models.display import Region, Point
from handler.models.color import Color
from handler.computer.display import Display

class DisplayChecker():
    @staticmethod
    def checkImage(image: Image, grayscale: bool, confience: float, region: Region):
        return bool(Display.findImage(image, grayscale, confience, region))
    @staticmethod
    def checkColor(point: Point, color: Color,confidence):
        # pyautogui.pixelMatchesColor(x1,y1, (130, 135, 144))
        return pyautogui.pixelMatchesColor(point.x, point.y, color.rgb, tolerance=confidence)
    # @staticmethod
    # def onClickingImage(image_obj: Image, grayscale: bool, confience: float, region: Region) -> None:
    #     # 1. get image
    #     image = image_obj
    #     # 2. search for the image and get region
    #     region = False
    #     while not region:
    #         region = Display.findImage(image, grayscale, confience, region)
    #     # 3. return when click on that region
    #     waitUntillMousePress(region=region)
    