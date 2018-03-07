import numpy as np
import random
from network import *

class Animat:
	def __init__(self, name = None, sensors = [], motors = [], perception_nodes = [], action_nodes = [], memory_capacity = 0, temporal_memory_capacity = 0):
		self.name = name
		self.network = Network(sensors, motors, perception_nodes, action_nodes, memory_capacity, temporal_memory_capacity)
		self.last_action = -1

	#End __init__()

	def update(self, time, temporal_input_length = 0):

		self.network.update_previous_active()

		for tt in range(0,temporal_input_length):
			self.temporal_update(time, tt)

		self.network.tick(time)
		self.learn()

		self.act(time)
	#End update()

	def temporal_update(self, time, temporal_time):
		print("Doing temporal stuff!")
		self.network.temporal_tick(time, temporal_time)

		#Learn
		self.temporal_learn()

	#End temporal_update()

	#
	def update_step_one_version(self, time):
		#handle temporal input somehow
		#possibly learn from temporal input
		
		#tick network
		self.network.update_previous_active()
		self.network.tick(time)
		self.learn()

		#end learning (learn from consequences of previous action in previous time step)
		#make decision
		#self.make_decision()
		#act
		self.babble(time)
		#begin learning
	#End update()

	def act(self, time):
		self.babble(time)
	#End act()

	def begin_learning(self):
		print("Not yet implemented")
	#End begin_learning()

	def end_learning(self):
		print("Not yet implemented")
	#End end_learning()

	def make_decision(self):
		print("Not yet implemented")
	#End make_decision()

	def babble(self, time):
		num_motors = self.network.number_of_motors
		random_motor_index = random.randint(0,num_motors-1)
		if self.network.activate_action_node(random_motor_index, time):
			self.last_action = random_motor_index
		else:
			self.last_action = -1
	#End babble()

	def learn(self):
		if not self.last_action == -1:
			self.network.update_transition_matrix(self.last_action)
			self.network.update_generators()
	#End learn()

	def temporal_learn(self):
		self.network.update_temporal_sequence_matrix()



	#End babble()


#End Class Animat

