from node import *

# Represents a logical AND node
# Extends 'Node', and overrides the 'tick' function.
class AndNode(Node):
	def __init__(self, name=None, inputs=[]):
		inputs = sorted(inputs, key=lambda x: x.name)
		if not name: name = makeName("AND", inputs)
		Node.__init__(self, name, inputs)
	#End __init__()

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
	#End tick()

	#Returning the number of ticks required for this node to become active.
	#TODO: this method does not check that the node has input....
	def activationTime(self):
		return max(self.inputs[0].activationTime(), self.inputs[1].activationTime())
	#End activationTime()

	#Returns true if this node has just gotten the first input it needs to become active.
	#TODO: this method does not check that the node has input....
	def startingActive(self):
		at1 = self.inputs[0].activationTime()
		at2 = self.inputs[1].activationTime()
		if(at1 > at2):
			return self.inputs[0].startingActive()
		else:
			return self.inputs[1].startingActive()
	#End startingActive()
# -END of class AndNode


# Represents a logical NAND node
# Extends 'Node', and overrides the 'tick' function.
class NAndNode(Node):
	def __init__(self, name=None, inputs=[]):
		inputs = sorted(inputs, key=lambda x: x.name)
		if not name: name = makeName("NAND", inputs)
		Node.__init__(self, name, inputs)
	#End __init__()

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
	#End tick()

	#Returning the number of ticks required for this node to become active.
	#TODO: this method does not check that the node has input....
	def activationTime(self):
		return 1 #As all nodes can become inactive in one time step.
	#End activationTime()

	#Returns true if this node has just gotten the first input it needs to become active.
	#TODO: this method does not check that the node has input....
	def startingActive(self):
		return not self.is_active();
	#End startingActive()
# -END of class NAndNode


# Represents a logical SEQ node
# Extends 'Node', and overrides the 'tick' function.
class SEQNode(Node):
	def __init__(self, name=None, inputs=[]):
		if not name: name = makeName("SEQ", inputs, sort=False)
		Node.__init__(self, name, inputs)
		self.possibleActivations = []
	#End __init__()

#	def tick(self, time, temporalTime = 0, temporal = False):
#		if temporal:
#			return False
#		if Node.tick(self, time):
#			if len(self.inputs) > 1:
#				if self.inputs[0].wasActive() and self.inputs[1].is_active():
#					self.activate(time)
#				else:
#					self.deactivate(time)
#			return True
#		else:
#			return False
#	#End tick()
	# Overrides the 'tick' function. Does not update if the tick is temporal. 
	# Else, ticks all input nodes, and then activates if the first input was temporal active in the past, and the second is active as soon after as possible.
	def tick(self, time, temporalTime = 0, temporal = False):
		if temporal:
			return False
		if Node.tick(self, time):
			if len(self.inputs) > 1:
				if(self.inputs[0].wasActive() and self.inputs[1].startingActive()): #Migth become active.
					waitTime = self.inputs[1].activationTime()
					self.possibleActivations.append(waitTime) #add a possible activation to check when relevant.
				#end if
				self.deactivate(time)#TODO: should this be done here?
				tmpPossibleActivations = []
				for waitTime in self.possibleActivations:
					waitTime = waitTime-1;
					if (waitTime) == 0:
						if self.inputs[1].is_active() and not self.is_active():#no need to activate if already active.
							self.activate(time)
					else:
						tmpPossibleActivations.append(waitTime)
				#end loop
				self.possibleActivations = tmpPossibleActivations
			#end if
			return True
		else:
			return False
	#End tick()

	#Returning the number of ticks required for this node to become active.
	def activationTime(self):
		activationTime = 0;
		for input in self.inputs:
			activationTime = activationTime + input.activationTime()
		return activationTime
	#End activationTime()

	#Returns true if this node has just gotten the first input it needs to become active.
	def startingActive(self):
		if len(self.inputs) > 0:
			return self.inputs[0].startingActive()
		return False #Does not have input, is allways false.
	#End startingActive()
#End SEQNode

#Node representing one of the Animats sensors 
class SensorNode(Node):
	def __init__(self, name, sensor, environment):
		Node.__init__(self, name, temporal=True, permanent=True)
		self.sensor = sensor
		self.environment = environment
	#End __init__()

	# Overrides the 'tick' function. Ticks this node, looking att different parts of the environment depending on if the tick is temporal or not.
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

	#Returning the number of ticks required for this node to become active.
	def activationTime(self):
		return 1
	#End activationTime()

	#Returns true if this node has just gotten the first input it needs to become active.
	def startingActive(self):
		return self.is_active()
	#End startingActive()

	#Returns true iff the input that this sensor reacts to is present in the input in the environment. 
	def readSensor(self, temporalTime=0, temporal=False):
		if self.sensor == "true":
			return 1
		if temporal:
			#self.previous_temporal_active = self.active
			currentInput = self.environment.get_environmental_temporal_state()
			if(len(currentInput) > 0 and len(currentInput) > temporalTime):
				return currentInput[temporalTime] == self.sensor
			else:
				return False
		else:
			currentInput = self.environment.get_environmental_state()
			for element in currentInput:
				if element == self.sensor:
					return True
			return False
	#End readSensor()

	# Method for debugging, returns the 'word' reprecented by this node.
	def get_word(self):
		return self.sensor
	#End get_word

#End SensorNode

