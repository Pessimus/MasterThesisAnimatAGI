import numpy as np
import random
from network import *

class Animat:
	def __init__(self, name = None, sensors = [], motors = [], perception_nodes = [], action_nodes = [], memory_capacity = 0, temporal_memory_capacity = 0):
		self.name = name
		self.network = Network(sensors, motors, perception_nodes, action_nodes, memory_capacity, temporal_memory_capacity)
		self.last_action = -1

	#End __init__()

	#
	def update(self, time):
		print("Not yet implemented")
		#handle temporal input somehow
		#possibly learn from temporal input
		
		#tick network
		self.network.tick(time)
		self.learn()
		#end learning (learn from consequences of previous action in previous time step)
		#make decision
		#self.make_decision()
		#act
		self.babble()
		#begin learning
		#done!
	#End update()

	def begin_learning(self):
		print("Not yet implemented")
	#End begin_learning()

	def end_learning(self):
		print("Not yet implemented")
	#End end_learning()

	def make_decision(self):
		print("Not yet implemented")
	#End make_decision()

	def babble(self):
		num_motors = self.network.number_of_motors
		random_motor_index = random.randint(0,num_motors-1)
		if self.network.activate_action_node(random_motor_index):
			self.last_action = random_motor_index
		else:
			self.last_action = -1
	#End babble()

	def learn(self):
		if not last_action == -1:
			self.network.update_temporal_transition_matrix(last_action)
			self.network.update_generators()


	#End learn()




	#End babble()


#End Class Animat

