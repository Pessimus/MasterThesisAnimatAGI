from node import *
from nodes import *
from temporalNodes import *

def test_if_nodes_update_when_they_should():
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

def testNodes():
	print "------------------------Starting Node Tests------------------------"
	test_if_nodes_update_when_they_should()
	test_if_nodes_update_to_the_value_they_should()


def init():
	testNodes()

if __name__ == "__main__":
	init()




