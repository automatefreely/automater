from dataclasses import dataclass

@dataclass
class Color:
	red: int
	green: int
	blue: int
	alpha: float
	def __post_init__(self) -> None:
		self._rgb=(self.red, self.green, self.blue)
	@property
	def rgb(self) -> tuple:
		return self._rgb
	