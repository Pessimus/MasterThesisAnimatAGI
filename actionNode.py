

# Counts the number of 'true' values, 'false' values, and total number of values in a array of booleans.
#def truth(v):
#	on = 0
#	off = 0
#	total = 0
#	for x in v:
#		if x: on = on + 1
#		else: off = off + 1
#		total = total + 1
#	return (on, off, total)
#End truth()

# Method for creating a string to use as the name of a node. Called from subclasses in "nodes" and "temporalNodes".
def makeName(kind, nodes, sort=True):
	if sort:
		return "%s(%s)" % (kind, ", ".join(sorted([x.getName() for x in nodes])))
	else:
		return "%s(%s)" % (kind, ", ".join([x.getName() for x in nodes]))
#End makeName()

# A class reprecenting a action node. Including functionallity common for all action node-types.
class ActionNode:
	def __init__(self, name=None, outputs=None, temporal = False, permanent = False):
		self.name = name
		self.temporal = temporal
		self.active = False
#		self.previousActive = False
#		self.previousTemporalActive = False
		self.outputs = outputs or []
		self.time = 0
		self.activations = 0
		self.createdAt = 0
		self.permanent = permanent
	#End __init__

	# Method for updating the node each time-step.
	# Takes as input:
	#	- the current time 
	#	- the in-time-step update step number (temporalTime)
	#	- if the update is temporal inside the time-step or not
	# Returns if the node updates or not.
#	def tick(self, time, temporalTime = 0, temporal = False):
#		if (self.time > time or (self.time==time and (not self.temporal or (self.temporalTime >= temporalTime)))):
#			#print("Returning False\n")#TODO: remove after debug.
#			return False
#		self.time = time
#		self.temporalTime = temporalTime
#
#		for node in self.inputs:
#			node.tick(time,temporalTime,True)
#
#		self.previousTemporalActive = self.active
#
#		#print("Returning True\n")#TODO: remove after debug.
#		return True
	#End tick()

	# Sets the node to active and increases the count of how many tinmes the node has been activeated. 
	# Also activates all its output nodes.
	def activate(self, time, temporal = False):
		if (self.time >=time):
			return False
		self.time = time
		self.active = True
		self.activations = self.activations + 1
		for o in self.outputs:
			o.activate(time, temporal)
		return True
	#End activate

	# Sets the node as Inactive.
	def deactivate(self, time):
		self.active = False
	#End deactivate()

	# Returns if the node is active.
	def isActive(self):
		return self.active
	#End isActive()

	# Returns if the node was active the last time step.
#	def wasActive(self):
#		return self.previousActive
 	#End wasActive()

	# Returns if the node was active the last temporal step within the current time-step.
#	def wasTemporalActive(self):
#		return self.previousTemporalActive
	#End wasActive()

	# Returns the name of this node.
	def getName(self):
		return self.name
	#End getName()

	# Method for debugging, returns the 'word' reprecented by this node.
	def getWord(self):
		if len(self.outputs) > 1:
			return self.outputs[0].getWord() + self.outputs[1].getWord()
		if len(self.outputs) == 1:
			return self.outputs[0].getWord()
		return ""
	#End getWord

#End Class
