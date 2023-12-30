from abc import ABC, abstractmethod
from dataclasses import dataclass, field

# from actions.objects import Actions
class BaseObjs(ABC):
	# def __init__(self):
	# 	objs: list = []
	@abstractmethod
	def append(self, obj):
		pass
	@abstractmethod
	def extend(self, obj):
		pass
	@abstractmethod
	def clear(self):
		pass