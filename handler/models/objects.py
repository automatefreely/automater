from dataclasses import dataclass
from enum import Enum

@dataclass
class Point:
	"""docstring for Point"""
	x: int = 0
	y: int = 0
	def __post_init__(self) -> None:
		if self.x < 0 and self.y < 0:
			raise Exception("Sorry, no co-ordinate below zero")
	def __add__(self, point: "Point") -> "Point":
		return Point(self.x+point.x, self.y+point.y)
	def __sub__(self, point: "Point") -> "Point":
		return Point(self.x-point.x, self.y-point.y)
	def __ne__(self, point: "Point") -> bool:
		return not (point.x==self.x and point.y==self.y)
	def __eq__(self, point: "Point") -> bool:
		return (point.x==self.x and point.y==self.y)

class MouseButtonType(Enum):
	"""docstring for ButtonType"""
	LEFT 		= "left"
	MIDDLE 		= "middle"
	RIGHT 		= "right"
		
@dataclass
class MouseButton:
	"""docstring for Button"""
	button_type: MouseButtonType = MouseButtonType.LEFT
	def type(self):
		return button_type.value