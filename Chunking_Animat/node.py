

# Counts the number of 'true' values, 'false' values, and total number of values in a array of booleans.
def truth(v):
	on = 0
	off = 0
	total = 0
	for x in v:
		if x: on = on + 1
		else: off = off + 1
		total = total + 1
	return (on, off, total)
#End truth()

# Method for creating a string to use as the name of a node. Called from subclasses in "nodes" and "temporalNodes".
def makeName(kind, nodes, sort=True):
	if sort:
		return "%s(%s)" % (kind, ", ".join(sorted([x.get_name() for x in nodes])))
	else:
		return "%s(%s)" % (kind, ", ".join([x.get_name() for x in nodes]))
#End makeName()

# A class reprecenting a node. Including functionallity common for all node-types.
class Node:
	def __init__(self, name=None, inputs=[], temporal = False, permanent = False, index = 0):
		self.name = name
		self.temporal = temporal
		self.active = False
		self.topactive = False
		self.previous_active = False
		self.previous_temporal_active = False
#		self.previous_top_active = False
#		self.previous_temporal_top_active = False
		self.inputs = inputs
		self.time = 0
		self.temporal_time = 0 #TODO: should this be here? Needed as the code is now....
		self.activations = 0
		self.created_at = 0
		self.permanent = permanent
		self.index = index
		#self.generator = None #TODO?
	#End __init__

	# Method for updating the node each time-step.
	# Takes as input:
	#	- the current time 
	#	- the in-time-step update step number (temporal_time)
	#	- if the update is temporal inside the time-step or not
	# Returns if the node updates or not.
	def tick(self, time, temporal_time = 0, temporal = False):
		if (self.time > time or (self.time==time and (not self.temporal or (self.temporal_time >= temporal_time)))):
			return False

		#if self.time < time:
		#	self.previous_active = self.active

		self.time = time
		self.temporal_time = temporal_time

		for node in self.inputs:
			node.tick(time,temporal_time,temporal)
		
		if temporal:
			self.previous_temporal_active = self.active

		return True
	#End tick()

	#SHOULD BE OVERWRITTEN BY SUBCLASSES
	#Returning the number of ticks required for this node to become active.
	def activation_time(self):
		return 1
	#End activation_time()

	def get_all_input(self):
		res = {self}
		for input in self.inputs:
			res = res | input.get_all_input()
		return res

	def get_all_sensor_input(self):
		res = []
		for input in self.inputs:
			res = res + input.get_all_sensor_input()
		return res

	#SHOULD BE OVERWRITTEN BY SUBCLASSES
	#Returns true if this node has just gotten the first input it needs to become active.
	def starting_active(self):
		return self.is_active()
	#End starting_active()

	# Sets the node as Active, and increases the count of how many tinmes the node has been active.
	def activate(self, time):
		self.active = True
		self.activations = self.activations + 1
	#End activate

	# Sets the node as Inactive.
	def deactivate(self, time):
		self.active = False
	#End deactivate()

	# Returns if the node is active.
	def is_active(self):
		return self.active
	#End is_active()

	# Returns if the node was active the last time step.
	def was_active(self):
		return self.previous_active
 	#End was_active()

	# Returns if the node was active the last temporal step within the current time-step.
	def was_temporal_active(self):
		return self.previous_temporal_active
	#End was_temporal_active()

	# Returns the name of this node.
	def get_name(self):
		return self.name
	#End get_name()

	# Returns the index of this node.
	def get_index(self):
		return self.index
	#End get_index()

	#Updates this node to check if it should be topactive. Might be called again from nodes that have it as input.
	def update_topactive(self, can_still_be_topactive = True):
		if not can_still_be_topactive:
			self.topactive = False
			for i in self.inputs:
				i.update_topactive(False)
		elif not self.active:# or not self.topactive:
			self.topactive = False
		elif self.topactive:
			for i in self.inputs:
				i.update_topactive(False)
	#End update_topactive()

	# Method for debugging, returns the 'word' reprecented by this node.
	def get_word(self):
		if len(self.inputs) > 1:
			return self.inputs[0].get_word() + self.inputs[1].get_word()
		if len(self.inputs) == 1:
			return self.inputs[0].get_word()
		return ""
	#End get_word

#End Class














