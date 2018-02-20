from node import *
from nodes import *
from temporalNodes import *
from environment import *
from actionNodes import *
from temporalActionNodes import *
import random



def test_if_nodes_update_when_they_should():

	print ("------------------test_if_nodes_update_when_they_should------------------")

	print("----------------Testing if nodes update----------------")
	seqNodeTestNode = SEQNode()
	v = seqNodeTestNode.tick(1)
	print("\t should be True,\n\t -------is %s" % (v))
	v = seqNodeTestNode.tick(1)
	print("\t should be False,\n\t -------is %s" % (v))
	v = seqNodeTestNode.tick(2,1)
	print("\t should be True,\n\t -------is %s" % (v))
	v = seqNodeTestNode.tick(2,2)
	print("\t should be False,\n\t -------is %s" % (v))
	v = seqNodeTestNode.tick(3,1,True)
	print("\t should be False,\n\t -------is %s" % (v))

	temporalSeqNodeTestNode = TemporalSEQNode()
	v = temporalSeqNodeTestNode.tick(1)
	print("\t should be False,\n\t -------is %s" % (v))
	v = temporalSeqNodeTestNode.tick(1)
	print("\t should be False,\n\t -------is %s" % (v))
	v = temporalSeqNodeTestNode.tick(2,1,True)
	print("\t should be True,\n\t -------is %s" % (v))
	v = temporalSeqNodeTestNode.tick(2,2,True)
	print("\t should be True,\n\t -------is %s" % (v))
	v = temporalSeqNodeTestNode.tick(2,2,True)
	print("\t should be False,\n\t -------is %s" % (v))

def test_if_nodes_update_to_the_value_they_should():

	print ("------------------test_if_nodes_update_to_the_value_they_should------------------")

	print("----------------Testing values of updated nodes----------------")
	dummy1 = Node()
	dummy2 = Node()

	print("--------Testing SEQ Node--------")
	seqNodeTestNode = SEQNode()
	inputList = [dummy1,dummy2] 
	seqNodeTestNode.inputs = inputList
	i = 1
	v = seqNodeTestNode.tick(i)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	dummy1.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	dummy1.active = False
	dummy2.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	dummy1.active = True
	dummy2.active = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (seqNodeTestNode.isActive()))
	dummy1.previousActive = True
	v = seqNodeTestNode.tick(i)
	i = i +1;
	print("\t should be True,\n\t -------is %s" % (seqNodeTestNode.isActive()))

	print("--------Testing Temporal SEQ Node--------")
	dummy1 = Node()
	dummy2 = Node()
	temporalSeqNodeTestNode = TemporalSEQNode()
	inputList = [dummy1,dummy2] 
	temporalSeqNodeTestNode.inputs = inputList
	i = 1

	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	dummy1.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	dummy1.active = False
	dummy2.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	dummy1.active = True
	dummy2.active = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	dummy1.previousActive = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	print("\t should be False,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))
	dummy1.previousTemporalActive = True
	v = temporalSeqNodeTestNode.tick(1,i,True)
	i = i +1;
	print("\t should be True,\n\t -------is %s" % (temporalSeqNodeTestNode.isActive()))

def test_if_sensors_react_to_input():

	print ("------------------test_if_sensors_react_to_input------------------")

	print("----------------Testing sensors----------------")
	testEnvironment = Environment()
	testSensor = SensorNode(name = "d-sensor",sensor = "d", environment =  testEnvironment)
	i = 1
	testSensor.tick(i)
	print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))

	testSensor.tick(i, 1, True)
	print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))

	testEnvironment.state = {"d", "o", "g"}
	i=i+1
	testSensor.tick(i)
	print("\t should be True,\n\t -------is %s" % (testSensor.isActive()))

	testEnvironment.state = {"g", "o", "g"}
	i=i+1
	testSensor.tick(i)
	print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))

	testEnvironment.temporalState = ["d", "o", "g"]
	i=i+1
	testSensor.tick(i, 1, True)
	print("\t should be True,\n\t -------is %s" % (testSensor.isActive()))

	testSensor.tick(i, 2, True)
	print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))

	testEnvironment.state = {"d", "o", "g"}
	testSensor.tick(i, 3, True)
	print("\t should be False,\n\t -------is %s" % (testSensor.isActive()))

def test_if_dog_can_be_found():

	print ("------------------test_if_dog_can_be_found------------------")

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

	if random.randint(0, 1) == 1:
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

	if(t_seq_dog.isActive()):
		print("THE DOG IS ACTIVE!!!!!!!!!!!!! OMG OMG")

	if(t_seq_cat.isActive()):
		print("THE CAT IS ACTIVE!!!!!!!!!!!!! OMG OMG")

	print(t_seq_cat.name)
	print(t_seq_cat.getWord())
	print(t_seq_dog.getWord())

def test_if_motors_produce_things():

	print ("------------------test_if_motors_produce_things------------------")

	testEnvironment = Environment()

	motor_node_d = MotorNode(name = "d-motor",motor = "d", environment =  testEnvironment)
	motor_node_o = MotorNode(name = "o-motor",motor = "o", environment =  testEnvironment)
	motor_node_g = MotorNode(name = "g-motor",motor = "g", environment =  testEnvironment)
	
	motor_node_d.activate(1)
	print("Testing the motor node 'd'. Environment (first print) should contain 'd'. And contains:")
	print(testEnvironment.nextState)
	print(testEnvironment.nextTemporalState)

	testEnvironment.nextState = set()
	motor_node_d.activate(2)
	motor_node_o.activate(2)
	print("Testing the motor node 'd' & 'o'. Environment (first print) should contain 'd' & 'o'. And contains:")
	print(testEnvironment.nextState)
	print(testEnvironment.nextTemporalState)

	testEnvironment.nextState = set()
	motor_node_d.activate(2,True)
	motor_node_o.activate(2,True)
	print("Testing the motor node 'd' & 'o'. Environment (second print) should contain 'd' & 'o'. And contains:")
	print(testEnvironment.nextState)
	print(testEnvironment.nextTemporalState)

	testEnvironment.nextTemporalState = []
	motor_node_d.active = False
	motor_node_o.active = False
	testAction_do = ActionAndNode(outputs=[motor_node_d,motor_node_o])
	testAction_do.activate(3)
	print("Testing the motor node 'd&o'. Environment (first print) should contain 'd' & 'o'. And contains:")
	print(testEnvironment.nextState)
	print(testEnvironment.nextTemporalState)

	testEnvironment.nextTemporalState = []
	testEnvironment.state = set()
	motor_node_d.active = False
	motor_node_o.active = False

	testTemporalAction_do = TemporalASEQNode(outputs=[motor_node_d,motor_node_o])
	testTemporalAction_do.activate(4, True)
	print("Testing the motor node 'do'. Environment (second print) should contain 'd' & 'o'. And contains:")
	print(testEnvironment.state)
	print(testEnvironment.nextTemporalState)

	testEnvironment.nextTemporalState = []
	testEnvironment.state = set()
	motor_node_d.active = False
	motor_node_o.active = False
	testTemporalAction_do.active = False

	testTemporalAction_dog = TemporalASEQNode(outputs=[testTemporalAction_do,motor_node_g])
	testTemporalAction_dog.activate(5, True)
	print("Testing the motor node 'dog'. Environment (second print) should contain 'd' & 'o' & 'g'. And contains:")
	print(testEnvironment.state)
	print(testEnvironment.nextTemporalState)
	
def test_if_animat_can_hear_it_self():
	print ("------------------test_if_animat_can_hear_it_self------------------")
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

	print("Animat says 'dog', thus environment should have 'dog'.")
	print(testEnvironment.nextTemporalState)

	print("---Updating Environment---")
	testEnvironment.state = testEnvironment.state
	testEnvironment.temporalState = testEnvironment.nextTemporalState
	testEnvironment.state.add(testEnvironment.nextTemporalState[len(testEnvironment.nextTemporalState)-1])
	testEnvironment.nextState = set()
	testEnvironment.nextTemporalState = [];
	#Possibly add more input if wanted. 
	
	print("environment should now have [dog] and {g}")
	print(testEnvironment.temporalState)
	print(testEnvironment.state)

	for n in all_sensor_nodes:
		n.tick(1,1,True)
	for n in all_sensor_nodes:
		n.tick(1,2,True)
	for n in all_sensor_nodes:
		n.tick(1,3,True)

	print("Animat has processed input, should now have heard 'dog'.")
	if(t_seq_dog.isActive()):
		print("THE DOG IS ACTIVE!!!!!!!!!!!!! OMG OMG")
	else:
		print("Where is the dog? :'(")



def run_tests():
	print ("------------------------------------Starting Tests------------------------------------")
	test_if_nodes_update_when_they_should()
	test_if_nodes_update_to_the_value_they_should()
	test_if_sensors_react_to_input()
	test_if_dog_can_be_found()
	test_if_motors_produce_things()
	test_if_animat_can_hear_it_self()