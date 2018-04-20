from AnimatImplementation.node import *

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
	def tick(self, time, temporal_time = 0, temporal = False):
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
	def activation_time(self):
		return max(self.inputs[0].activation_time(), self.inputs[1].activation_time())
	#End activation_time()

	#Returns true if this node has just gotten the first input it needs to become active.
	#TODO: this method does not check that the node has input....
	def starting_active(self):
		at1 = self.inputs[0].activation_time()
		at2 = self.inputs[1].activation_time()
		if(at1 > at2):
			return self.inputs[0].starting_active()
		else:
			return self.inputs[1].starting_active()
	#End starting_active()
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
	def tick(self, time, temporal_time = 0, temporal = False):
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
	def activation_time(self):
		return 1 #As all nodes can become inactive in one time step.
	#End activation_time()

	#Returns true if this node has just gotten the first input it needs to become active.
	#TODO: this method does not check that the node has input....
	def starting_active(self):
		return not self.is_active();
	#End starting_active()
# -END of class NAndNode


# Represents a logical SEQ node
# Extends 'Node', and overrides the 'tick' function.
class SEQNode(Node):
	def __init__(self, name=None, inputs=[]):
		if not name: name = makeName("SEQ", inputs, sort=False)
		Node.__init__(self, name, inputs)
		self.possible_activations = []
	#End __init__()

#	def tick(self, time, temporal_time = 0, temporal = False):
#		if temporal:
#			return False
#		if Node.tick(self, time):
#			if len(self.inputs) > 1:
#				if self.inputs[0].was_active() and self.inputs[1].is_active():
#					self.activate(time)
#				else:
#					self.deactivate(time)
#			return True
#		else:
#			return False
#	#End tick()
	# Overrides the 'tick' function. Does not update if the tick is temporal. 
	# Else, ticks all input nodes, and then activates if the first input was temporal active in the past, and the second is active as soon after as possible.
	def tick(self, time, temporal_time = 0, temporal = False):
		if temporal:
			return False
		if Node.tick(self, time):
			if len(self.inputs) > 1:
				if(self.inputs[0].was_active() and self.inputs[1].starting_active()): #Migth become active.
					waitTime = self.inputs[1].activation_time()
					self.possible_activations.append(waitTime) #add a possible activation to check when relevant.
				#end if
				self.deactivate(time)#TODO: should this be done here?
				tmppossible_activations = []
				for waitTime in self.possible_activations:
					waitTime = waitTime-1;
					if (waitTime) == 0:
						if self.inputs[1].is_active() and not self.is_active():#no need to activate if already active.
							self.activate(time)
					else:
						tmppossible_activations.append(waitTime)
				#end loop
				self.possible_activations = tmppossible_activations
			#end if
			return True
		else:
			return False
	#End tick()

	#Returning the number of ticks required for this node to become active.
	def activation_time(self):
		activation_time = 0;
		for input in self.inputs:
			activation_time = activation_time + input.activation_time()
		return activation_time
	#End activation_time()

	#Returns true if this node has just gotten the first input it needs to become active.
	def starting_active(self):
		if len(self.inputs) > 0:
			return self.inputs[0].starting_active()
		return False #Does not have input, is allways false.
	#End starting_active()
#End SEQNode

#Node representing one of the Animats sensors 
class SensorNode(Node):
	def __init__(self, name, sensor, environment):
		Node.__init__(self, name, temporal=True, permanent=True)
		self.sensor = sensor
		self.environment = environment
		self.last_tick_temporal = False
	#End __init__()

	# Overrides the 'tick' function. Ticks this node, looking att different parts of the environment depending on if the tick is temporal or not.
	def tick(self, time, temporal_time=0, temporal=False):
		if (not temporal) and self.last_tick_temporal:
			self.last_tick_temporal = False
			self.time = time - 1
		if Node.tick(self,time,temporal_time, temporal):
			self.last_tick_temporal = temporal
			if self.read_sensor(temporal_time,temporal):
				self.activate(time)
			else:
				self.deactivate(time)
			return True
		else:
			return False
	#End tick()

	#Returning the number of ticks required for this node to become active.
	def activation_time(self):
		return 1
	#End activation_time()

	#Returns true if this node has just gotten the first input it needs to become active.
	def starting_active(self):
		return self.is_active()
	#End starting_active()

	#Returns true iff the input that this sensor reacts to is present in the input in the environment. 
	def read_sensor(self, temporal_time=0, temporal=False):
		if self.sensor == "true":
			return 1
		if temporal:
			#self.previous_temporal_active = self.active
			currentInput = self.environment.get_environmental_temporal_state()
			if(len(currentInput) > 0 and len(currentInput) > temporal_time):
				return currentInput[temporal_time] == self.sensor
			else:
				return False
		else:
			currentInput = self.environment.get_environmental_state()
			for element in currentInput:
				if element == self.sensor:
					return True
			return False
	#End read_sensor()

	# Method for debugging, returns the 'word' reprecented by this node.
	def get_word(self):
		return self.sensor
	#End get_word

	#TODOD: THIS IS DEBUG.
	#Updates this node to check if it should be topactive. Might be called again from nodes that have it as input.
	#def update_topactive(self, can_still_be_topactive = True):
	#	self.topactive = self.active
	#End update_topactive()

#End SensorNode

