import ogre.renderer.OGRE as ogre

#This class does not need physics 
class pickUp:
	#This class will just have a position along with id
	def __init__(self, id, pos = ogre.Vector3(0,0,0), mesh = "Cube.mesh"):
		self.id = id
		self.pos = pos
		self.mesh = mesh
	
	#Naturally this will move the item itself down so it's invisible
	def  move(self, pos = ogre.Vector3(0,-10000,0)):
		self.pos = pos		

	def check(self, pos):#This class will detect if the player position matches with the pickup Item
		'''
		print pos.x
		print pos.y
		print pos.z

		print self.pos.x
		print self.pos.y
		print self.pos.z
		
		if(self.pos.x == pos.x and self.pos.y == pos.y and self.pos.z == pos.z):
			#Play sound and move the item out of scope
			print "w"
			self.move(ogre.Vector3(-100000,-10000,0))
		'''
		if((
(self.pos.x +20) > pos.x or (self.pos.x - 20) < pos.x) 
and 
((self.pos.y +20) > pos.y or (self.pos.y - 20) < pos.y)
 and 
(self.pos.z +20) > pos.z or (self.pos.z - 20) < pos.z):
			#Play sound and move the item out of scope
			print "w"
			self.move(ogre.Vector3(-100000,-10000,0))
		
	def tick(self, dt):

		pass

