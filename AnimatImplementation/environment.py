import copy


# A class representing the environment that the Animat can perceive. 
# Contains a set of values and a list of temporal orderd values, that the Animat can perceive.
# Can also be given values to be in the next set and list, after the method update() has been called.
class Environment:
	def __init__(self, temporal_state = [], state = set()):
		self.state = state
		self.temporal_state = temporal_state
		self.next_state = set()
		self.next_temporal_state = []
	#End __init__()

	#Method allowing the environment to give its state as output.
	def get_environmental_state(self):
		return copy.copy(self.state)
	#End getEnvironmentalState()

	#Method allowing the environment to give the temporal part of its state as output.
	def get_environmental_temporal_state(self):
		return copy.copy(self.temporal_state)
	#End getEnvironmentaltemporal_state()

	#Method for adding input to the environment's state. Will be part of output in the next timestep.
	def add_environmental_input(self, input):
		self.next_state.add(input)
	#End addEnvironmentalInput()

	#Method for adding temporal input to the environment's temporal state. Will be part of temporal output in the next timestep.
	def add_environmental_temporal_input(self, input):
		#self.nexttemporal_state = self.nexttemporal_state + input
		self.next_temporal_state.append(input)
	#End addEnvironmentalTemporalInput()

	#Set the current state to next state and clears the variable for next state.
	#To be used between timesteps.
	def update(self):
		self.state = self.next_state
		self.next_state = set()

		if(len(self.next_temporal_state) > 0):
			self.state.add(self.next_temporal_state[-1])

		self.temporal_state = self.next_temporal_state
		self.next_temporal_state = []
	#End update()

	#Method allowing the environment to give its next state as output.
	def get_next_environmental_state(self):
		return copy.copy(self.next_state)
	#End getNextEnvironmentalState()

	#Method allowing the environment to give the temporal part of its next state as output.
	def get_next_environmental_temporal_state(self):
		return copy.copy(self.next_temporal_state)
	#End getNextEnvironmentaltemporal_state()

	#Clears the state (both temporal and non-temporal), and also the data for next state.
	def clear(self):
		self.state = set()
		self.temporal_state = []
		self.next_state = set()
		self.next_temporal_state = []
	#End clear()

#End Environment