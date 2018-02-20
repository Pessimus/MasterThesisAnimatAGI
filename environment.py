class Environment:
	def __init__(self, temporalInput = [], input = set(), temporalOutput = [], output = set()):
		self.temporalInput = temporalInput
		self.input = input
		self.temporalOutput = temporalOutput
		self.output = output
	#End __init__()