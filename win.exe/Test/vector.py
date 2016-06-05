import math #Import math for square root function

#Vectory class
class MyVector:
	#Pre-instanted variables for all objects of that class
	x = 0
	y = 0
	z = 0
		
	#Constructor
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	#Add, sub, div, mult functions
	def add(self, vector2):
		self.x = self.x + vector2.x
		self.y = self.y + vector2.y
		self.z = self.z + vector2.z
		return self
	
	def sub(self, vector2):
		self.x = self.x - vector2.x
		self.y = self.y - vector2.y
		self.z = self.z - vector2.z
		return self

	def div(self, scale_num):
		self.x = self.x/scale_num
		self.y = self.y/scale_num
		self.z = self.z/scale_num
		return self

	def multiply(self, scale_num):
		self.x = self.x * scale_num
		self.y = self.y * scale_num
		self.z = self.z * scale_num
		return self

	#The length function which calculates the magnitude after squaring and square rooting it
	def length(self):
		squared = ((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
		magnitude = math.sqrt(squared)
		return magnitude
		
##########################################################################################
#OP OVERLOADERS
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		print "Calling op Add"
		return MyVector(x,y,z)

	def __sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		z = self.z - other.z
		print "Calling op sub"
		return MyVector(x,y,z)

	def __mul__ (self, other):
		x = self.x * other
		y = self.y * other
		z = self.z * other
		print "Calling op mult"
		return MyVector(x,y,z)

	def __div__ (self, other):
		x = self.x / other
		y = self.y / other
		z = self.z / other
		print "Calling op div"
		return MyVector(x,y,z)

####################################################################
	# Call __str__ function to print out a string for the class, and use subclass float to solve the point precision issue
	def __str__(self):
		string = "(%0.2f, " % self.x + "%0.2f, " % self.y + "%0.2f)" % self.z
		return string 
