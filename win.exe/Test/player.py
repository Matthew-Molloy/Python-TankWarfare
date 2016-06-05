import ogre.renderer.OGRE as ogre

class Player:
	pos = ogre.Vector3(0,0,0)
	vel = ogre.Vector3(0,0,0)
	high = 90
	low = 0
	size = 50
	gravity = 0
	mesh = "robot.mesh"
	def __init__(self, pos = ogre.Vector3(100,0,0), vel = ogre.Vector3(0,0,0), mesh = "robot.mesh"):
		self.pos = pos
		self.vel = vel
	
	def move(self, dtime):
		self.pos = self.pos + (self.vel * dtime)

		#if(self.jump()):
		#	self.pos = self.pos+  ogre.Vector3(0,50,0)
		print self.pos

	#The jump mechanic for the player
	def jump(self):
			while(self.pos.y < self.pos.y+self.high):		
				self.pos = self.pos+  ogre.Vector3(0,50,0)
			return True
	#This function checks for collision below, mostly for platforms
	def collisionBelow(self, pos, size):
		if(pos.y < self.pos.y or pos.y == self.pos.y ): #This will check if there's a platform underneath the y axis of the current player
			#If there is an existing platform then set the position of the y axis to that	
			changeInPos = pos.y - self.pos.y
			if(changeInPos < 0):
				changeInPos = -1 * changeInPos
			if(changeInPos < 50):
				self.pos.y = pos.y
				return True

		#This section will be there for detecting the platform on z and x axis

	#This will be the 
	def fall(self, pos):
		if(self.collisionBelow( pos,0)): #This will check if there's collision first
			#If there is collision change the gravity to complete 0
			gravity = 0
			print "certainly"

		else:
			gravity = 0.981
			self.vel.y -= gravity
			
		pass 
