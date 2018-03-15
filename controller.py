from textHandler import *
import datetime

class Controller():
	#TODO: remember animat can be none for now
	def __init__(self, environment, input_file_name, output_file_name, animat=None):
		self.animat = animat
		self.environment = environment
		self.file_reader = FileReader(input_file_name + ".txt")
		self.file_writer = FileWriter("output/" + output_file_name + datetime.datetime.now().strftime("%y%m%d-%H%M%S") + ".txt")
	#End __init__()

	#Updates environment and animat until there is no more input.
	#TODO: check if the animat gets to give its last response
	def run(self):
		while not self.file_reader.end_of_file:
			self.update_environment()
			#self.update_animat()

		self.file_reader.closeFile()
		self.file_writer.closeFile()
	#End updater()

	#TODO: should this be tick? like an environment tick()?
	def update_environment(self):
		#print("Debug: Updating environment")
		#add the next word of the file to the environment's next temporal state
		self.environment.add_environmental_temporal_input(self.file_reader.getNextWord())

		#TODO: add the next non-word input which should also come from somewhere...
		#environment.addEnvironmentalInput()

		#save the environment's current temporal state (word)
		current_temporal_state = self.environment.get_environmental_temporal_state() #list of all letters active in a time step
		self.file_writer.writeLineToFile(convertListToWord(current_temporal_state))

		#TODO: save the environments non-word state somewhere...
		#currentState = environment.get_environmental_state()

		self.environment.update()
	#End update_environment

	#def update_animat(self):
		#TODO: tick the animat
		#print("Debug: Placeholder - time to tick animat")
	#End update_animat
# #End class controller
