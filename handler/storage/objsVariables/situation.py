from abc import ABC, abstractmethod

from handler.storage.base import BaseObjs
# import handler.storage.mainObject as mainObject

class Situation(ABC):
    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def directRecord(self) -> "Situation":
        pass

    @abstractmethod
    def record(self) -> "Situation":
        pass


class Situations():
    def __init__(self) -> None:
        self._situations: list[Situation] = []
        
    def append(self, obj):
        self._situations.append(obj)

    def extend(self, obj):
        self._situations.extend(obj)

    def clear(self):
        self._situations = []
        
    def run(self) -> None:
        for situation in self._situations:
            situation.run()
            
    def saveTo(self, mainObject) -> None:
        mainObject.appendAction(self)

class SituationsObjs(BaseObjs):
    """docstring for situations"""

    def __init__(self) -> None:
        self.objs = []

    def append(self, obj):
        self.objs.append(obj)

    def extend(self, obj):
        self.objs.extend(obj)

    def clear(self):
        self.objs = []