import pygame

class Joy:

	

	def __init__(self):#Initializes joystick
		pygame.init()
		pygame.joystick.init()
		joystick = pygame.joystick.Joystick(0)
		joystick.init()
	
	def getLeftJoy(self):
		joystick = pygame.joystick.Joystick(0)#Initializes remote in frame
		
		for event in pygame.event.get():#Checks all the buttons
			lX =  joystick.get_axis(0)
			lY = -joystick.get_axis(1)
			#Sets threshold
			if(-0.08 < lX < 0.08): lX = 0
			if(-0.08 < lY < 0.08): lY = 0
			if(0.9999 < lX):       lX = 1
			if(0.9999 < lY):       lY = 1
			if(lX < -0.9999):      lX = -1
			if(lY < -0.9999):      lY = -1
			
			return (lX, lY)
	
	def getRightJoy(self):
		joystick = pygame.joystick.Joystick(0)#Initializes remote in frame
		
		for event in pygame.event.get():#Checks all the buttons
			rX =  joystick.get_axis(3)
			rY = -joystick.get_axis(4)
			#Sets threshold
			if(-0.08 < rX < 0.08): rX = 0
			if(-0.08 < rY < 0.08): rY = 0
			if(0.9999 < rX):       rX = 1
			if(0.9999 < rY):       rY = 1
			if(rX < -0.9999):      rX = -1
			if(rY < -0.9999):      rY = -1
			
			return (rX, rY)
			
	def getArrows(self):
		joystick = pygame.joystick.Joystick(0)#Initializes remote in frame
		
		for event in pygame.event.get():#Checks all the buttons
			return joystick.get_hat(0)
			
	
	
