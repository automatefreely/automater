from dataclasses import dataclass, field
import pyautogui

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
	@classmethod
	def tuple_to_point(cls, t: tuple) -> "Point":
		return cls(*tuple)
	def get_tuple(self) -> tuple:
		return (self.x, self.y)
	def is_in(self, region: "Region") -> bool:
		return region.l_t.y <= self.y <= region.l_b.y and region.l_t.x <= self.x <= region.r_t.x

@dataclass
class Region:
	"""docstring for Region"""
	left_top_point: Point = field(default_factory=lambda: Point(0,0))
	right_botton_point: Point = field(default_factory=lambda: Point(*pyautogui.size()))
	def __post_init__(self) -> None:
		self.left_botton_point = Point(self.left_top_point.x, self.right_botton_point.y)
		self.right_top_point = Point(self.right_botton_point.x, self.left_top_point.y)
		self.width = self.right_botton_point.x - self.left_top_point.x 
		self.height = self.right_botton_point.y - self.left_top_point.y
		# abbrivations
		self.l_t = self.left_top_point
		self.l_b = self.left_botton_point
		self.r_t = self.right_top_point
		self.r_b = self.right_botton_point
		self.w = self.width
		self.h = self.height
	def center(self) -> Point:
		return Point((self.l_t.x+self.r_b.x)/2, (self.l_t.y+self.r_b.y)/2)
	def __contains__(self, point: Point):
		return self.l_t.y <= point.y <= self.l_b.y and self.l_t.x <= point.x <= self.r_t.x