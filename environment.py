import copy

class Environment:
	def __init__(self, temporalState = [], state = set()):
		self.state = state
		self.temporalState = temporalState
		self.nextState = set()
		self.nextTemporalState = []
	#End __init__()

	#Method allowing the environment to give its state as output.
	def getEnvironmentalState(self):
		return copy.copy(self.state)
	#End getEnvironmentalState()

	#Method allowing the environment to give the temporal part of its state as output.
	def getEnvironmentalTemporalState(self):
		return copy.copy(self.temporalState)
	#End getEnvironmentalTemporalState()

	#Method for adding input to the environment's state. Will be part of output in the next timestep.
	def addEnvironmentalInput(self, input):
		self.nextState.add(input)
	#End addEnvironmentalInput()

	#Method for adding temporal input to the environment's temporal state. Will be part of temporal output in the next timestep.
	def addEnvironmentalTemporalInput(self, input):
		#self.nextTemporalState = self.nextTemporalState + input
		self.nextTemporalState.append(input)
	#End addEnvironmentalTemporalInput()

	#Set the current state to next state and clears the variable for next state.
	#To be used between timesteps.
	def update(self):
		self.state = self.nextState
		self.nextState = set()

		self.temporalState = self.nextTemporalState
		self.nextTemporalState = []
	#End update()