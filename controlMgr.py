import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import platform

class ControlMgr(ogre.FrameListener):

    def __init__(self, engine):
        ogre.FrameListener.__init__(self)
        self.engine = engine
        self.gfx = self.engine.gfxMgr
        self.entityMgr = self.engine.entityMgr
        pass

    def init(self):
        self.keyboard = self.gfx.keyboard
        self.mouse = self.gfx.mouse
        self.gfx.root.addFrameListener(self)
        self.mouseDown = False
 
        # Key and mouse state tracking.
        self.toggle = 0
        self.mouseDown = False
        # Set the rotation and movement speed.
        self.rotate = 0.13
        self.move = 250
        pass

    def tick(self, dt):
        pass

    def stop(self):
        pass

 
    def frameStarted(self, frameEvent):
 
        # Capture and update each input device.
        self.keyboard.capture()
        self.mouse.capture()
 
        # Get the current mouse state.
        currMouse = self.mouse.getMouseState()
 
        # Update the mouseDown boolean.            
        self.mouseDown = currMouse.buttonDown(OIS.MB_Left)
 
        # Update the toggle timer.
        if self.toggle >= 0:
            self.toggle -= frameEvent.timeSinceLastFrame
 
        # Handle only Tab selection
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB):
	    #Left or right shift adds next ent
	    if self.keyboard.isKeyDown(OIS.KC_LSHIFT) or self.keyboard.isKeyDown(OIS.KC_RSHIFT):
	       self.toggle = 0.2
	       ent = self.entityMgr.selectNextEnt()
	       #check if ent already in list
	       if self.entityMgr.selectedEntIndecies.count(ent) == 0:
	          self.entityMgr.selectedEntIndecies.append(ent)
	          ent.node.showBoundingBox(True)

	    else:
               # Update the toggle timer.
               self.toggle = 0.2
               ent = self.entityMgr.selectNextEnt()
	       while len(self.entityMgr.selectedEntIndecies) > 0:
	          a = self.entityMgr.selectedEntIndecies.pop()
	          a.node.showBoundingBox(False)
               self.entityMgr.selectedEntIndecies.append(ent)

               print "FrameListener: Selected: ", str(ent)
               ent.node.showBoundingBox(True)

#--------------------------------------------------------------------------------------
        
        #print str(self.selectedEntIndex), selectedEnt.id
        import utils

        # Speed Up
        if  self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_UP):
           self.toggle = 0.2
	   for selectedEnt in self.entityMgr.selectedEntIndecies:
              selectedEnt.desiredSpeed = utils.clamp(selectedEnt.desiredSpeed + selectedEnt.deltaSpeed, 0, selectedEnt.maxSpeed)
              print "Speeding UP", selectedEnt.desiredSpeed

        # Slow down
        if  self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_DOWN):
           self.toggle = 0.2
	   for selectedEnt in self.entityMgr.selectedEntIndecies:
              selectedEnt.desiredSpeed = utils.clamp(selectedEnt.desiredSpeed - selectedEnt.deltaSpeed, 0, selectedEnt.maxSpeed)
              print "Slowing down", selectedEnt.desiredSpeed


        # Turn Left.
        if  self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_LEFT):
           self.toggle = 0.2
	   for selectedEnt in self.entityMgr.selectedEntIndecies:
              selectedEnt.desiredHeading += selectedEnt.deltaYaw
              selectedEnt.desiredHeading = utils.fixAngle(selectedEnt.desiredHeading)
              print "Turn left", selectedEnt.desiredHeading

            
        # Turn Right.
        if  self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_RIGHT):
           self.toggle = 0.2
	   for selectedEnt in self.entityMgr.selectedEntIndecies:
              selectedEnt.desiredHeading -= selectedEnt.deltaYaw
              selectedEnt.desiredHeading = utils.fixAngle(selectedEnt.desiredHeading)
              print "Turn right", selectedEnt.desiredHeading

        #print self.selectedEnt.uiname, selectedEnt.id, str(selectedEnt.vel)

 #-------------------------------------------------------------------------------------
 
        return True

    def frameEnded(self, evt):
        pass
        return True;

    def frameRenderingQueued(self, evt):
        pass
        return True;


