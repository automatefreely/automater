from dataclasses import dataclass

from handler.models.display import Point, Region
from handler.storage.base import BaseObjs

class RegionObjs(BaseObjs):
	def __init__(self):
		self.objs= []

	def append(self, obj):
		self.objs.append(obj)

	def extend(self, obj):
		self.objs.extend(obj)

	def clear(self):
		self.objs = []

class PointObjs(BaseObjs):
	def __init__(self):
		self.objs= []

	def append(self, obj):
		self.objs.append(obj)

	def extend(self, obj):
		self.objs.extend(obj)

	def clear(self):
		self.objs = []