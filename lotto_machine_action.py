import lotto_machine as lm

class lotto_machine_action:
	machine = None
	
	def __init__(self):
		pass
	
	# list type
	def __init__(self, args):
		self.machine = None
		myBasket = lm.basket()

		for i in args:
			myBasket.setValue(lm.ball(i))
		
		self.machine = lm.lotto_machine(myBasket)	

	def __del__(self):
		pass	
	
	def pop_ball(self):
		return self.machine.pop()
	
	def pop_balls(self,cnt):
		ret = []

		for i in range(cnt):
			ret.append(self.machine.pop())
			#ret.append(lm.lotto_machine.pop())

		return ret
