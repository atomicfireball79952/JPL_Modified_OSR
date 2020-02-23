import math

turnBuffer = 1

class calculate:

	def __init__(self, distances):#Initializes distance values
		self.d1 = distances[0]
		self.d2 = distances[1]
		self.d3 = distances[2]
		self.d4 = distances[3]
		
		
	def calculateTurningAngles(self, turnValue):
		minRadius = self.d1 + self.d3 + turnBuffer#Calculates smallest possible radius
		
		self.radius = 0 #Initializes radius
		if(turnValue != 0): self.radius = abs(minRadius/turnValue) #Sets radius proportional to joystick
		
		if self.radius == 0: return [0]*4 #If rover isn't turning

		#Calculates angles
		ang1 = int(10*math.degrees(math.atan(self.d3/(abs(self.radius)+self.d1))))/10
		ang2 = int(10*math.degrees(math.atan(self.d2/(abs(self.radius)+self.d1))))/10
		ang3 = int(10*math.degrees(math.atan(self.d2/(abs(self.radius)-self.d1))))/10
		ang4 = int(10*math.degrees(math.atan(self.d3/(abs(self.radius)-self.d1))))/10
		
		#Makes angles depentant on which direction the rover is turning
		if self.radius > 0:
			return [ang2,-ang1,-ang4,ang3]
		else:
			return [-ang4,ang3,ang2,-ang1]
		     
		
	def calculateMotorSpeeds(self, speed):
	
		speed *= 1000 #Sets speed from -1 1 to -1000 1000
	
		if(self.radius != 0):
		
			rmax = self.radius + self.d4 #Sets radius of outside wheels
	
			#Returns angles of -45.0 to 45.0
			a = math.pow(self.d2,2)
			b = math.pow(self.d3,2)
			c = math.pow(abs(self.radius) + self.d1,2)
			d = math.pow(abs(self.radius) - self.d1,2)
			e = abs(self.radius) - self.d4
			
			rmax_float = float(rmax) #Makes it a float, I guess
			
			#Returns speed of -100.0 to 100.0
			v1 = int(speed*(math.sqrt(b + d))/rmax_float)/10
			v2 = int((speed*e/rmax_float))/10                        # Slowest wheel
			v3 = int((speed*math.sqrt(a + d))/rmax_float)/10
			v4 = int((speed*math.sqrt(a + c))/rmax_float)/10
			v5 = int(speed)/10                            # Fastest wheel
			v6 = int((speed*math.sqrt(b + c))/rmax_float)/10

			#Makes speeds depentant on which direction the rover is turning
			if (self.radius < 0):
				velocity = [v1,v2,v3,v4,v5,v6]
			elif (self.radius > 0):
				velocity = [v6,v5,v4,v3,v2,v1]

		else: velocity = [int(speed)]*6 #If the rover isn't turning

		return velocity #When the rover is turning
			
			
			
