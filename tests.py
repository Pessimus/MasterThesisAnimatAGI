from node import *
from nodes import *
from temporalNodes import *
from environment import *
from actionNodes import *
from temporalActionNodes import *
from textHandler import *
from controller import *
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
		print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not seqNodeTestNode.isActive())
	dummy1.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not seqNodeTestNode.isActive())
	dummy1.active = False
	dummy2.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not seqNodeTestNode.isActive())
	dummy1.active = True
	dummy2.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not seqNodeTestNode.isActive())
	dummy1.previousActive = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	if verbose:
		print("\t should be True,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (seqNodeTestNode.isActive())

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
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.isActive())
	dummy1.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.isActive())
	dummy1.active = False
	dummy2.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.isActive())
	dummy1.active = True
	dummy2.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.isActive())
	dummy1.previousActive = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (not temporalSeqNodeTestNode.isActive())
	dummy1.previousTemporalActive = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	if verbose:
		print("\t should be True,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	else:
		pasing_tests = pasing_tests and (temporalSeqNodeTestNode.isActive())

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
		print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))
	else:
		pasing_tests = pasing_tests and (not testSensor.isActive())

	testSensor.tick(i, 1, True)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))
	else:
		pasing_tests = pasing_tests and (not testSensor.isActive())

	testEnvironment.state = {"d", "o", "g"}
	i=i+1
	testSensor.tick(i)
	if verbose:
		print("\t should be True,\n\t -------is %s" % (testSensor.isActive()))
	else:
		pasing_tests = pasing_tests and (testSensor.isActive())

	testEnvironment.state = {"g", "o", "g"}
	i=i+1
	testSensor.tick(i)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))
	else:
		pasing_tests = pasing_tests and (not testSensor.isActive())

	testEnvironment.temporalState = ["d", "o", "g"]
	i=i+1
	testSensor.tick(i, 1, True)
	if verbose:
		print("\t should be True,\n\t -------is %s" % (testSensor.isActive()))
	else:
		pasing_tests = pasing_tests and (testSensor.isActive())

	testSensor.tick(i, 2, True)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))
	else:
		pasing_tests = pasing_tests and (not testSensor.isActive())

	testEnvironment.state = {"d", "o", "g"}
	testSensor.tick(i, 3, True)
	if verbose:
		print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))
	else:
		pasing_tests = pasing_tests and (not testSensor.isActive())

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
			testEnvironment.temporalState = ["d","o","g"]
		else:
			testEnvironment.temporalState = ["c","a","t"]

		for n in all_nodes:
			n.tick(1,1,True)

		#print(sensor_node_d.isActive())
		#print("--1--")

		for n in all_nodes:
			n.tick(1,2,True)

		#print(sensor_node_o.isActive())
		#print(t_seq_do.isActive())
		#print("--2--")

		for n in all_nodes:
			n.tick(1,3,True)

		#print(sensor_node_g.isActive())
		#print(t_seq_ca.isActive())
		#print(t_seq_cat.isActive())
		#print("--3--")
		if verbose:
			if(t_seq_dog.isActive()):
				print("THE DOG IS ACTIVE!!!!!!!!!!!!! OMG OMG")

			if(t_seq_cat.isActive()):
				print("THE CAT IS ACTIVE!!!!!!!!!!!!! OMG OMG")

			print(t_seq_cat.name)
			print(t_seq_cat.getWord())
			print(t_seq_dog.getWord())
		else:
			if(r == 1):
				pasing_tests = pasing_tests and t_seq_dog.isActive()
			else:
				pasing_tests = pasing_tests and t_seq_cat.isActive()

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
		print(testEnvironment.nextState)
		print(testEnvironment.nextTemporalState)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.nextTemporalState) == 0 and ("d" in testEnvironment.nextState) and len(testEnvironment.nextState) == 1)

	testEnvironment.nextState = set()
	motor_node_d.activate(2)
	motor_node_o.activate(2)
	if verbose:
		print("Testing the motor node 'd' & 'o'. Environment (first print) should contain 'd' & 'o'. And contains:")
		print(testEnvironment.nextState)
		print(testEnvironment.nextTemporalState)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.nextTemporalState) == 0 and ("d" in testEnvironment.nextState and "o" in testEnvironment.nextState) and len(testEnvironment.nextState) == 2)

	testEnvironment.nextState = set()
	motor_node_d.activate(2,True)
	motor_node_o.activate(2,True)
	if verbose:
		print("Testing the motor node 'd' & 'o'. Environment (second print) should contain 'd' & 'o'. And contains:")
		print(testEnvironment.nextState)
		print(testEnvironment.nextTemporalState)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.nextState) == 0 and len(testEnvironment.nextTemporalState) == 2 and testEnvironment.nextTemporalState[0] == "d" and testEnvironment.nextTemporalState[1] == "o")


	testEnvironment.nextTemporalState = []
	motor_node_d.active = False
	motor_node_o.active = False
	testAction_do = ActionAndNode(outputs=[motor_node_d,motor_node_o])
	testAction_do.activate(3)
	if verbose:
		print("Testing the motor node 'd&o'. Environment (first print) should contain 'd' & 'o'. And contains:")
		print(testEnvironment.nextState)
		print(testEnvironment.nextTemporalState)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.nextTemporalState) == 0 and ("d" in testEnvironment.nextState and "o" in testEnvironment.nextState) and len(testEnvironment.nextState) == 2)

	testEnvironment.nextTemporalState = []
	testEnvironment.nextState = set()
	motor_node_d.active = False
	motor_node_o.active = False

	testTemporalAction_do = TemporalASEQNode(outputs=[motor_node_d,motor_node_o])
	testTemporalAction_do.activate(4, True)
	if verbose:
		print("Testing the motor node 'do'. Environment (second print) should contain 'd' & 'o'. And contains:")
		print(testEnvironment.nextState)
		print(testEnvironment.nextTemporalState)
	else:
		pasing_tests = pasing_tests and (len(testEnvironment.nextState) == 0 and len(testEnvironment.nextTemporalState) == 2 and testEnvironment.nextTemporalState[0] == "d" and testEnvironment.nextTemporalState[1] == "o")

	testEnvironment.nextTemporalState = []
	testEnvironment.nextState = set()
	motor_node_d.active = False
	motor_node_o.active = False
	testTemporalAction_do.active = False

	testTemporalAction_dog = TemporalASEQNode(outputs=[testTemporalAction_do,motor_node_g])
	testTemporalAction_dog.activate(5, True)
	if verbose:
		print("Testing the motor node 'dog'. Environment (second print) should contain 'd' & 'o' & 'g'. And contains:")
		print(testEnvironment.nextState)
		print(testEnvironment.nextTemporalState)
	else:
		pasing_tests = pasing_tests and len(testEnvironment.nextState) == 0 and len(testEnvironment.nextTemporalState) == 3 and testEnvironment.nextTemporalState[0] == "d" and testEnvironment.nextTemporalState[1] == "o" and testEnvironment.nextTemporalState[2] == "g"

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
		print(testEnvironment.nextTemporalState)
	else:
		pasing_tests = pasing_tests and len(testEnvironment.nextState) == 0 and len(testEnvironment.nextTemporalState) == 3 and testEnvironment.nextTemporalState[0] == "d" and testEnvironment.nextTemporalState[1] == "o" and testEnvironment.nextTemporalState[2] == "g"

	if verbose:
		print("---Updating Environment---")
	testEnvironment.state = testEnvironment.state
	testEnvironment.temporalState = testEnvironment.nextTemporalState
	testEnvironment.state.add(testEnvironment.nextTemporalState[len(testEnvironment.nextTemporalState)-1])
	testEnvironment.nextState = set()
	testEnvironment.nextTemporalState = [];
	#Possibly add more input if wanted. 
	
	if verbose:
		print("environment should now have [dog] and {g}")
		print(testEnvironment.temporalState)
		print(testEnvironment.state)
	else:
		pasing_tests = pasing_tests and len(testEnvironment.state) == 1 and ("g" in testEnvironment.state) and len(testEnvironment.temporalState) == 3 and testEnvironment.temporalState[0] == "d" and testEnvironment.temporalState[1] == "o" and testEnvironment.temporalState[2] == "g"

	for n in all_sensor_nodes:
		n.tick(1,1,True)
	for n in all_sensor_nodes:
		n.tick(1,2,True)
	for n in all_sensor_nodes:
		n.tick(1,3,True)

	if verbose:
		print("Animat has processed input, should now have heard 'dog'.")
		if(t_seq_dog.isActive()):
			print("THE DOG IS ACTIVE!!!!!!!!!!!!! OMG OMG")
		else:
			print("Where is the dog? :'(")
	else:
		pasing_tests = pasing_tests and t_seq_dog.isActive()

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_filereader_works(verbose = True):
	print ("------------------test_if_filereader_works------------------")
	pasing_tests = True

	file = fileReader("inputText.txt")
	testSentence = fileReader.getNextSentence(file)
	if verbose:
		print("---Reading a sentence from a file:---")
		print(testSentence)
	else:
		pasing_tests = pasing_tests and testSentence == "Hello World! this is dog, the doggo master of !!!!universe??\n"

	testSentence = removeSignFromString(testSentence)
	if verbose:
		print("---Removing all special signs from the sentence:---")
		print(testSentence)
	else:
		pasing_tests = pasing_tests and testSentence == "Hello World this is dog the doggo master of universe"

	testList = convertSentenceToList(testSentence)
	if verbose:
		print("---Converting the sentence to a list of words:---")
		print(testList)
	else:
		pasing_tests = pasing_tests and len(testList) == 10 and testList[0] == "Hello" and testList[1] == "World" and testList[2] == "this" and testList[3] == "is" and testList[4] == "dog" and testList[5] == "the" and testList[6] == "doggo" and testList[7] == "master" and testList[8] == "of" and testList[9] == "universe"

	testSentence2 = convertListToSentence(testList)
	if verbose:
		print("---Converting the list back into a sentence:---")
		print(testSentence2)
	else:
		pasing_tests = pasing_tests and testSentence == "Hello World this is dog the doggo master of universe"

	wordList = convertWordToList("doggo")
	if verbose:
		print("---Converting the word 'doggo' into a list of chars:---")
		print(wordList)
	else:
		pasing_tests = pasing_tests and len(wordList) == 5 and wordList[0] == "d" and wordList[1] == "o" and wordList[2] == "g" and wordList[3] == "g" and wordList[4] == "o"

	word = convertListToWord(wordList)
	if verbose:
		print("---And converting it back into a word:---")
		print(word)
	else:
		pasing_tests = pasing_tests and word == "doggo"

	if verbose:
		print("---Printing the rest of the file word by word:---")
		while not file.end_of_file:
			nextWord = file.getNextWord()
			print(nextWord)
	else:
		l = []
		while not file.end_of_file:
			nextWord = file.getNextWord()
			l.append(nextWord)
		pasing_tests = pasing_tests and len(l) == 14 and l[0] == "I" and l[1] == "am" and l[2] == "the" and l[3] == "super" and l[4] == "cat" and l[5] == "The" and l[6] == "dogs" and l[7] == "won" and l[8] == "I" and l[9] == "won" and l[10] == "People" and l[11] == "won't" and l[12] == "win" and l[13] == ""

	file.closeFile()

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")

def test_if_filewriter_works(verbose = True):
	print ("------------------test_if_filewriter_works------------------")
	if verbose:
		print("Writing to the file 'outputText.txt'.")
	file = fileWriter("outputText.txt")

	file.writeLineToFile("Psst...")

	arr = ["Dogs","are","better","than","humans."]
	file.writeLinesToFile(arr)

	file.closeFile()

	if not verbose:
		pasing_tests = True
		file2 = fileReader("outputText.txt")
		l = []
		while not file2.end_of_file:
			nextWord = file2.getNextWord()
			l.append(nextWord)
		pasing_tests = pasing_tests and len(l) == 7 and l[0] == "Psst" and l[1] == "Dogs" and l[2] == "are" and l[3] == "better" and l[4] == "than" and l[5] == "humans" and l[6] == ""
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
			testEnvironment.temporalState = ["d","o","g"]
			word_that_should_be_active = "dog"
			node_that_should_be_active = t_seq_dog
		elif r == 1:
			testEnvironment.temporalState = ["c","a","t"]
			word_that_should_be_active = "cat"
			node_that_should_be_active = t_seq_cat
		elif r == 2:
			testEnvironment.temporalState = ["d","o","g","g","o"]
			word_that_should_be_active = "doggo"
			node_that_should_be_active = t_seq_doggo
		else: 
			testEnvironment.temporalState = ["d","o","g","o"]
			word_that_should_be_active = "dogo (that is not recognised)"
			node_that_should_be_active = None

		nbrTicks = len(testEnvironment.temporalState)

		for i in range(nbrTicks):
			#print(testEnvironment.temporalState[i])
			for n in all_nodes:
				n.tick(1,i+1,True)

		if verbose:
			print("The '" + word_that_should_be_active + "' should be active....")
			if(t_seq_dog.isActive()):
				print("THE DOG IS ACTIVE!!!!!!!!!!!!! OMG OMG")
			elif(t_seq_cat.isActive()):
				print("THE CAT IS ACTIVE!!!!!!!!!!!!! OMG OMG")
			elif(t_seq_doggo.isActive()):
				print("THE DOGGO IS ACTIVE!!!!!!!!!!!!! OMG OMG")
		else:
			if(not node_that_should_be_active == None):
				pasing_tests = pasing_tests and node_that_should_be_active.isActive()
			else:
				pasing_tests = pasing_tests and (not t_seq_dog.isActive()) and (not t_seq_cat.isActive()) and (not t_seq_doggo.isActive())

	if not verbose:
		if pasing_tests:
			print("All tests pased.")
		else:
			print("Tests failed")


	#print(t_seq_cat.name)
	#print(t_seq_cat.getWord())
	#print(t_seq_dog.getWord())

def test_if_controller_works():
	print("------------------test_if_controller_works------------------")
	test_environment = Environment()
	test_controller = Controller(test_environment, "inputText", "outputText") 
	test_controller.run()



def run_tests(verbose = False):
	print ("------------------------------------Starting Tests------------------------------------")
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

