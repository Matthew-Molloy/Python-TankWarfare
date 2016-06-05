#Assignment 3
#Sushil Louis Game Engine
#Author: Zeeshan Sajid
#For this project, I utilized ent.py, physics.py made by Sushil Louis

import SampleFramework as sf
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
from ent import Entity
from player import Player
from pickup import pickUp

changeInVelocity = 30
class TutorialFrameListener(sf.FrameListener):

	def __init__(self, renderWindow, camera, sceneManager, sceneNodeEntity, physicsEntity,pickEntity, pickScene, pScene, pEnt, oBox):
		
		#You have to call this for the constructor
			sf.FrameListener.__init__(self, renderWindow, camera)

			# Key and mouse state tracking.
			self.toggle = 0
			self.mouseDown = False

		#Instantiate a Node entity that will keep track of the position of the node and change according to the velocity of the physics after ever clock tick
			self.sceneNode = sceneNodeEntity
 
			# Populate the camera and scene manager containers.
			self.camNode = camera.parentSceneNode.parentSceneNode
			self.sceneManager = sceneManager
 
			# Set the rotation and movement speed.
			self.rotate = 2.13
			self.move = 250
	
		#Instantiate a physics entity variable which will control the pos and vel of the cube
			self.cubeEnt = physicsEntity
		
			#Pick entity
			self.pickEntity = pickEntity
			self.pickScene = pickScene

			#Player Ent
			self.pScene = pScene
			self.pEnt = pEnt

			#This will get the animation state of the player object
			self.animate = oBox.getAnimationState('Walk')

	
	def frameStarted(self, frameEvent):
			global changeInVelocity 
			changeInVelocity = 30

		#Send the clock tick to the tick entity in Sushil's program, to get the time and to update the program physics
			self.cubeEnt.tick(frameEvent.timeSinceLastFrame)
		#Upon doing so, update the position of the node as well, but after every tick
			self.sceneNode.position = self.cubeEnt.pos

			#Pickup check
			self.pickEntity.check(self.cubeEnt.pos)
			self.pickScene.position = self.pickEntity.pos

			#Player
			self.pEnt.move(frameEvent.timeSinceLastFrame)
			self.pScene.position = self.pEnt.pos

			#Player fall status
			self.pEnt.fall(self.pickScene.position)


			# If the render window has been closed, end the program.
			if(self.renderWindow.isClosed()):
					return False
 
			# Capture and update each input device.
			self.Keyboard.capture()
			self.Mouse.capture()
 
		   # Get the current mouse state.
			currMouse = self.Mouse.getMouseState()
 
			# Use the Left mouse button to turn Light1 on and off.
			if currMouse.buttonDown(OIS.MB_Left) and not self.mouseDown:
					light = self.sceneManager.getLight('Light1')
					light.visible = not light.visible
 
			# Update the mouseDown boolean.
			self.mouseDown = currMouse.buttonDown(OIS.MB_Left)
 
			# Update the toggle timer.
			if self.toggle >= 0:
					self.toggle -= frameEvent.timeSinceLastFrame
 
			# Swap the camera's viewpoint with the keys 1 or 2.
			if self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_1):
					# Update the toggle timer.
					self.toggle = 0.1
					# Attach the camera to PitchNode1.
					self.camera.parentSceneNode.detachObject(self.camera)
					self.camNode = self.sceneManager.getSceneNode("CamNode1")
					self.sceneManager.getSceneNode("PitchNode1").attachObject(self.camera)

			elif self.toggle < 0 and self.Keyboard.isKeyDown(OIS.KC_2):
					# Update the toggle timer.
					self.toggle = 0.1
					# Attach the camera to PitchNode2.
					self.camera.parentSceneNode.detachObject(self.camera)
					self.camNode = self.sceneManager.getSceneNode("CamNode2")
					self.sceneManager.getSceneNode("PitchNode2").attachObject(self.camera)
 
			# Move the camera using keyboard input.
			transVector = ogre.Vector3(0, 0, 0)

		# Move Forward.
			if self.Keyboard.isKeyDown(OIS.KC_W):
				transVector.z -= self.move
			# Move Backward.
			if self.Keyboard.isKeyDown(OIS.KC_S):
					transVector.z += self.move
			# Strafe Left.
			if self.Keyboard.isKeyDown(OIS.KC_A):
					transVector.x -= self.move
			# Strafe Right.
			if self.Keyboard.isKeyDown(OIS.KC_D):
				transVector.x += self.move
			# Move Up.
			if self.Keyboard.isKeyDown(OIS.KC_E):
					transVector.y += self.move
			# Move Down.
			if self.Keyboard.isKeyDown(OIS.KC_F):
					transVector.y -= self.move
 
			# Translate the camera based on time.
			self.camNode.translate(self.camNode.orientation
							  * transVector
							  * frameEvent.timeSinceLastFrame)

			# Rotate the camera when the Right mouse button is down.
			if currMouse.buttonDown(OIS.MB_Right):
				self.camNode.yaw(ogre.Degree(-self.rotate
							* currMouse.X.rel).valueRadians())
				self.camNode.getChild(0).pitch(ogre.Degree(-self.rotate
										  * currMouse.Y.rel).valueRadians())


		######### BOX MOVEMENTS
				
		#Subtracting the z axis so it moves into the screen
			if self.Keyboard.isKeyDown(OIS.KC_NUMPAD8):
				self.pEnt.vel.z = self.pEnt.vel.z - changeInVelocity


		#Adding so it moves towards the screen
			if self.Keyboard.isKeyDown(OIS.KC_NUMPAD2):
					self.pEnt.vel.z = self.pEnt.vel.z + changeInVelocity

		#This will move the y axist up
			if self.Keyboard.isKeyDown(OIS.KC_NUMPAD9):
					self.pEnt.vel.y = self.pEnt.vel.y +changeInVelocity

		#This will move it down
			if self.Keyboard.isKeyDown(OIS.KC_NUMPAD3):
					self.pEnt.vel.y =self.pEnt.vel.y - changeInVelocity

		#This will stop the vector in general
			#if self.Keyboard.isKeyDown(OIS.KC_SPACE):
			#		self.pEnt.vel = ogre.Vector3(0,0,0)

		#Move the x to the left
			if self.Keyboard.isKeyDown(OIS.KC_NUMPAD4):
					self.pEnt.vel.x = self.pEnt.vel.x  - changeInVelocity

		#Move to the right
			if self.Keyboard.isKeyDown(OIS.KC_NUMPAD6):
					self.pEnt.vel.x = self.pEnt.vel.x + changeInVelocity

			if self.Keyboard.isKeyDown(OIS.KC_SPACE):
					self.pEnt.jump()
		
		# If the escape key is pressed end the program.
			return not self.Keyboard.isKeyDown(OIS.KC_ESCAPE)

class TutorialApplication(sf.Application):
	def _createScene(self):
		#Create a scene and assign it ambient light
		sceneManager = self.sceneManager
		sceneManager.ambientLight = (1,1,1)

		#Create ground surface height
		surfaceHeight = -100
		
		#Setup ground plane and then create a mesh from it
		plane = ogre.Plane ((0, 1, 0), surfaceHeight)
		meshManager = ogre.MeshManager.getSingleton ()
		meshManager.createPlane ('Ground', 'General', plane,
									 10000, 10000, 20, 20, True, 1, 5, 5, (0, 0, 1))
		ent = sceneManager.createEntity('GroundEntity', 'Ground')
		sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
		ent.setMaterialName ('Splashspacehold')
		ent.castShadows = False
		self.sceneManager.setSkyDome (True, "Examples/CloudySky", 5, 8)

		#Create the enetiy physics for the box
		self.cubeEntity = Entity("Cube", mesh = "SpacesuitGlove.mesh")

		#Create the box entity for python ogre
		self.pyOgreBox = sceneManager.createEntity("My Cube", self.cubeEntity.mesh)

		#Create a scene and then attach it to the sceneManager
		self.cubeScene = sceneManager.getRootSceneNode().createChildSceneNode("My Cube")
		
		#Then attach it
		self.cubeScene.attachObject(self.pyOgreBox)





		#This will attach the picup object
		self.pickEntity = pickUp(1, ogre.Vector3(100,0,0))

		self.pBox = sceneManager.createEntity("My Pickup", self.pickEntity.mesh)
		self.pickScene = sceneManager.getRootSceneNode().createChildSceneNode("PickUp", self.pickEntity.pos)
		self.pickScene.scale(3,3,3)
		self.pickScene.attachObject(self.pBox)
		


		#This will test the player object
		self.pEnt = Player()
		self.oBox = sceneManager.createEntity("Player", self.pEnt.mesh)
		self.pScene = sceneManager.getRootSceneNode().createChildSceneNode("player", self.pEnt.pos)
		self.pScene.scale(5,5,5)
		self.pScene.attachObject(self.oBox)


		#Create a scene Node that will hold the camera
		#Also, the function that moves the camera up and down requires a parent, in which this will be the parent of the main camera
		parentNode = sceneManager.getRootSceneNode().createChildSceneNode('myCameraNode',  (0, 300, 400))
	
		#Create a child node from which it's relative to the maincamera
		camNode = parentNode.createChildSceneNode('MainCamera')
		camNode.attachObject(self.camera)

	def _createCamera(self):
		self.camera =  self.sceneManager.createCamera ('PlayerCam')
		self.camera.nearClipDistance = 5
		self.camera.position = (0, 0, 400)
	

	def _createFrameListener(self):

		#Create a object of the root framelistener, in which it will keep track of our camera, our render cube physics and our cube node as it moves out of the screen
		self.frameListener = TutorialFrameListener(self.renderWindow, self.camera, self.sceneManager, self.cubeScene, self.cubeEntity, self.pickEntity, self.pickScene,
self.pScene, self.pEnt, self.oBox
)

		#This is necessary since Ogre C++ will need this item and needs to hold a reference to it
		self.root.addFrameListener(self.frameListener)

	def _createViewports(self):
		viewport = self.renderWindow.addViewport (self.camera)
		viewport.backGroundColor = (0, 0, 0)
		self.camera.aspectRatio = float (viewport.actualWidth) / float (viewport.actualHeight)
 
 
if __name__ == '__main__':
	ta = TutorialApplication()
	ta.go()
