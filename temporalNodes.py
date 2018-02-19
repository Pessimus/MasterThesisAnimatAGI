from node import *

# Represents a logical SEQ node
# Extends 'Node', and overrides the 'tick' function.
class TemporalSEQNode(Node):
	def __init__(self, name=None, inputs=[]):
		if not name: name = makeName("SEQ", inputs, sort=False)
		Node.__init__(self, name, inputs, True)
	#End __init__

	# Overrides the 'tick' function. Does not update if the tick is not temporal. 
	# Else, (temporal) ticks all input nodes, and then activates if the first input was temporal active and the second is active.
	# Updates the variable 'previousTemporalActive'
	def tick(self, time, temporalTime = 0, temporal = False):
		if not temporal:
			return False
		if Node.tick(self, time, temporalTime, temporal):
			if len(self.inputs) > 1:
				self.previousTemporalActive = self.active 	#temporal nodes should update this value in tick (TODO: sould this be moved outside the if? Should not matter?)
				if self.inputs[0].wasTemporalActive() and self.inputs[1].isActive():
					self.activate(time)
				else:
					self.deactivate(time)
			return True
		else:
			return False
	#End tick()

#End SEQNode









	