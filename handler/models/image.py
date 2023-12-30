from dataclasses import dataclass
import PIL

@dataclass
class Image:
	"""docstring for Image"""
	image_obj: PIL.Image.Image
	def save(self, image_name: str = "screen") -> None:
		self.image_obj.save()