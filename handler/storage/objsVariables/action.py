from abc import ABC, abstractmethod
import time

from handler.storage.base import BaseObjs
# import handler.storage.mainObject as mainObject

# from numba import jit
# from numba import vectorize
# import numpy as np

def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

class Actions(ABC):
    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def directRecord(self) -> "Actions":
        pass

    @abstractmethod
    def record(self) -> "Actions":
        pass

    def saveTo(self, mainObject) -> None:
        mainObject.appendAction(self)


class ActionObjs(BaseObjs):
	def __init__(self):
		self.objs= []

	def append(self, obj):
		self.objs.append(obj)

	def extend(self, obj):
		self.objs.extend(obj)

	def clear(self):
		self.objs = []
		
	def pop(self):
		return self.objs.pop()
	@timeit
	# @jit
	def run(self):
		# print(len(self.objs))
		# a=tuple(self.objs)
		# print(len(a))
		for action in self.objs:
			action.run()
		
	# 	# [action.run() for action in self.objs]

	# 	# a = (action.run for action in self.objs)
	# 	# for _ in a:
	# 	# 	pass
		

	# 	# i=1
	# 	# while 1:
	# 	# 	try:
	# 	# 		self.objs[i].run()
	# 	# 		i += 1
	# 	# 	except:
	# 	# 		break
	# 	# print("run sucussful")
	# 	# for i in self.objs:
	# 	# 	if isinstance(i, Wait):
	# 	# 		t+=i.time
	# 	# print(sum([i.time for i in self.objs if isinstance(i, actions.ActionObjects.Wait)]))
	
	# @vectorize
	# def actualrun(self, i):
	# 	print(i)
	# @timeit
	# def run(self):

	# 	self.actualrun(np.arange(len(self.objs)))