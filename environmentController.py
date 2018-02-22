from textHandler import *
import datetime

class environmentUpdater():

	def __init__(self, environment, input_file_name, output_file_name):
		self.environment = environment
		self.file_reader = fileReader(input_file_name)
		self.file_writer = fileWriter(output_file_name + datetime.datetime.now().strftime("%y%m%d-%H%M%S"))
	#End __init__()

	def updater():
		while not file_reader.end_of_file:
			self.update_environment()

		self.file_reader.close()
		self.file_writer.close()
	#End updater()

	#TODO: should this be tick? like an environment tick()?
	def update_environment():
		#add the next word of the file to the environment's next temporal state
		self.environment.addEnvironmentalTemporalInput(file_reader.getNextWord())

		#TODO: add the next non-word input which should also come from somewhere...
		#environment.addEnvironmentalInput()

		#save the environments current temporal state (word)
		currentTemporalState = environment.getEnvironmentalTemporalState() #list of all letters active in a time step
		self.file_writer.write(convertListToWord(currentTemporalState))

		#TODO: save the environments non-word state somewhere...
		#currentState = environment.getEnvironmentalState()

		self.environment.update()
	#End update_environment
# #End class environmentUpdater


# def environment_updater(environment, input_file_name, output_file_name):
# 	#file objects for reading from input file and writing to output_file
# 	file_reader = fileReader(input_file_name)
# 	file_writer = fileWriter(output_file_name)

# 	#as long as there is input left in the file, update
# 	while not file_reader.end_of_file:
# 		update_environment(environment, file_reader, file_writer)

# 	file_reader.close()
# 	file_writer.close()
# #End environment_updater()

# def update_environment():
# 	#add the next word of the file to the environment's next temporal state
# 	environment.addEnvironmentalTemporalInput(file_reader.getNextWord())

# 	#TODO: add the next non-word input which should also come from somewhere...
# 	#environment.addEnvironmentalInput()

# 	#save the environments current temporal state (word)
# 	currentTemporalState = environment.getEnvironmentalTemporalState() #list of all letters active in a time step
# 	file_writer.write(convertListToWord(currentTemporalState))

# 	#TODO: save the environments non-word state somewhere...
# 	#currentState = environment.getEnvironmentalState()

# 	environment.update()
# #End update_environment