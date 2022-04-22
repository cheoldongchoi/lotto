import random 

class ball:
	value=None

	def __init__(self, inStr_val):
		self.value = None
		self.value=inStr_val

	def __del__(self):
		pass

	def setValue(self, inStr_val):
		self.value = inStr_val

	def getValue(self):
		return self.value

class basket:
	myBasket=[]

	def __init__(self):
		self.myBasket=[]
		pass

	'''	
	def __init__(self, objects):
		self.myBasket = []
		self.myBasket= objects
	'''

	def __del__(self):
		pass	
	
	def setValue(self, object):
		self.myBasket.append(object)

	def getValue(self):
		return self.myBasket

class lotto_machine:
	myBasket = []
	
	def __init__(self, objects):
		self.myBasket = []
		for i in objects.getValue():
			self.myBasket.append(i)	

	def __del__(self):
		pass

	def getBalls(self):
		return self.myBasket

	def shaking(self):
		random.shuffle(self.myBasket)

	def pop(self):
		try:
			self.shaking()
			ret = (self.myBasket[0]).getValue()
			
			del self.myBasket[0]
			return ret
		except (IndexError) as e:
			print(e)
			return 'Error'


