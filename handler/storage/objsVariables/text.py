from dataclasses import dataclass, field
from typing import List


from handler.models.text import Text
from handler.storage.base import BaseObjs

class TextObjs(BaseObjs):
	def __init__(self):
		self.objs= []

	def append(self, obj):
		self.objs.append(obj)
		
	def extend(self, obj):
		self.objs.extend(obj)
		
	def clear(self):
		self.objs = []