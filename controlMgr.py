from contextlib import contextmanager
import pygame
import sys
import os

import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS

from xBox import JoyAxes
from xBox import JoyButtons


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


class ControlMgr(ogre.FrameListener):
    def __init__(self, engine):
        ogre.FrameListener.__init__(self)
        self.engine = engine
        self.gfx = self.engine.gfxMgr
        self.sound = self.engine.soundMgr
        self.widget = self.engine.widgetMgr
        self.entityMgr = self.engine.entityMgr
        self.tank = None
        self.tank1 = None
        pass

    def init(self):

        self.joyStick1 = None
        self.joyStick2 = None
        self.keyboard = self.gfx.keyboard
        self.mouse = self.gfx.mouse
        self.gfx.root.addFrameListener(self)
        self.mouseDown = False

        # Key and mouse state tracking.
        self.toggle = 0
        self.toggle1 = 0
        self.mouseDown = False
        # Set the rotation and movement speed.
        self.rotate = 0.13
        self.move = 250

        self.tank = self.entityMgr.ents[0]
        self.tank1 = self.entityMgr.ents[1]
        self.tank1.node.attachObject(self.gfx.camera1)
        self.tank.node.attachObject(self.gfx.camera)

        pygame.init()
        pygame.joystick.init()

        self.joyNum = pygame.joystick.get_count()
        if self.joyNum == 1:
            self.joyStick1 = pygame.joystick.Joystick(0)
            self.joyStick1.init()

        if self.joyNum == 2:
            self.joyStick1 = pygame.joystick.Joystick(0)
            self.joyStick1.init()
            self.joyStick2 = pygame.joystick.Joystick(1)
            self.joyStick2.init()

        pass

    def initTanks(self):
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

        if self.toggle1 >= 0:
            self.toggle1 -= frameEvent.timeSinceLastFrame


        # Handle only Tab selection
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB):
            # Left or right shift adds next ent
            if self.keyboard.isKeyDown(OIS.KC_LSHIFT) or self.keyboard.isKeyDown(OIS.KC_RSHIFT):
                self.toggle = 0.2
                ent = self.entityMgr.selectNextEnt()
                # check if ent already in list
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

                # --------------------------------------------------------------------------------------

        # Speed Up
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_UP):
            self.toggle = 0.2
            for selectedEnt in self.entityMgr.selectedEntIndecies:
                selectedEnt.desiredSpeed += selectedEnt.deltaSpeed
                selectedEnt.collision = False
                print "Speeding UP", selectedEnt.desiredSpeed

        # Slow down
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_DOWN):
            self.toggle = 0.2
            for selectedEnt in self.entityMgr.selectedEntIndecies:
                selectedEnt.desiredSpeed -= selectedEnt.deltaSpeed
                selectedEnt.collision = False
                print "Slowing down", selectedEnt.desiredSpeed


        # Turn Left.
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_LEFT):
            self.toggle = 0.2
            for selectedEnt in self.entityMgr.selectedEntIndecies:
                selectedEnt.desiredHeading += selectedEnt.deltaYaw
                print "Turn left", selectedEnt.desiredHeading


        # Turn Right.
        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_RIGHT):
            self.toggle = 0.2
            for selectedEnt in self.entityMgr.selectedEntIndecies:
                selectedEnt.desiredHeading -= selectedEnt.deltaYaw
                print "Turn right", selectedEnt.desiredHeading
                # -------------------------------------------------------------------------------------

        for event in pygame.event.get():
            if self.joyStick1:
                temp = self.joyStick1.get_axis(JoyAxes.LEFT_LEFTRIGHT)
                temp1 = self.joyStick1.get_axis(JoyAxes.LEFT_UPDOWN)
                self.tank.desiredSpeed = self.tank.deltaSpeed * -temp1
                self.tank.collision = False
                self.tank.desiredHeading -= self.tank.deltaYaw * temp
                if self.joyStick1.get_axis(JoyAxes.RT) > 0 and self.toggle < 0:
                    self.toggle = 2
                    self.sound.shoot1()
                    self.tank.shoot()

                if self.joyStick1.get_button(JoyButtons.START) and self.engine.overlayMgr.showMenu is True and self.toggle < 0:
                    self.toggle = 2
                    self.engine.inputMgr.startCheck = True
                    self.engine.gameMgr.loadLevel()

            if self.joyStick2:
                temp = self.joyStick2.get_axis(JoyAxes.LEFT_LEFTRIGHT)
                temp1 = self.joyStick2.get_axis(JoyAxes.LEFT_UPDOWN)
                self.tank1.desiredSpeed = self.tank1.deltaSpeed * -temp1
                self.tank1.collision = False
                self.tank1.desiredHeading -= self.tank1.deltaYaw * temp

                if self.joyStick2.get_axis(JoyAxes.RT) > 0 and self.toggle1 < 0:
                    self.toggle1 = 2
                    self.sound.shoot2()
                    self.tank1.shoot()

        return True

    def frameEnded(self, evt):
        pass
        return True

    def frameRenderingQueued(self, evt):
        pass
        return True

