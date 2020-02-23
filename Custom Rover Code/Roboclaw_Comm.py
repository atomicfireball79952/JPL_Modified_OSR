from roboclaw import Roboclaw
import math
import serial


class comm:
	
	def __init__(self):
		self.rc = Roboclaw("/dev/ttyS0",115200)
		self.rc.Open()
		self.accel           = [0]    * 10
		self.qpps            = [None] * 10
		self.err             = [None] * 5
		self.address         = [128,129,130,131,132]
		
		
		version = 1
		for address in self.address:
			print("Attempting to talk to motor controller",address)
			version = version & self.rc.ReadVersion(address)
			print(version)
		if version != 0:
			print("[Motor__init__] Sucessfully connected to RoboClaw motor controllers")
		else:
			raise Exception("Unable to establish connection to Roboclaw motor controllers")
		
		
	def accellDriveMotors(self):
		
		
		for i in range(3):
			self.rc.SpeedAccelM1(self.address[i],12000,12000)
			self.rc.SpeedAccelM2(self.address[i],12000,12000)
