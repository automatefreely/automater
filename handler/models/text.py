from dataclasses import dataclass

@dataclass
class Text:
	text: str
	def __str__(self) -> str:
		return self.text