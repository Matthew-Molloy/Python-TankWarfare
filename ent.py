# Entity class to hold information about entities for 38Engine
# Sushil Louis

from vector import MyVector
from physics import Physics
from render  import Renderable
import ogre.renderer.OGRE as ogre
class Entity:


    aspectTypes = [Physics, Renderable]
    
    def __init__(self, id, engine, pos = MyVector(0,0,0), mesh = 'robot.mesh', vel = MyVector(0, 0, 0), yaw = 0):
        self.id = id
        self.yawOffset = 0
        self.collision = False
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.node = None
        self.deltaSpeed = 1
        self.deltaYaw   = .5
        self.speed = 0.0
        self.heading = 0.0
        self.aspects = []
        self.initAspects()
        self.engine = engine
        

    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self))
        

    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)
        self.checkCollision(dtime)


    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s,  mesh = %s\nSpeed: %f, Heading: %f" % (self.id, str(self.pos), str(self.vel), self.mesh, self.speed, self.heading)
        return x


class CVN68(Entity):
    def __init__(self, id, engine, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, engine = engine, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'tank.mesh'
        self.uiname = 'CVN68'
        self.eid = id
        self.yawOffset = 90
        self.acceleration = 2
        self.turningRate  = 0.2
        self.maxSpeed = 20
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.engine = engine
        self.checkValue = 240

    def checkCollision(self, dtime):
        # checkValue indicates the distance from the target ent to the collision spot of the current ent
        for key, target in self.engine.entityMgr.ents.items():
            if target.uiname == 'DDG51':
                diffZ = target.pos.z - self.pos.z
                diffX = target.pos.x - self.pos.x
                self.distance = ogre.Math.Sqrt(ogre.Math.Sqr(diffZ) + ogre.Math.Sqr(diffX))
                #print self.distance.valueDegrees()
                if self.distance.valueDegrees() < target.checkValue:
                    print "Collision"
                    self.collision = True
                    self.speed = 0
                    self.desiredSpeed = 0



class DDG51(Entity):
    def __init__(self, id, engine, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, engine = engine, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'tank.mesh'
        self.uiname = 'DDG51'
        self.eid = id
        self.acceleration = 5
        self.turningRate = 0.2
        self.maxSpeed = 32
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.engine = engine
        self.checkValue = 150

    def checkCollision(self, dtime):
        # checkValue indicates the distance from the target ent to the collision spot of the current ent
        for key, target in self.engine.entityMgr.ents.items():
            if target.uiname == 'CVN68':
                diffZ = target.pos.z - self.pos.z
                diffX = target.pos.x - self.pos.x
                self.distance = ogre.Math.Sqrt(ogre.Math.Sqr(diffZ) + ogre.Math.Sqr(diffX))
                #print self.distance.valueDegrees()
                if self.distance.valueDegrees() < target.checkValue:
                    print "Collision"
                    self.collision = True
                    self.speed = 0
                    self.desiredSpeed = 0

