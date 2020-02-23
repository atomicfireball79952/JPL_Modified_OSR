from Joystick   import Joy
from Dimensions import dimensions
from Calculations import calculate
from Roboclaw_Comm import comm


#Initializes variables
joystick = Joy()
#communication = comm()

leftJoy  = (0,0)
rightJoy = (0,0)
arrows   = (0,0)

distances = dimensions.getDistances()

calculations = calculate(distances)

while(True):
	
	#Gets remote data
	leftJoyNew  = joystick.getLeftJoy()
	rightJoyNew = joystick.getRightJoy()
	arrowsNew   = joystick.getArrows()
	
	
	#If data is read, sets variables
	if(leftJoyNew  != None): leftJoy  = leftJoyNew
	if(rightJoyNew != None): rightJoy = rightJoyNew
	if(arrowsNew   != None): arrows   = arrowsNew
	
	
	#Calculate values for turning and driving
	angles = calculations.calculateTurningAngles(leftJoy[0])
	speeds = calculations.calculateMotorSpeeds(leftJoy[1])
	
	
	#Communicate with motor controllers
#	communication.accellDriveMotors()
	
	
	#Debugging code. Un-comment to use
	#print(leftJoy," || ",rightJoy," || ",arrows)
	print(speeds," || ",angles)
	
	
