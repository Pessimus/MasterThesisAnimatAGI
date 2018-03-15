from node import *
from nodes import *
from temporalNodes import *
from environment import *
from actionNodes import *
from temporalActionNodes import *
from textHandler import *
from controller import *
from network import *
from animat import *
import random



def test_if_nodes_update_when_they_should(verbose = True):

	print ("------------------test_if_nodes_update_when_they_should------------------")

	#print("----------------Testing if nodes update----------------")
	pasing_tests = True
	seqNodeTestNode = SEQNode()
	v = seqNodeTestNode.tick(1)
	if verbose:
		print("\t should be True,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (v)
	v = seqNodeTestNode.tick(1)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (not v)
	v = seqNodeTestNode.tick(2,1)
	if verbose:
		print("\t should be True,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (v)
	v = seqNodeTestNode.tick(2,2)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (not v)
	v = seqNodeTestNode.tick(3,1,True)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (not v)

	temporalSeqNodeTestNode = TemporalSEQNode()
	v = temporalSeqNodeTestNode.tick(1)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (not v)
	v = temporalSeqNodeTestNode.tick(1)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (not v)
	v = temporalSeqNodeTestNode.tick(2,1,True)
	if verbose:
		print("\t should be True,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (v)
	v = temporalSeqNodeTestNode.tick(2,2,True)
	if verbose:
		print("\t should be True,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (v)
	v = temporalSeqNodeTestNode.tick(2,2,True)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (v))
	else:
		pasing_tests = pasing_tests and (not v)

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_nodes_update_to_the_value_they_should(verbose = True):

	print ("------------------test_if_nodes_update_to_the_value_they_should------------------")

	#print("----------------Testing values of updated nodes----------------")
	dummy1 = Node()
	dummy2 = Node()

	if verbose:
		print("--------Testing SEQ Node--------")
	pasing_tests = True

	seqNodeTestNode = SEQNode()
	inputList = [dummy1,dummy2] 
	seqNodeTestNode.inputs = inputList
	i = 1
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not seqNodeTestNode.is_active())
	dummy1.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not seqNodeTestNode.is_active())
	dummy1.active = False
	dummy2.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not seqNodeTestNode.is_active())
	dummy1.active = True
	dummy2.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not seqNodeTestNode.is_active())
	dummy1.previous_active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be True,\n\t -------is %s" % (seqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (seqNodeTestNode.is_active())

	if verbose:
		print("--------Testing Temporal SEQ Node--------")

	dummy1 = Node()
	dummy2 = Node()
	temporalSeqNodeTestNode = TemporalSEQNode()
	inputList = [dummy1,dummy2] 
	temporalSeqNodeTestNode.inputs = inputList
	i = 1

	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.is_active())
	dummy1.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.is_active())
	dummy1.active = False
	dummy2.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.is_active())
	dummy1.active = True
	dummy2.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.is_active())
	dummy1.previous_active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.is_active())
	dummy1.previous_temporal_active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be True,\n\t -------is %s" % (temporalSeqNodeTestNode.is_active()))
	else:
		pasing_tests = pasing_tests and (temporalSeqNodeTestNode.is_active())

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_sensors_react_to_input(verbose = True):

	print ("------------------test_if_sensors_react_to_input------------------")
	pasing_tests = True

	#print("----------------Testing sensors----------------")
	testEnvironment = Environment()
	testSensor = SensorNode(name = "d-sensor",sensor = "d", environment =  testEnvironment)
	i = 1
	testSensor.tick(i)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.is_active()))
	else:
		pasing_tests = pasing_tests and (not testSensor.is_active())

	testSensor.tick(i, 0, True)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.is_active()))
	else:
		pasing_tests = pasing_tests and (not testSensor.is_active())

	testEnvironment.state = {"d", "o", "g"}
	i=i+1
	testSensor.tick(i)
	if verbose:
		print("\t should be True,\n\t -------is %s" % (testSensor.is_active()))
	else:
		pasing_tests = pasing_tests and (testSensor.is_active())

	testEnvironment.state = {"g", "o", "g"}
	i=i+1
	testSensor.tick(i)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.is_active()))
	else:
		pasing_tests = pasing_tests and (not testSensor.is_active())

	testEnvironment.temporal_state = ["d", "o", "g"]
	i=i+1
	testSensor.tick(i, 0, True)
	if verbose:
		print("\t should be True,\n\t -------is %s" % (testSensor.is_active()))
	else:
		pasing_tests = pasing_tests and (testSensor.is_active())

	testSensor.tick(i, 1, True)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.is_active()))
	else:
		pasing_tests = pasing_tests and (not testSensor.is_active())

	testEnvironment.state = {"d", "o", "g"}
	testSensor.tick(i, 2, True)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.is_active()))
	else:
		pasing_tests = pasing_tests and (not testSensor.is_active())

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_dog_can_be_found(verbose = True):

	print ("------------------test_if_dog_can_be_found------------------")
	pasing_tests = True

	for r in range(2):
		testEnvironment = Environment()
	
		sensor_node_d = SensorNode(name = "d-sensor",sensor = "d", environment =  testEnvironment)
		sensor_node_o = SensorNode(name = "o-sensor",sensor = "o", environment =  testEnvironment)
		sensor_node_g = SensorNode(name = "g-sensor",sensor = "g", environment =  testEnvironment)

		sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  testEnvironment)
		sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  testEnvironment)
		sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  testEnvironment)

		t_seq_do = TemporalSEQNode(inputs = [sensor_node_d, sensor_node_o])
		t_seq_dog = TemporalSEQNode(inputs = [t_seq_do, sensor_node_g])
		t_seq_ca = TemporalSEQNode(inputs = [sensor_node_c, sensor_node_a])
		t_seq_cat = TemporalSEQNode(inputs = [t_seq_ca,sensor_node_t])
	
		all_nodes = {sensor_node_d,sensor_node_o,sensor_node_g,t_seq_do,t_seq_dog,sensor_node_c,sensor_node_a,sensor_node_t,t_seq_ca,t_seq_cat}

	#	if random.randint(0, 1) == 1:
		if r == 1:
			testEnvironment.temporal_state = ["d","o","g"]
		else:
			testEnvironment.temporal_state = ["c","a","t"]

		for n in all_nodes:
			n.tick(1,0,True)

		#print(sensor_node_d.is_active())
		#print("--1--")

		for n in all_nodes:
			n.tick(1,1,True)

		#print(sensor_node_o.is_active())
		#print(t_seq_do.is_active())
		#print("--2--")

		for n in all_nodes:
			n.tick(1,2,True)

		#print(sensor_node_g.is_active())
		#print(t_seq_ca.is_active())
		#print(t_seq_cat.is_active())
		#print("--3--")
		if verbose:
			if(t_seq_dog.is_active()):
				print("THE DOG IS ACTIVE!!!!!!!!!!!!! OMG OMG")

			if(t_seq_cat.is_active()):
				print("THE CAT IS ACTIVE!!!!!!!!!!!!! OMG OMG")

			print(t_seq_cat.name)
			print(t_seq_cat.get_word())
			print(t_seq_dog.get_word())
		else:
			if(r == 1):
				pasing_tests = pasing_tests and t_seq_dog.is_active()
			else:
				pasing_tests = pasing_tests and t_seq_cat.is_active()

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_motors_produce_things(verbose = True):

	print ("------------------test_if_motors_produce_things------------------")
	pasing_tests = True

	testEnvironment = Environment()

	motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  testEnvironment)
	motor_node_o = MotorNode(name = "o-motor",motor = "o", environment =  testEnvironment)
	motor_node_g = MotorNode(name = "g-motor",motor = "g", environment =  testEnvironment)
	
	motor_node_d.activate(1)
	if verbose:
		print("Testing the motor node 'd'. Environment (first print) should contain 'd'. And contains:")
		print(testEnvironment.next_state)
		print(testEnvironment.next_temporal_state)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.next_temporal_state) == 0 and ("d" in testEnvironment.next_state) and len(testEnvironment.next_state) == 1)

	testEnvironment.next_state = set()
	motor_node_d.activate(2)
	motor_node_o.activate(2)
	if verbose:
		print("Testing the motor node 'd' & 'o'. Environment (first print) should contain 'd' & 'o'. And contains:")
		print(testEnvironment.next_state)
		print(testEnvironment.next_temporal_state)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.next_temporal_state) == 0 and ("d" in testEnvironment.next_state and "o" in testEnvironment.next_state) and len(testEnvironment.next_state) == 2)

	testEnvironment.next_state = set()
	motor_node_d.activate(2,True)
	motor_node_o.activate(2,True)
	if verbose:
		print("Testing the motor node 'd' & 'o'. Environment (second print) should contain 'd' & 'o'. And contains:")
		print(testEnvironment.next_state)
		print(testEnvironment.next_temporal_state)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.next_state) == 0 and len(testEnvironment.next_temporal_state) == 2 and testEnvironment.next_temporal_state[0] == "d" and testEnvironment.next_temporal_state[1] == "o")


	testEnvironment.next_temporal_state = []
	motor_node_d.active = False
	motor_node_o.active = False
	testAction_do = ActionAndNode(outputs=[motor_node_d,motor_node_o])
	testAction_do.activate(3)
	if verbose:
		print("Testing the motor node 'd&o'. Environment (first print) should contain 'd' & 'o'. And contains:")
		print(testEnvironment.next_state)
		print(testEnvironment.next_temporal_state)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.next_temporal_state) == 0 and ("d" in testEnvironment.next_state and "o" in testEnvironment.next_state) and len(testEnvironment.next_state) == 2)

	testEnvironment.next_temporal_state = []
	testEnvironment.next_state = set()
	motor_node_d.active = False
	motor_node_o.active = False

	testTemporalAction_do = TemporalASEQNode(outputs=[motor_node_d,motor_node_o])
	testTemporalAction_do.activate(4, True)
	if verbose:
		print("Testing the motor node 'do'. Environment (second print) should contain 'd' & 'o'. And contains:")
		print(testEnvironment.next_state)
		print(testEnvironment.next_temporal_state)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.next_state) == 0 and len(testEnvironment.next_temporal_state) == 2 and testEnvironment.next_temporal_state[0] == "d" and testEnvironment.next_temporal_state[1] == "o")

	testEnvironment.next_temporal_state = []
	testEnvironment.next_state = set()
	motor_node_d.active = False
	motor_node_o.active = False
	testTemporalAction_do.active = False

	testTemporalAction_dog = TemporalASEQNode(outputs=[testTemporalAction_do,motor_node_g])
	testTemporalAction_dog.activate(5, True)
	if verbose:
		print("Testing the motor node 'dog'. Environment (second print) should contain 'd' & 'o' & 'g'. And contains:")
		print(testEnvironment.next_state)
		print(testEnvironment.next_temporal_state)
	else:
		pasing_tests = pasing_tests and len(testEnvironment.next_state) == 0 and len(testEnvironment.next_temporal_state) == 3 and testEnvironment.next_temporal_state[0] == "d" and testEnvironment.next_temporal_state[1] == "o" and testEnvironment.next_temporal_state[2] == "g"

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")
	
def test_if_animat_can_hear_it_self(verbose = True):
	print ("------------------test_if_animat_can_hear_it_self------------------")
	pasing_tests = True

	testEnvironment = Environment()

	motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  testEnvironment)
	motor_node_o = MotorNode(name = "o-motor",motor = "o", environment =  testEnvironment)
	motor_node_g = MotorNode(name = "g-motor",motor = "g", environment =  testEnvironment)

	sensor_node_d = SensorNode(name = "d-sensor",sensor = "d", environment =  testEnvironment)
	sensor_node_o = SensorNode(name = "o-sensor",sensor = "o", environment =  testEnvironment)
	sensor_node_g = SensorNode(name = "g-sensor",sensor = "g", environment =  testEnvironment)

	testTemporalAction_do = TemporalASEQNode(outputs=[motor_node_d,motor_node_o])
	testTemporalAction_dog = TemporalASEQNode(outputs=[testTemporalAction_do,motor_node_g])

	t_seq_do = TemporalSEQNode(inputs = [sensor_node_d, sensor_node_o])
	t_seq_dog = TemporalSEQNode(inputs = [t_seq_do, sensor_node_g])

	all_sensor_nodes = {sensor_node_d,sensor_node_o,sensor_node_g,t_seq_do,t_seq_dog}

	testTemporalAction_dog.activate(1,True)

	if verbose:
		print("Animat says 'dog', thus environment should have 'dog'.")
		print(testEnvironment.next_temporal_state)
	else:
		pasing_tests = pasing_tests and len(testEnvironment.next_state) == 0 and len(testEnvironment.next_temporal_state) == 3 and testEnvironment.next_temporal_state[0] == "d" and testEnvironment.next_temporal_state[1] == "o" and testEnvironment.next_temporal_state[2] == "g"

	if verbose:
		print("---Updating Environment---")
	testEnvironment.state = testEnvironment.state
	testEnvironment.temporal_state = testEnvironment.next_temporal_state
	testEnvironment.state.add(testEnvironment.next_temporal_state[len(testEnvironment.next_temporal_state)-1])
	testEnvironment.next_state = set()
	testEnvironment.next_temporal_state = [];
	#Possibly add more input if wanted. 
	
	if verbose:
		print("environment should now have [dog] and {g}")
		print(testEnvironment.temporal_state)
		print(testEnvironment.state)
	else:
		pasing_tests = pasing_tests and len(testEnvironment.state) == 1 and ("g" in testEnvironment.state) and len(testEnvironment.temporal_state) == 3 and testEnvironment.temporal_state[0] == "d" and testEnvironment.temporal_state[1] == "o" and testEnvironment.temporal_state[2] == "g"

	for n in all_sensor_nodes:
		n.tick(1,0,True)
	for n in all_sensor_nodes:
		n.tick(1,1,True)
	for n in all_sensor_nodes:
		n.tick(1,2,True)

	if verbose:
		print("Animat has processed input, should now have heard 'dog'.")
		if(t_seq_dog.is_active()):
			print("THE DOG IS ACTIVE!!!!!!!!!!!!! OMG OMG")
		else:
			print("Where is the dog? :'(")
	else:
		pasing_tests = pasing_tests and t_seq_dog.is_active()

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_filereader_works(verbose = True):
	print ("------------------test_if_filereader_works------------------")
	pasing_tests = True

	file = FileReader("inputText.txt")
	#testSentence = fileReader.get_next_sentence(file)
	testSentence = file.get_next_sentence()
	if verbose:
		print("---Reading a sentence from a file:---")
		print(testSentence)
	else:
		pasing_tests = pasing_tests and testSentence == "Hello World! this is dog, the doggo master of !!!!universe??\n"

	testSentence = remove_sign_from_string(testSentence)
	if verbose:
		print("---Removing all special signs from the sentence:---")
		print(testSentence)
	else:
		pasing_tests = pasing_tests and testSentence == "Hello World this is dog the doggo master of universe"

	testList = convert_sentence_to_list(testSentence)
	if verbose:
		print("---Converting the sentence to a list of words:---")
		print(testList)
	else:
		pasing_tests = pasing_tests and len(testList) == 10 and testList[0] == "Hello" and testList[1] == "World" and testList[2] == "this" and testList[3] == "is" and testList[4] == "dog" and testList[5] == "the" and testList[6] == "doggo" and testList[7] == "master" and testList[8] == "of" and testList[9] == "universe"

	testSentence2 = convert_list_to_sentence(testList)
	if verbose:
		print("---Converting the list back into a sentence:---")
		print(testSentence2)
	else:
		pasing_tests = pasing_tests and testSentence == "Hello World this is dog the doggo master of universe"

	wordList = convert_word_to_list("doggo")
	if verbose:
		print("---Converting the word 'doggo' into a list of chars:---")
		print(wordList)
	else:
		pasing_tests = pasing_tests and len(wordList) == 5 and wordList[0] == "d" and wordList[1] == "o" and wordList[2] == "g" and wordList[3] == "g" and wordList[4] == "o"

	word = convert_list_to_word(wordList)
	if verbose:
		print("---And converting it back into a word:---")
		print(word)
	else:
		pasing_tests = pasing_tests and word == "doggo"

	if verbose:
		print("---Printing the rest of the file word by word:---")
		while not file.end_of_file:
			nextWord = file.get_next_word()
			print(nextWord)
	else:
		l = []
		while not file.end_of_file:
			nextWord = file.get_next_word()
			l.append(nextWord)
		pasing_tests = pasing_tests and len(l) == 14 and l[0] == "I" and l[1] == "am" and l[2] == "the" and l[3] == "super" and l[4] == "cat" and l[5] == "The" and l[6] == "dogs" and l[7] == "won" and l[8] == "I" and l[9] == "won" and l[10] == "People" and l[11] == "won't" and l[12] == "win" and l[13] == ""

	file.close_file()

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_filewriter_works(verbose = True):
	print ("------------------test_if_filewriter_works------------------")
	if verbose:
		print("Writing to the file 'outputText.txt'.")
	file = FileWriter("outputText.txt")

	file.write_line_to_file("Psst...")

	arr = ["Dogs","are","better","than","humans."]
	file.write_lines_to_file(arr)

	file.close_file()

	if not verbose:
		pasing_tests = True
		file2 = FileReader("outputText.txt")
		l = []
		while not file2.end_of_file:
			nextWord = file2.get_next_word()
			l.append(nextWord)
		pasing_tests = pasing_tests and len(l) == 7 and l[0] == "Psst" and l[1] == "Dogs" and l[2] == "are" and l[3] == "better" and l[4] == "than" and l[5] == "humans" and l[6] == ""
		file2.close_file()
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_new_seq_nodes_work_as_intended(verbose = True):
	print ("------------------test_if_new_seq_nodes_work_as_intended------------------")

	pasing_tests = True

	for r in range(4):
		testEnvironment = Environment()
		
		sensor_node_d = SensorNode(name = "d-sensor",sensor = "d", environment =  testEnvironment)
		sensor_node_o = SensorNode(name = "o-sensor",sensor = "o", environment =  testEnvironment)
		sensor_node_g = SensorNode(name = "g-sensor",sensor = "g", environment =  testEnvironment)

		sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  testEnvironment)
		sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  testEnvironment)
		sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  testEnvironment)

		t_seq_do = TemporalSEQNode(inputs = [sensor_node_d, sensor_node_o])
		t_seq_dog = TemporalSEQNode(inputs = [t_seq_do, sensor_node_g])

		t_seq_go = TemporalSEQNode(inputs = [sensor_node_g, sensor_node_o])
		t_seq_doggo = TemporalSEQNode(inputs = [t_seq_dog, t_seq_go])

		t_seq_at = TemporalSEQNode(inputs = [sensor_node_a, sensor_node_t])
		t_seq_cat = TemporalSEQNode(inputs = [sensor_node_c,t_seq_at])
	
		all_nodes = {sensor_node_d,sensor_node_o,sensor_node_g,t_seq_do,t_seq_dog,sensor_node_c,sensor_node_a,sensor_node_t,t_seq_at,t_seq_cat, t_seq_go, t_seq_doggo}

		word_that_should_be_active = ""
		node_that_should_be_active = None
		#r = random.randint(0, 3)
		if  r == 0:
			testEnvironment.temporal_state = ["d","o","g"]
			word_that_should_be_active = "dog"
			node_that_should_be_active = t_seq_dog
		elif r == 1:
			testEnvironment.temporal_state = ["c","a","t"]
			word_that_should_be_active = "cat"
			node_that_should_be_active = t_seq_cat
		elif r == 2:
			testEnvironment.temporal_state = ["d","o","g","g","o"]
			word_that_should_be_active = "doggo"
			node_that_should_be_active = t_seq_doggo
		else: 
			testEnvironment.temporal_state = ["d","o","g","o"]
			word_that_should_be_active = "dogo (that is not recognised)"
			node_that_should_be_active = None

		nbrTicks = len(testEnvironment.temporal_state)

		for i in range(nbrTicks):
			#print(testEnvironment.temporal_state[i])
			for n in all_nodes:
				n.tick(1,i,True)

		if verbose:
			print("The '" + word_that_should_be_active + "' should be active....")
			if(t_seq_dog.is_active()):
				print("THE DOG IS ACTIVE!!!!!!!!!!!!! OMG OMG")
			elif(t_seq_cat.is_active()):
				print("THE CAT IS ACTIVE!!!!!!!!!!!!! OMG OMG")
			elif(t_seq_doggo.is_active()):
				print("THE DOGGO IS ACTIVE!!!!!!!!!!!!! OMG OMG")
		else:
			if(not node_that_should_be_active == None):
				pasing_tests = pasing_tests and node_that_should_be_active.is_active()
			else:
				pasing_tests = pasing_tests and (not t_seq_dog.is_active()) and (not t_seq_cat.is_active()) and (not t_seq_doggo.is_active())

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")


	#print(t_seq_cat.name)
	#print(t_seq_cat.get_word())
	#print(t_seq_dog.get_word())

def test_if_controller_works():
	print("------------------test_if_controller_works------------------")
	test_environment = Environment()
	test_controller = Controller(test_environment, "inputText", "outputText") 
	test_controller.run()

def test_if_network_works(verbose = True):
	print("------------------test_if_network_works------------------")
	pasing_tests = True
	
	if verbose:
		print("Creating the network.")

	testEnvironment = Environment()
		
	sensor_node_d = SensorNode(name = "d-sensor",sensor = "d", environment =  testEnvironment)
	sensor_node_o = SensorNode(name = "o-sensor",sensor = "o", environment =  testEnvironment)
	sensor_node_g = SensorNode(name = "g-sensor",sensor = "g", environment =  testEnvironment)

	sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  testEnvironment)
	sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  testEnvironment)
	sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  testEnvironment)

	motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  testEnvironment)
	motor_node_o = MotorNode(name = "o-motor",motor = "o", environment =  testEnvironment)
	motor_node_g = MotorNode(name = "g-motor",motor = "g", environment =  testEnvironment)

	t_seq_do = TemporalSEQNode(inputs = [sensor_node_d, sensor_node_o])
	t_seq_dog = TemporalSEQNode(inputs = [t_seq_do, sensor_node_g])

	t_seq_go = TemporalSEQNode(inputs = [sensor_node_g, sensor_node_o])
	t_seq_doggo = TemporalSEQNode(inputs = [t_seq_dog, t_seq_go])

	t_seq_at = TemporalSEQNode(inputs = [sensor_node_a, sensor_node_t])
	t_seq_cat = TemporalSEQNode(inputs = [sensor_node_c,t_seq_at])

	sensors = [sensor_node_d, sensor_node_o, sensor_node_g, sensor_node_c, sensor_node_a, sensor_node_t]
	perception_nodes = [t_seq_do, t_seq_dog, t_seq_at, t_seq_cat]
	motors = [motor_node_d, motor_node_o, motor_node_g]

	test_network = Network(sensors = sensors, perception_nodes = perception_nodes, motors = motors)

	t = 0

	if verbose:
		print("Testing if it can recognise dog.")

	testEnvironment.temporal_state = ["d","o","g"]

	nbrTicks = len(testEnvironment.temporal_state)
	t = t+1
	for i in range(nbrTicks):
		test_network.temporal_tick(t,i)

	if verbose:
		if t_seq_dog.active:
			print("The dog is active! :)")
		else:
			print("No dog? :'(")
	else:
		pasing_tests = pasing_tests and t_seq_dog.active


	if verbose:
		print("Testing if it can recognise cat.")

	testEnvironment.temporal_state = ["c","a","t"]

	nbrTicks = len(testEnvironment.temporal_state)
	t = t+1
	for i in range(nbrTicks):
		test_network.temporal_tick(t,i)

	if verbose:
		if t_seq_cat.active:
			print("The cat is active! :)")
		else:
			print("No cat? :'(")
	else:
		pasing_tests = pasing_tests and t_seq_cat.active


	if verbose:
		print("Testing if a 'go' node can be added.")
	test_network.add_perception_node(t_seq_go)
	if verbose:
		test_network.print_network()
	else:
		pasing_tests = pasing_tests and (t_seq_go in test_network.perception_nodes)

	test_network.add_perception_node(t_seq_doggo)

	if verbose:
		print("Testing if it can recognise doggo.")
	testEnvironment.temporal_state = ["d","o","g","g","o"]
	nbrTicks = len(testEnvironment.temporal_state)
	t = t+1
	for i in range(nbrTicks):
		test_network.temporal_tick(t,i)
	if verbose:
		if t_seq_doggo.active:
			print("The doggo is active! :)")
		else:
			print("No doggo? :'(")
	else:
		pasing_tests = pasing_tests and t_seq_doggo.active

	if verbose:
		print("Testing removal of nodes. The 'do' node should not be possible to remove.")
	v = test_network.remove_perception_node(t_seq_do)
	if verbose:
		test_network.print_network()
	else:
		pasing_tests = pasing_tests and (t_seq_do in test_network.perception_nodes) and not v

	if verbose:
		print("Testing removal of nodes. The 'doggo' node should be removed.")
	v = test_network.remove_perception_node(t_seq_doggo)
	if verbose:
		test_network.print_network()
	else:
		pasing_tests = pasing_tests and not (t_seq_doggo in test_network.perception_nodes) and v

	if verbose:
		print("Testing if it can no longer recognise doggo.")
	t_seq_doggo.active = False
	testEnvironment.temporal_state = ["d","o","g","g","o"]
	nbrTicks = len(testEnvironment.temporal_state)
	t = t+1
	for i in range(nbrTicks):
		test_network.temporal_tick(t,i)
	if verbose:
		if t_seq_doggo.active:
			print("The doggo is active!? .....")
		else:
			print("No doggo. ok.")
	else:
		pasing_tests = pasing_tests and not t_seq_doggo.active


	if verbose:
		print("Testing the identification of topactive nodes while recognising 'dog'.")

	testEnvironment.temporal_state = ["d","o","g"]
	nbrTicks = len(testEnvironment.temporal_state)
	t = t+1
	i = 0
	test_network.temporal_tick(t,i)
	t_a = test_network.get_topactive_nodes()
	if verbose:
		print("---")
		for n in t_a:
			print(n.get_word())
	else:
		pasing_tests = pasing_tests and sensor_node_d in t_a and len(t_a) == 2 #including true node
	t = t+1
	i = i+1
	test_network.temporal_tick(t,i)
	t_a = test_network.get_topactive_nodes()
	if verbose:
		print("---")
		for n in t_a:
			print(n.get_word())
	else:
		pasing_tests = pasing_tests and t_seq_do in t_a and len(t_a) == 2 #including true node
	t = t+1
	i = i+1
	test_network.temporal_tick(t,i)
	t_a = test_network.get_topactive_nodes()
	if verbose:
		print("---")
		for n in t_a:
			print(n.get_word())
	else:
		pasing_tests = pasing_tests and t_seq_dog in t_a and len(t_a) == 2 #including true node
	

	if verbose:
		print("Testing the update_previous_active method")
	test_network.deactivate_all_nodes()
	t_seq_doggo.active = True #since this is not in the network, it should NOT be updated by update_previous_active()
	t_seq_cat.active = True
	t_seq_go.active = True
	sensor_node_o.active = True
	sensor_node_a.active = True
	test_network.update_previous_active()
	if verbose:
		test_network.print_network()
	else:
		pasing_tests = pasing_tests and not t_seq_doggo.was_active() and t_seq_cat.was_active() and t_seq_go.was_active() and sensor_node_o.was_active() and sensor_node_a.was_active()
		pasing_tests = pasing_tests and not t_seq_do.was_active() and not t_seq_dog.was_active() and not t_seq_at.was_active() and not sensor_node_d.was_active() and not sensor_node_g.was_active() and not sensor_node_c.was_active() and not sensor_node_t.was_active()

	if verbose:
		print("Testing the add_action_node method")
	test_action_do = TemporalASEQNode(outputs=[motor_node_d,motor_node_o])
	test_network.add_action_node(test_action_do)
	if verbose:
		print("Action node 'do' should be in network")
		test_network.print_network()
	else:
		pasing_tests = pasing_tests and test_action_do in test_network.action_nodes


	if verbose:
		print("Testing the removal of action nodes")
	test_action_dog = TemporalASEQNode(outputs=[test_action_do,motor_node_g])
	test_network.add_action_node(test_action_dog)

	test_network.remove_action_node(test_action_do)
	if verbose:
		print("Attempting to remove 'do' node. Should still be in network.")
		test_network.print_network()
	else:
		pasing_tests = pasing_tests and test_action_do in test_network.action_nodes

	test_network.remove_action_node(test_action_dog)
	if verbose:
		print("Attempting to remove 'dog' node. Should be removed from network.")
		test_network.print_network()
	else:
		pasing_tests = pasing_tests and not test_action_dog in test_network.action_nodes









	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_animat_can_run_first_step_code():
	print("------------------test_if_animat_can_run_first_step_code------------------")

	test_environment = Environment()
		
	sensor_node_d = SensorNode(name = "d-sensor",sensor = "d", environment =  test_environment)
	sensor_node_o = SensorNode(name = "o-sensor",sensor = "o", environment =  test_environment)
	sensor_node_g = SensorNode(name = "g-sensor",sensor = "g", environment =  test_environment)

	#sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  test_environment)
	#sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  test_environment)
	#sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  test_environment)

	motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  test_environment)
	motor_node_o = MotorNode(name = "o-motor",motor = "o", environment =  test_environment)
	motor_node_g = MotorNode(name = "g-motor",motor = "g", environment =  test_environment)

	#(self, name = None, sensors = [], motors = [], perception_nodes = [], action_nodes = [], memory_capacity = 0, temporal_memory_capacity = 0):
	sensors = [sensor_node_d, sensor_node_o, sensor_node_g]
	motors = [motor_node_d, motor_node_o, motor_node_g]

	test_animat = Animat("TheDoggo", sensors, motors)

	for x in range(1, 10): #If from 0, the change in node.py is needed to avoid error.
		test_animat.update_step_one_version(x)
		test_environment.update()

	print("")
	print("Printing all the sensor nodes in order:")
	print("\t[true, 'd', 'o', 'g']")
	print("Printing all the motor nodes in order:")
	print("\t['d', 'o', 'g']")
	print("Now printing the generator list in the Animat:")
	print(test_animat.network.generator_list)

def test_if_animat_can_learn_alphabet_in_step_one(verbose = True):
	print("------------------test_if_animat_can_learn_alphabet_in_step_one------------------")

	test_environment = Environment()
		
	sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  test_environment)
	sensor_node_b = SensorNode(name = "b-sensor",sensor = "b", environment =  test_environment)
	sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  test_environment)
	sensor_node_d = SensorNode(name = "d-sensor",sensor = "d", environment =  test_environment)
	sensor_node_e = SensorNode(name = "e-sensor",sensor = "e", environment =  test_environment)
	sensor_node_f = SensorNode(name = "f-sensor",sensor = "f", environment =  test_environment)
	sensor_node_g = SensorNode(name = "g-sensor",sensor = "g", environment =  test_environment)
	sensor_node_h = SensorNode(name = "h-sensor",sensor = "h", environment =  test_environment)
	sensor_node_i = SensorNode(name = "i-sensor",sensor = "i", environment =  test_environment)
	sensor_node_j = SensorNode(name = "j-sensor",sensor = "j", environment =  test_environment)
	sensor_node_k = SensorNode(name = "k-sensor",sensor = "k", environment =  test_environment)
	sensor_node_l = SensorNode(name = "l-sensor",sensor = "l", environment =  test_environment)
	sensor_node_m = SensorNode(name = "m-sensor",sensor = "m", environment =  test_environment)
	sensor_node_n = SensorNode(name = "n-sensor",sensor = "n", environment =  test_environment)
	sensor_node_o = SensorNode(name = "o-sensor",sensor = "o", environment =  test_environment)
	sensor_node_p = SensorNode(name = "p-sensor",sensor = "p", environment =  test_environment)
	sensor_node_q = SensorNode(name = "q-sensor",sensor = "q", environment =  test_environment)
	sensor_node_r = SensorNode(name = "r-sensor",sensor = "r", environment =  test_environment)
	sensor_node_s = SensorNode(name = "s-sensor",sensor = "s", environment =  test_environment)
	sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  test_environment)
	sensor_node_u = SensorNode(name = "u-sensor",sensor = "u", environment =  test_environment)
	sensor_node_v = SensorNode(name = "v-sensor",sensor = "v", environment =  test_environment)
	sensor_node_w = SensorNode(name = "w-sensor",sensor = "w", environment =  test_environment)
	sensor_node_x = SensorNode(name = "x-sensor",sensor = "x", environment =  test_environment)
	sensor_node_y = SensorNode(name = "y-sensor",sensor = "y", environment =  test_environment)
	sensor_node_z = SensorNode(name = "z-sensor",sensor = "z", environment =  test_environment)

	#sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  test_environment)
	#sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  test_environment)
	#sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  test_environment)

	#motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  test_environment)
	motor_node_a = MotorNode(name = "a-motor",motor = "a", environment =  test_environment)
	motor_node_b = MotorNode(name = "b-motor",motor = "b", environment =  test_environment)
	motor_node_c = MotorNode(name = "c-motor",motor = "c", environment =  test_environment)
	motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  test_environment)
	motor_node_e = MotorNode(name = "e-motor",motor = "e", environment =  test_environment)
	motor_node_f = MotorNode(name = "f-motor",motor = "f", environment =  test_environment)
	motor_node_g = MotorNode(name = "g-motor",motor = "g", environment =  test_environment)
	motor_node_h = MotorNode(name = "h-motor",motor = "h", environment =  test_environment)
	motor_node_i = MotorNode(name = "i-motor",motor = "i", environment =  test_environment)
	motor_node_j = MotorNode(name = "j-motor",motor = "j", environment =  test_environment)
	motor_node_k = MotorNode(name = "k-motor",motor = "k", environment =  test_environment)
	motor_node_l = MotorNode(name = "l-motor",motor = "l", environment =  test_environment)
	motor_node_m = MotorNode(name = "m-motor",motor = "m", environment =  test_environment)
	motor_node_n = MotorNode(name = "n-motor",motor = "n", environment =  test_environment)
	motor_node_o = MotorNode(name = "o-motor",motor = "o", environment =  test_environment)
	motor_node_p = MotorNode(name = "p-motor",motor = "p", environment =  test_environment)
	motor_node_q = MotorNode(name = "q-motor",motor = "q", environment =  test_environment)
	motor_node_r = MotorNode(name = "r-motor",motor = "r", environment =  test_environment)
	motor_node_s = MotorNode(name = "s-motor",motor = "s", environment =  test_environment)
	motor_node_t = MotorNode(name = "t-motor",motor = "t", environment =  test_environment)
	motor_node_u = MotorNode(name = "u-motor",motor = "u", environment =  test_environment)
	motor_node_v = MotorNode(name = "v-motor",motor = "v", environment =  test_environment)
	motor_node_w = MotorNode(name = "w-motor",motor = "w", environment =  test_environment)
	motor_node_x = MotorNode(name = "x-motor",motor = "x", environment =  test_environment)
	motor_node_y = MotorNode(name = "y-motor",motor = "y", environment =  test_environment)
	motor_node_z = MotorNode(name = "z-motor",motor = "z", environment =  test_environment)

	sensors = [sensor_node_a, sensor_node_b, sensor_node_c, sensor_node_d, sensor_node_e, sensor_node_f, sensor_node_g, sensor_node_h, sensor_node_i, sensor_node_j, sensor_node_k, sensor_node_l, sensor_node_m, sensor_node_n, sensor_node_o, sensor_node_p, sensor_node_q, sensor_node_r, sensor_node_s, sensor_node_t, sensor_node_u, sensor_node_v, sensor_node_w, sensor_node_x, sensor_node_y, sensor_node_z]
	motors = [motor_node_a, motor_node_b, motor_node_c, motor_node_d, motor_node_e, motor_node_f, motor_node_g, motor_node_h, motor_node_i, motor_node_j, motor_node_k, motor_node_l, motor_node_m, motor_node_n, motor_node_o, motor_node_p, motor_node_q, motor_node_r, motor_node_s, motor_node_t, motor_node_u, motor_node_v, motor_node_w, motor_node_x, motor_node_y, motor_node_z]

	from random import shuffle
	shuffle(sensors)
	shuffle(motors)

	test_animat = Animat("TheDoggo", sensors, motors)

	for x in range(1, 100): #If from 0, the change in node.py is needed to avoid error.
		test_animat.update_step_one_version(x)
		test_environment.update()

	generators = test_animat.network.generator_list

	passing_tests = True

	for node in sensors:
		index = node.get_index()
		generator_index = generators[index]
		if generator_index == -1:
			if verbose:
				print("Sensor for %s, does not have a generator." % (node.get_word()))
			passing_tests = False
		else:
			if verbose:
				print("Sensor for %s, having generator number %d, that produces %s." % (node.get_word(), generator_index, motors[generator_index].get_word()))
			passing_tests = passing_tests and (node.get_word() == motors[generator_index].get_word())
	
	if passing_tests:
		print("All tests pased.")
	else:
		print("Tests failed (might be due to stochasticity)")

def test_how_often_the_animat_learns_the_entire_alphabet():	
	print("------------------test_how_often_the_animat_learns_the_entire_alphabet------------------")
	import numpy as np
	avg_nbr = 100
	tests_to_run = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]

	print("Running tests with the nomber of iterations to babble set to:")
	print(tests_to_run)
	print("And averages over %d averaging runs." % (avg_nbr))

	results_all_generators_found = []
	results_avg_number_of_generators_found = []

	for nbr_iterations in tests_to_run:
		#start a test
		stats = np.zeros(avg_nbr)
		for test_number in range(1,avg_nbr+1): #run test several (avg_nbr) times to average.
			test_environment = Environment()
		
			sensors, motors = create_nodes_for_alphabet(test_environment)
		
			totlal_number_of_sensors = len(sensors)

			from random import shuffle
			shuffle(sensors)
			shuffle(motors)

			test_animat = Animat("TheDoggo", sensors, motors)
			#number_of_babble_iterations = nbr_iterations

			#let the animat learn
			for x in range(1, nbr_iterations+1): #+1 needed ass the loop does NOT include the last iteration
				test_animat.update(x)
				test_environment.update()

			generators = test_animat.network.generator_list

			number_of_correct_generators = 0
			for node in sensors:
				index = node.get_index()
				generator_index = generators[index]
				if not generator_index == -1: #does have a generator.
					if node.get_word() == motors[generator_index].get_word(): #is the right sensor.
						number_of_correct_generators = number_of_correct_generators + 1

			stats[test_number-1] = number_of_correct_generators
			#print("Number of correct generators is %d of %d, when babbling for %d iterations." % (number_of_correct_generators, totlal_number_of_sensors, nbr_iterations))
		#print(stats)
		result = sum([value == totlal_number_of_sensors for value in stats])
		#print(result)
		
		avg_number_of_generators_found = sum(stats)/avg_nbr

		results_all_generators_found.append(result/avg_nbr)
		#results_avg_number_of_generators_found.append(avg_number_of_generators_found/totlal_number_of_sensors)
		results_avg_number_of_generators_found.append(float(format(avg_number_of_generators_found/totlal_number_of_sensors, '.2f')))
	
	print("Percentage of times that all generators were found for the different tests:")
	print(results_all_generators_found)
	print("Average percentage of generators found for the different tests:")
	print(results_avg_number_of_generators_found)

	file = FileWriter("output/babbling_result.m")
	file.write_line_to_file("clear all, clf, clc")
	file.write_line_to_file("%The tests to run")
	file.write_line_to_file("tests_to_run = "+str(tests_to_run))
	file.write_line_to_file("%Percentage of times that all generators were found for the different tests:")
	file.write_line_to_file("results_all_generators_found = "+str(results_all_generators_found))
	file.write_line_to_file("% Average percentage of generators found for the different tests:")
	file.write_line_to_file("results_avg_number_of_generators_found = "+str(results_avg_number_of_generators_found))
	file.write_line_to_file("plot(tests_to_run,results_all_generators_found)")
	file.write_line_to_file("figure")
	file.write_line_to_file("yyaxis left")
	file.write_line_to_file("ylabel('Percentage of runs where all generators were found')")
	file.write_line_to_file("plot(tests_to_run,results_all_generators_found)")
	file.write_line_to_file("hold on")
	file.write_line_to_file("yyaxis right")
	file.write_line_to_file("ylabel('Average number of generators found');")
	file.write_line_to_file("plot(tests_to_run,results_avg_number_of_generators_found)")
	file.write_line_to_file("title('Statistics of how well the Animat finds generators');")
	file.write_line_to_file("xlabel('Number of timesteps spent babbling');")
	#file.write_line_to_file("legend('Runs where all generators were found','Average number of generators found','Location','east')")

def create_nodes_for_alphabet(test_environment):
	sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  test_environment)
	sensor_node_b = SensorNode(name = "b-sensor",sensor = "b", environment =  test_environment)
	sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  test_environment)
	sensor_node_d = SensorNode(name = "d-sensor",sensor = "d", environment =  test_environment)
	sensor_node_e = SensorNode(name = "e-sensor",sensor = "e", environment =  test_environment)
	sensor_node_f = SensorNode(name = "f-sensor",sensor = "f", environment =  test_environment)
	sensor_node_g = SensorNode(name = "g-sensor",sensor = "g", environment =  test_environment)
	sensor_node_h = SensorNode(name = "h-sensor",sensor = "h", environment =  test_environment)
	sensor_node_i = SensorNode(name = "i-sensor",sensor = "i", environment =  test_environment)
	sensor_node_j = SensorNode(name = "j-sensor",sensor = "j", environment =  test_environment)
	sensor_node_k = SensorNode(name = "k-sensor",sensor = "k", environment =  test_environment)
	sensor_node_l = SensorNode(name = "l-sensor",sensor = "l", environment =  test_environment)
	sensor_node_m = SensorNode(name = "m-sensor",sensor = "m", environment =  test_environment)
	sensor_node_n = SensorNode(name = "n-sensor",sensor = "n", environment =  test_environment)
	sensor_node_o = SensorNode(name = "o-sensor",sensor = "o", environment =  test_environment)
	sensor_node_p = SensorNode(name = "p-sensor",sensor = "p", environment =  test_environment)
	sensor_node_q = SensorNode(name = "q-sensor",sensor = "q", environment =  test_environment)
	sensor_node_r = SensorNode(name = "r-sensor",sensor = "r", environment =  test_environment)
	sensor_node_s = SensorNode(name = "s-sensor",sensor = "s", environment =  test_environment)
	sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  test_environment)
	sensor_node_u = SensorNode(name = "u-sensor",sensor = "u", environment =  test_environment)
	sensor_node_v = SensorNode(name = "v-sensor",sensor = "v", environment =  test_environment)
	sensor_node_w = SensorNode(name = "w-sensor",sensor = "w", environment =  test_environment)
	sensor_node_x = SensorNode(name = "x-sensor",sensor = "x", environment =  test_environment)
	sensor_node_y = SensorNode(name = "y-sensor",sensor = "y", environment =  test_environment)
	sensor_node_z = SensorNode(name = "z-sensor",sensor = "z", environment =  test_environment)

	motor_node_a = MotorNode(name = "a-motor",motor = "a", environment =  test_environment)
	motor_node_b = MotorNode(name = "b-motor",motor = "b", environment =  test_environment)
	motor_node_c = MotorNode(name = "c-motor",motor = "c", environment =  test_environment)
	motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  test_environment)
	motor_node_e = MotorNode(name = "e-motor",motor = "e", environment =  test_environment)
	motor_node_f = MotorNode(name = "f-motor",motor = "f", environment =  test_environment)
	motor_node_g = MotorNode(name = "g-motor",motor = "g", environment =  test_environment)
	motor_node_h = MotorNode(name = "h-motor",motor = "h", environment =  test_environment)
	motor_node_i = MotorNode(name = "i-motor",motor = "i", environment =  test_environment)
	motor_node_j = MotorNode(name = "j-motor",motor = "j", environment =  test_environment)
	motor_node_k = MotorNode(name = "k-motor",motor = "k", environment =  test_environment)
	motor_node_l = MotorNode(name = "l-motor",motor = "l", environment =  test_environment)
	motor_node_m = MotorNode(name = "m-motor",motor = "m", environment =  test_environment)
	motor_node_n = MotorNode(name = "n-motor",motor = "n", environment =  test_environment)
	motor_node_o = MotorNode(name = "o-motor",motor = "o", environment =  test_environment)
	motor_node_p = MotorNode(name = "p-motor",motor = "p", environment =  test_environment)
	motor_node_q = MotorNode(name = "q-motor",motor = "q", environment =  test_environment)
	motor_node_r = MotorNode(name = "r-motor",motor = "r", environment =  test_environment)
	motor_node_s = MotorNode(name = "s-motor",motor = "s", environment =  test_environment)
	motor_node_t = MotorNode(name = "t-motor",motor = "t", environment =  test_environment)
	motor_node_u = MotorNode(name = "u-motor",motor = "u", environment =  test_environment)
	motor_node_v = MotorNode(name = "v-motor",motor = "v", environment =  test_environment)
	motor_node_w = MotorNode(name = "w-motor",motor = "w", environment =  test_environment)
	motor_node_x = MotorNode(name = "x-motor",motor = "x", environment =  test_environment)
	motor_node_y = MotorNode(name = "y-motor",motor = "y", environment =  test_environment)
	motor_node_z = MotorNode(name = "z-motor",motor = "z", environment =  test_environment)

	sensors = [sensor_node_a, sensor_node_b, sensor_node_c, sensor_node_d, sensor_node_e, sensor_node_f, sensor_node_g, sensor_node_h, sensor_node_i, sensor_node_j, sensor_node_k, sensor_node_l, sensor_node_m, sensor_node_n, sensor_node_o, sensor_node_p, sensor_node_q, sensor_node_r, sensor_node_s, sensor_node_t, sensor_node_u, sensor_node_v, sensor_node_w, sensor_node_x, sensor_node_y, sensor_node_z]
	motors = [motor_node_a, motor_node_b, motor_node_c, motor_node_d, motor_node_e, motor_node_f, motor_node_g, motor_node_h, motor_node_i, motor_node_j, motor_node_k, motor_node_l, motor_node_m, motor_node_n, motor_node_o, motor_node_p, motor_node_q, motor_node_r, motor_node_s, motor_node_t, motor_node_u, motor_node_v, motor_node_w, motor_node_x, motor_node_y, motor_node_z]

	from random import shuffle
	shuffle(sensors)
	shuffle(motors)

	return sensors, motors

def test_step_two_animat():
	print("------------------test_step_two_animat------------------")
	test_environment = Environment()	
	#sensors, motors = create_nodes_for_alphabet(test_environment)

	sensor_node_c = SensorNode(name = "c-sensor",sensor = "c", environment =  test_environment)
	sensor_node_a = SensorNode(name = "a-sensor",sensor = "a", environment =  test_environment)
	sensor_node_t = SensorNode(name = "t-sensor",sensor = "t", environment =  test_environment)

	motor_node_c = MotorNode(name = "c-motor",motor = "c", environment =  test_environment)
	motor_node_a = MotorNode(name = "a-motor",motor = "a", environment =  test_environment)
	motor_node_t = MotorNode(name = "t-motor",motor = "t", environment =  test_environment)

	sensors = [sensor_node_c,sensor_node_a,sensor_node_t]
	motors = [motor_node_c,motor_node_a,motor_node_t]

	totlal_number_of_sensors = len(sensors)
	test_animat = Animat("TheCat", sensors, motors, temporal_memory_capacity = 5, seq_formation_probability = 1/25)

	test_environment.temporal_state = ["c","a","t"]

	for t in range(1,501):
	#	print("------------------------")
		test_animat.update(t,3)
	#test_animat.update(1,3)

	print("Done ish")
	#print(test_animat.network.temporal_sequence_matrix)
	#mat = copy(test_animat.network.temporal_sequence_matrix)
	mat = np.zeros(test_animat.network.temporal_sequence_matrix.shape)
	for i in range(0,test_animat.network.temporal_sequence_matrix.shape[0]):
		for j in range(0,test_animat.network.temporal_sequence_matrix.shape[1]):
			v = test_animat.network.temporal_sequence_matrix[i][j]
			if not v == 0:
				mat[i][j] = len(v)
	#print("\nSimpler form:")
	print(mat)

	print("perception nodes: ")
	print([n.name for n in test_animat.network.perception_nodes])

	
def run_tests(verbose = False):
	print ("------------------------------------Starting Tests------------------------------------")
	if(True):
		test_if_nodes_update_when_they_should(verbose)
		test_if_nodes_update_to_the_value_they_should(verbose)
		test_if_sensors_react_to_input(verbose)
		test_if_dog_can_be_found(verbose)
		test_if_motors_produce_things(verbose)
		test_if_animat_can_hear_it_self(verbose)
		test_if_filereader_works(verbose)
		test_if_filewriter_works(verbose)
		test_if_new_seq_nodes_work_as_intended(verbose)
		test_if_controller_works()
		test_if_network_works(verbose)
		test_if_animat_can_run_first_step_code()
		test_if_animat_can_learn_alphabet_in_step_one(verbose)
#	test_how_often_the_animat_learns_the_entire_alphabet() #Note, this is slow. Prints statistics of how often the Animat learns generators.
	test_step_two_animat() 


