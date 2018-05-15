from AnimatImplementation.node import *

# Represents a logical SEQ node
# Extends 'Node', and overrides the 'tick' function.
class TemporalSEQNode(Node):
	def __init__(self, name=None, inputs=[]):
		if not name: name = makeName("SEQ", inputs, sort=False)
		Node.__init__(self, name, inputs, True)
		self.possible_activations = []
	#End __init__

	# Overrides the 'tick' function. 
	# Else, (temporal) ticks all input nodes, and then activates if the first input was temporal active in the past, and the second is active as soon after as possible.
	# Updates the variable 'previous_temporal_active'
	def tick(self, time, temporal_time = 0, temporal = False):
		#if not temporal:
		#	return False
		if Node.tick(self, time, temporal_time, temporal):
			if len(self.inputs) > 1:
				self.previous_temporal_active = self.active 	#temporal nodes should update this value in tick (TODO: sould this be moved outside the if? Should not matter?)

				if(self.inputs[0].was_temporal_active() and self.inputs[1].starting_active()): #Migth become active.
					waitTime = self.inputs[1].activation_time()
					self.possible_activations.append(waitTime) #add a possible activation to check when relevant.
				#end if
				#print("debug in tick in TemporalSEQNode---")
				#print(self.possible_activations)
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


#-------------------OLD-------------------
# Represents a logical SEQ node
# Extends 'Node', and overrides the 'tick' function.
#class TemporalSEQNode(Node):
#	def __init__(self, name=None, inputs=[]):
#		if not name: name = makeName("SEQ", inputs, sort=False)
#		Node.__init__(self, name, inputs, True)
#	#End __init__
#
#	# Overrides the 'tick' function. Does not update if the tick is not temporal. 
#	# Else, (temporal) ticks all input nodes, and then activates if the first input was temporal active and the second is active.
#	# Updates the variable 'previous_temporal_active'
#	def tick(self, time, temporal_time = 0, temporal = False):
#		if not temporal:
#			return False
#		if Node.tick(self, time, temporal_time, temporal):
#			if len(self.inputs) > 1:
#				self.previous_temporal_active = self.active 	#temporal nodes should update this value in tick (TODO: sould this be moved outside the if? Should not matter?)
#				if self.inputs[0].was_temporal_active() and self.inputs[1].is_active():
#					self.activate(time)
#				else:
#					self.deactivate(time)
#			return True
#		else:
#			return False
#	#End tick()
#
#End SEQNode









	