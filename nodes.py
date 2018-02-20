from node import *

# Represents a logical AND node
# Extends 'Node', and overrides the 'tick' function.
class AndNode(Node):
	def __init__(self, name=None, inputs=[]):
		inputs = sorted(inputs, key=lambda x: x.name)
		if not name: name = makeName("AND", inputs)
		Node.__init__(self, name, inputs)

	# Override of super method, makes call to parent and then updates if not yet updated this tick.
	# Is set to active if all the input nodes are active (and the number of input nodes is larger than 0). 
	def tick(self, time, temporalTime = 0, temporal = False):
		if temporal:
			return False
		if Node.tick(self, time):
			v = [node.active for node in self.inputs]
			on, off, total = truth(v)
			if total > 0 and total == on:
				self.activate(time)
			else:
				self.deactivate(time)
			return True
		else:
			return False
# -END of class AndNode


# Represents a logical NAND node
# Extends 'Node', and overrides the 'tick' function.
class NAndNode(Node):
	def __init__(self, name=None, inputs=[]):
		inputs = sorted(inputs, key=lambda x: x.name)
		if not name: name = makeName("NAND", inputs)
		Node.__init__(self, name, inputs)

	# Override of super method, makes call to parent and then updates if not yet updated this tick.
	# Is set to inactive if all the input nodes are active (and the number of input nodes is larger than 0). 
	def tick(self, time, temporalTime = 0, temporal = False):
		if temporal:
			return False
		if Node.tick(self, time):
			v = [node.active for node in self.inputs]
			on, off, total = truth(v)
			if total > 0 and total == on:
				self.deactivate(time)
			else:
				self.activate(time)
			return True
		else:
			return False
# -END of class NAndNode


# Represents a logical SEQ node
# Extends 'Node', and overrides the 'tick' function.
class SEQNode(Node):
	def __init__(self, name=None, inputs=[]):
		if not name: name = makeName("SEQ", inputs, sort=False)
		Node.__init__(self, name, inputs)

	def tick(self, time, temporalTime = 0, temporal = False):
		if temporal:
			return False
		if Node.tick(self, time):
			if len(self.inputs) > 1:
				if self.inputs[0].wasActive() and self.inputs[1].isActive():
					self.activate(time)
				else:
					self.deactivate(time)
			return True
		else:
			return False
#End SEQNode

#Node representing one of the Animats sensors 
class SensorNode(Node):
	def __init__(self, name, sensor, environment):
		Node.__init__(self, name, temporal=True, permanent=True)
		self.sensor = sensor
		self.environment = environment
	#End __init__()


	def tick(self, time, temporalTime=0, temporal=False):
		if Node.tick(self,time,temporalTime, temporal):
			if self.readSensor(temporalTime,temporal):
				self.activate(time)
			else:
				self.deactivate(time)
			return True
		else:
			return False
	#End tick()

	def readSensor(self, temporalTime=0, temporal=False):
		if self.sensor == "true":
			return 1
		if temporal:
			self.previousTemporalActive = self.active
			currentInput = self.environment.getEnvironmentalTemporalState()
			if(len(currentInput) > 0 and len(currentInput) >= temporalTime):
				return currentInput[temporalTime-1] == self.sensor
			else:
				return False
		else:
			currentInput = self.environment.getEnvironmentalState()
			for element in currentInput:
				if element == self.sensor:
					return True
			return False
	#End readSensor()

	# Method for debugging, returns the 'word' reprecented by this node.
	def getWord(self):
		return self.sensor
	#End getWord

#End SensorNode

