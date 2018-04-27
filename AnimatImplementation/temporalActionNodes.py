from actionNode import *

# Represents a action SEQ node
# Extends 'ActionNode', and overrides the 'activate' function.
class TemporalASEQNode(ActionNode):
	def __init__(self, name=None, outputs=[]):
		if not name: name = makeName("SEQ", outputs, sort=False)
		ActionNode.__init__(self, name, outputs, True)
	#End __init__

	# Override of super method, makes call to parent if it should activate.
	def activate(self, time, temporal = False):
		if not temporal:
			return False
		return ActionNode.activate(self,time, temporal)
	#End activate

#End SEQNode

