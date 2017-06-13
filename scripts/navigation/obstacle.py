from ctypes import *

class Obstacle(Structure):
	_fields_ =	[ ("x",		c_float), 
			  ("y",		c_float),
			  ("x2",	c_float),
			  ("y2",	c_float), 
			  ("radius",	c_float) ]

class ListObstacle(Structure):
	_fields_ = [ ("List", Obstacle * 13),
				("size", c_int) ]

class OrientedPoint(Structure):
	_fields_ = [ ("x", c_float),
				("y", c_float),
				("theta", c_float) ]

class ListOrientedPoint(Structure):
	_fields_ = [ ("List", OrientedPoint * 50),
				("size", c_int) ]
