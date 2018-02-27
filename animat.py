import numpy as np
from network import *

class Animat:
	def __init__(self, name = None, sensors = [], motors = [], perception_nodes = [], action_nodes = [], memory_capacity = 0, temporal_memory_capacity = 0):
		self.name = name
		self.network = Network(sensors, motors, perception_nodes, action_nodes, memory_capacity, temporal_memory_capacity)
	#End __init__()

#End Class Animat

