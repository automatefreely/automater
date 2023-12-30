from abc import ABC, abstractmethod

from handler.storage.base import BaseObjs


class Condition(ABC):
    @abstractmethod
    def record(self):
        pass
    @abstractmethod
    def directRecord(self):
        pass
    @abstractmethod
    def check(self) -> bool:
        pass


class ConditionObjs(BaseObjs):
	def __init__(self):
		self.objs= []

	def append(self, obj):
		self.objs.append(obj)

	def extend(self, obj):
		self.objs.extend(obj)

	def clear(self):
		self.objs = []