from AnimatImplementation.actionNode import *

# Represents a action AND node
# Extends 'ActionNode', and overrides the 'tick' function.
class ActionAndNode(ActionNode):
	def __init__(self, name=None, outputs=[]):
		outputs = sorted(outputs, key=lambda x: x.name)
		if not name: name = makeName("AAND", outputs)
		ActionNode.__init__(self, name, outputs)

	# Override of super method, makes call to parent if it should activate.
	def activate(self, time, temporal = False):
		if temporal:
			return False
		return ActionNode.activate(self,time)
	#End activate
#End ActionAndNode

#Node representing one of the Animats sensors 
class MotorNode(ActionNode):
	def __init__(self, name, motor, environment):
		ActionNode.__init__(self, name, temporal=True, permanent=True)
		self.motor = motor
		self.environment = environment
	#End __init__()

	# Override of super method, makes call to parent if it should activate.
	def activate(self, time, temporal = False):
		self.active = True
		self.activations = self.activations + 1
		self.activate_motor(temporal)
		return True
	#End activate

	def activate_motor(self, temporal=False):
		if temporal:
			self.environment.add_environmental_temporal_input(self.motor)
		else:
			self.environment.add_environmental_input(self.motor)
	#End readSensor()

	# Method for debugging, returns the 'word' reprecented by this node.
	def get_word(self):
		return self.motor
	#End get_word

#End SensorNode











