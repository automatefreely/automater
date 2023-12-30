import pyautogui
from time import sleep
from typing import Union
from tkinter import messagebox

from handler.models.color import Color
from handler.models.display import Point, Region
from handler.models.image import Image

class Display:
    """Handles things related to display"""
    @staticmethod
    def screenshot(region: Region=Region()) -> Image:
        image_obj = pyautogui.screenshot(region=(region.l_t.x, region.l_t.y, region.w, region.h))
        return Image(image_obj)
    @staticmethod
    def getMousePoint(time: float = 3) -> Point:
        #pyautogui.PAUSE = 1
        sleep(time)
        x , y = pyautogui.position()
        return Point(x, y)
    @classmethod
    def regionSelector(cls, askForFullScreen: bool = True) -> Region:
        if askForFullScreen==True and messagebox.askquestion('Automater | Finder','full screen or not') == "yes":
            return Region()
        messagebox.showinfo('Area Selector | Finder','navigate to top-left point after cliking ok')
        l_t=left_top_point=cls.getMousePoint()
        messagebox.showinfo('Area Selector | Finder','navigate to bottum-right point after cliking ok')
        r_b=right_botton_point=cls.getMousePoint()
        return Region(l_t,r_b)
    @staticmethod
    def checkImage(image: Image, region: Region, grayscale: bool, confience: float) -> Union[bool, Region]:
        if confience!=1:
            box=pyautogui.locateOnScreen(image.image_obj, 
                region=(region.l_t.x, region.l_t.y, region.width, region.height),
                confidence=confience,
                grayscale=grayscale)
        elif confience==1:
            box=pyautogui.locateOnScreen(image.image_obj, 
                region=(region.l_t.x, region.l_t.y, region.width, region.height),
                grayscale=grayscale)
        try:
            point=pyautogui.center(box)
            return Region(Point(box.left, box.top), Point(box.left + box.width, box.top + box.height))
        except TypeError:
            return False
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
        
























    # def screenshot(self, time=0, name="screen", region: Region=Region()):
    #     # point1,point2=region[0],region[1]
    #     # x1,y1=region.point1.get_tuple()
    #     # x2,y2=region.point2.get_tuple()
    #     # sleep(float(time))
    #     # left=int(x1)
    #     # top=int(y1)
    #     # width=int(x2)-int(x1)
    #     # height=int(y2)-int(y1)
    #     # myscreenshot=pyautogui.screenshot(region=(left, top, width, height))
    #     myscreenshot=pyautogui.screenshot(region=(region.l_t.x, region.l_t.y, region.w, region.h))