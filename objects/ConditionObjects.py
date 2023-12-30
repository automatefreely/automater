from tkinter import messagebox

from handler.computer.display import Display
from handler.models.display import Region
from handler.models.image import Image
from handler.storage.objsVariables.situation import Situation, Situations
from handler.storage.objsVariables.condition import Condition, ConditionObjs


class IfImageCondition(Condition):
    def directRecord(self, image: Image, grayscale: bool, confience: float, region: Region):
        self.image = image
        self.grayscale = grayscale
        self.confience = confience
        self.region = region
        return self
    
    def record(self, grayscale: bool, confience: float):
        self.grayscale = grayscale
        self.confience = confience
        messagebox.askquestion('askquestion', 'now select the area of image')
        region_of_image = Display.regionSelector(askForFullScreen=False)
        messagebox.askquestion('askquestion', 'click yes to conform')
        self.image = Display.screenshot(region=region_of_image)
        messagebox.askquestion('askquestion', 'now select the area to search it')
        self.region=Display.regionSelector()
        return self

    def check(self) -> bool:
        return Display.checkImage(
            image=self.image, grayscale=self.grayscale, 
            confience=self.confience, region=self.region)