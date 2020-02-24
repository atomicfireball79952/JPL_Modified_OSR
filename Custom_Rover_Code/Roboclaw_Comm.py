from roboclaw import Roboclaw
import math
import serial
from time import sleep


class comm:
	
	def __init__(self):
		self.rc = Roboclaw("/dev/ttyS0",115200)
		self.rc.Open()
		self.accel           = [0]    * 10
		self.qpps            = [None] * 10
		self.err             = [None] * 5
		self.address         = [128,129,130,131,132]
		
		'''
		version = 1
		for address in self.address:
			print("Attempting to talk to motor controller",address)
			version = version & self.rc.ReadVersion(0x80)
			print(version)
		if version != 0:
			print("[Motor__init__] Sucessfully connected to RoboClaw motor controllers")
		else:
			raise Exception("Unable to establish connection to Roboclaw motor controllers")
		'''
		
	def accellDriveMotors(self, speeds):
		
		
		for i in range(3):
			self.rc.SpeedAccelM1(self.address[i],7000,speeds[i*2]*32767/500)
			self.rc.SpeedAccelM2(self.address[i],7000,speeds[(i*2+1)]*32767/500)
		

	def getCornerEncoders(self):
		
		enc = []
		
		for i in range(4):
			index = int(math.ceil((i+1)/2.0)+2)
			if not(i%2):
				enc.append(self.rc.ReadEncM1(self.address[index])[1])
			else:
				enc.append(self.rc.ReadEncM2(self.address[index])[1])
						
		return enc
		
	def moveCorners(self, tick):
		
		enc = []
		
		speed, accel = 1000,2000
		
		for i in range(4):
			index = int(math.ceil((i+1)/2.0)+2)
			if not(i%2):
				enc.append(self.rc.ReadEncM1(self.address[index])[1])
			else:
				enc.append(self.rc.ReadEncM2(self.address[index])[1])
						
			if(abs(tick[i] - enc[i]) < 25):
				tick[i] = -1
			
			if(tick[i] != -1):
				if(i % 2): self.rc.SpeedAccelDeccelPositionM2(self.address[index],accel,speed,accel,tick[i],1)
				else:      self.rc.SpeedAccelDeccelPositionM1(self.address[index],accel,speed,accel,tick[i],1)
				
			else:
				if(i%2): self.rc.ForwardM2(self.address[index],0)
				else:    self.rc.ForwardM1(self.address[index],0)
