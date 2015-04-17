import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import platform

class InputMgr(ogre.FrameListener):

    def __init__(self, engine):
        ogre.FrameListener.__init__(self)
        self.gfx = engine.gfxMgr
        self.entMgr = engine.entityMgr
        self.engine = engine
        self.state = True

    def init(self):
	self.raySceneQuery = None
        self.keyboard = self.gfx.keyboard
        self.mouse = self.gfx.mouse
        self.gfx.root.addFrameListener(self)
        self.mouseDown = False
        self.camera = self.gfx.camera
        self.rotate = 0.13
        self.move = 250

        self.raySceneQuery =self.gfx.sceneManager.createRayQuery(ogre.Ray())
        pass

    def tick(self, dt):
        pass

    def stop(self):
        pass
    
    def frameStarted(self, frameEvent):
     
 	self.keyboard.capture()
	self.mouse.capture()
        # Get the current mouse state.
        currMouse = self.mouse.getMouseState()

	#set up camera position
	if currMouse.buttonDown(OIS.MB_Left):
	   currMouse = self.mouse.getMouseState()
	   width = self.camera.getViewport().getActualWidth()
	   height = self.camera.getViewport().getActualHeight()
	   srcx = float(float(currMouse.X.abs)/float(width))
	   srcy = float(float(currMouse.Y.abs)/float(height))
	   mouseRay = self.camera.getCameraToViewportRay(srcx,srcy)
	   self.raySceneQuery.setRay(mouseRay)
	   self.raySceneQuery.setSortByDistance(True)
	   result = self.raySceneQuery.execute()
	   currentItem = None
	   #empty selected entities
	   for item in result:
		if item.movable:
			if not(item.movable.getName() == "Camera") and not(item.movable.getName() == 'GroundEntity'):
				currentItem = item.movable
	   x = 0
	   currentEntity = None
	   if currentItem != None:
		while x < self.entMgr.nEnts:
			if (self.entMgr.ents[x].uiname + str(x)) == currentItem.getName():
				currentEntity = self.entMgr.ents[x]
				self.entMgr.currentSelectedEntIndex = x
			x+=1
		
		if self.keyboard.isKeyDown(OIS.KC_LSHIFT) or self.keyboard.isKeyDown(OIS.KC_RSHIFT):
			if self.entMgr.selectedEntIndecies.count(currentEntity) == 0:
				self.entMgr.selectedEntIndecies.append(currentEntity)
			self.entMgr.selectedEnt = currentEntity
			currentEntity.node.showBoundingBox(True)
		else:
			#emptylist
			while len(self.entMgr.selectedEntIndecies) > 0:
	          		a = self.entMgr.selectedEntIndecies.pop()
	          		a.node.showBoundingBox(False)
               		self.entMgr.selectedEntIndecies.append(currentEntity)
			self.entMgr.selectedEnt = currentEntity
			currentEntity.node.showBoundingBox(True)
	   else:
		while len(self.entMgr.selectedEntIndecies) > 0:
	          	a = self.entMgr.selectedEntIndecies.pop()
	          	a.node.showBoundingBox(False)
		self.entMgr.selectedEnt = self.entMgr.ents[self.entMgr.nEnts - 1]
		self.entMgr.currentSelectedEntIndex = self.entMgr.nEnts - 1
				
				
	  
        # Move the camera using keyboard input.
        transVector = ogre.Vector3(0, 0, 0)

        # Move Forward.
        if self.keyboard.isKeyDown(OIS.KC_W):
           transVector.z -= self.move
        # Move Backward.
        if self.keyboard.isKeyDown(OIS.KC_S):
            transVector.z += self.move
        # Strafe Left.
        if self.keyboard.isKeyDown(OIS.KC_A):
            transVector.x -= self.move
        # Strafe Right.
        if  self.keyboard.isKeyDown(OIS.KC_D):
           transVector.x += self.move
        # Move Up.        
        if self.keyboard.isKeyDown(OIS.KC_PGUP):
            transVector.y += self.move
        # Move Down.
        if self.keyboard.isKeyDown(OIS.KC_PGDOWN):
            transVector.y -= self.move

        # Translate the camera based on time.
        self.camera.setPosition(self.camera.getPosition()
                              + transVector
                              * frameEvent.timeSinceLastFrame)
	
 
        # Rotate the camera when the Right mouse button is down.
        if currMouse.buttonDown(OIS.MB_Right):
           self.camera.yaw(ogre.Degree(-self.rotate 
                            * currMouse.X.rel).valueRadians())
           self.camera.pitch(ogre.Degree(-self.rotate
                                          * currMouse.Y.rel).valueRadians())

        if self.keyboard.isKeyDown(OIS.KC_Q):
           self.camera.yaw(ogre.Degree(self.rotate).valueRadians())
        if self.keyboard.isKeyDown(OIS.KC_E):
           self.camera.yaw(ogre.Degree(-self.rotate).valueRadians())
        if self.keyboard.isKeyDown(OIS.KC_Z):
           self.camera.pitch(ogre.Degree(self.rotate).valueRadians())
        if self.keyboard.isKeyDown(OIS.KC_X):
           self.camera.pitch(ogre.Degree(-self.rotate).valueRadians())
 
        # If the escape key is pressed end the program.

        if self.keyboard.isKeyDown(OIS.KC_ESCAPE):
            self.engine.keepRunning = self.state = False

        return self.state
