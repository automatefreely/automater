import pickle
import os

from handler.storage.objsVariables import action, display, image, situation, text

class MainObject():
	"""all the objects created are stored here
	"""
	def __init__(self) -> None:
		self.action_objects 	= action.ActionObjs()
		self.text_objects 		= text.TextObjs()
		self.image_objects 		= image.ImageObjs()
		self.region_objects 	= display.RegionObjs()
		self.point_objects 		= display.PointObjs()
		self.situation_objects 	= situation.SituationsObjs()

	@property
	def list_of_objs(self):
		_list_of_objs = [
			self.action_objects, 
			self.text_objects, 
			self.image_objects, 
			self.region_objects, 
			self.point_objects, 
			self.situation_objects
			]
		return _list_of_objs
	
	def save(self, file_name: str) -> None:
		with open(file_name+".txt","wb") as file:
			pickle.dump(self, file)
		
	def load(self, file_name: str, append: bool=False) -> "MainObject":
		with open(file_name+".txt","rb") as file:
			mainObject=pickle.load(file)
		if append==True:
			self.extend(mainObject)
			return self
		self.clear()
		self.extend(mainObject)
		return self

	def appendAction(self, action: action.Actions) -> "MainObject":
		self.action_objects.append(action)
		return self

	def extend(self, anotherMainObject: "MainObject") -> "MainObject":
		"""join to MainObject

		Args:
			anotherMainObject (MainObject): to join to Main Object

		Returns:
			MainObject: it returns again a main object
		"""
		[self_objs.extend(other_objs.objs) for (self_objs, other_objs) in zip(self.list_of_objs, anotherMainObject.list_of_objs)]
		return self

	def clear(self) -> None:
		[objs.clear() for objs in self.list_of_objs]

	def popAction(self) -> None:
		self.action_objects.pop()

	def run(self) -> None:
		# [action.run() for action in self.action_objects.objs]
		self.action_objects.run()

	def actionList(self) -> None:
		return (action for action in self.action_objects.objs)

	def app(self, name: str) -> None:
		with open(name+".py", "wb") as f:
			f.write(self)
		command = "pyinstaller {name}.py --nofile --noconsole"
		os.system("cmd /c {command}")
   
   

    

















































		# print("\n\nhelp2", self.action_objects.objs)
		# print("\n\nhelp1", anotherMainObject.action_objects.objs)
		# self.action_objects.extend(anotherMainObject.action_objects.objs)
		# print("\n\nhelp2", self.action_objects.objs)
		# self.image_objects.extend(anotherMainObject.image_objects.objs)
		# self.text_objects.extend(anotherMainObject.text_objects.objs)
		# self.region_objects.extend(anotherMainObject.region_objects.objs)
		# self.point_objects.extend(anotherMainObject.point_objects.objs)





































		# self.action_objects.extend(anotherMainObject.action_objects)
		# self.image_objects.extend(anotherMainObject.image_objects)
		# self.text_objects.extend(anotherMainObject.text_objects)
		# self.region_objects.extend(anotherMainObject.region_objects)
		# self.point_objects.extend(anotherMainObject.point_objects)