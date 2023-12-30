from dataclasses import dataclass

from handler.models.image import Image
from handler.storage.base import BaseObjs

class ImageObjs(BaseObjs):
	def __init__(self):
		self.objs= []

	def append(self, obj):
		self.objs.append(obj)

	def extend(self, obj):
		self.objs.extend(obj)

	def clear(self):
		self.objs = []