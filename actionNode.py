
# Method for creating a string to use as the name of a node. Called from subclasses in "nodes" and "temporalNodes".
def makeName(kind, nodes, sort=True):
	if sort:
		return "%s(%s)" % (kind, ", ".join(sorted([x.get_name() for x in nodes])))
	else:
		return "%s(%s)" % (kind, ", ".join([x.get_name() for x in nodes]))
#End makeName()

# A class reprecenting a action node. Including functionallity common for all action node-types.
class ActionNode:
	def __init__(self, name=None, outputs=[], temporal = False, permanent = False, index=0):
		self.name = name
		self.temporal = temporal
		self.active = False
		#self.previous_active = False
		#self.previous_temporal_active = False
		self.outputs = outputs
		self.time = 0
		self.activations = 0
		self.created_at = 0
		self.permanent = permanent
		self.index = index
	#End __init__()

	# Sets the node to active and increases the count of how many tinmes the node has been activeated. 
	# Also activates all its output nodes.
	def activate(self, time, temporal = False):
		if (self.time > time or (self.time == time and not temporal)):
			return False
		self.time = time
		self.active = True
		self.activations = self.activations + 1
		for o in self.outputs:
			o.activate(time, temporal)
		return True
	#End activate()

	# Sets the node as Inactive.
	def deactivate(self, time):
		self.active = False
	#End deactivate()

	# Returns if the node is active.
	def is_active(self):
		return self.active
	#End is_active()

	# Returns the name of this node.
	def get_name(self):
		return self.name
	#End get_name()


	# Returns the index of this node.
	def get_index(self):
		return self.index
	#End get_index()


	# Method for debugging, returns the 'word' reprecented by this node.
	def get_word(self):
		if len(self.outputs) > 1:
			return self.outputs[0].get_word() + self.outputs[1].get_word()
		if len(self.outputs) == 1:
			return self.outputs[0].get_word()
		return ""
	#End getWord

#End Class
