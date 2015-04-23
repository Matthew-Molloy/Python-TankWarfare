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
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.node = None
        self.deltaSpeed = 5
        self.deltaYaw   = 0.8
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


    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s,  mesh = %s\nSpeed: %f, Heading: %f" % (self.id, str(self.pos), str(self.vel), self.mesh, self.speed, self.heading)
        return x


class CVN68(Entity):
    def __init__(self, id, engine, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, engine = engine, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'cvn68.mesh'
        self.uiname = 'CVN68'
        self.eid = id
        self.acceleration = 2
        self.turningRate  = 0.2
        self.maxSpeed = 20
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.engine = engine
        self.checkValue = 240

    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)
        self.checkCollision(dtime)

    def checkCollision(self, dtime):
        # checkValue indicates the distance from the target ent to the collision spot of the current ent
        for key, target in self.engine.entityMgr.ents.items():
            if target.uiname == 'DDG51':
                diffZ = target.pos.z - self.pos.z
                diffX = target.pos.x - self.pos.x
                self.distance = ogre.Math.Sqrt(ogre.Math.Sqr(diffZ) + ogre.Math.Sqr(diffX))
                print self.distance.valueDegrees()
                if self.distance.valueDegrees() < target.checkValue:
                    print "Collision"
                    self.speed = 0
                    self.desiredSpeed = 0
                    self.pos.z -= 2
                    self.pos.x -= 2


class CIGARETTE(Entity):
    def __init__(self, id, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'cigarette.mesh'
        self.uiname = 'CIGARETTE'
        self.eid = id
        self.acceleration  = 6
        self.turningRate   = 0.1
        self.maxSpeed = 40
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class MONTEREY(Entity):
    def __init__(self, id, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'Monterey.mesh'
        self.uiname = 'MONTEREY'
        self.eid = id
        self.acceleration = 5
        self.turningRate = 0.1
        self.maxSpeed = 35
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class JETSKI(Entity):
    def __init__(self, id, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'Watercr.mesh'
        self.uiname = 'JETSKI'
        self.eid = id
        self.acceleration = 7
        self.turningRate = 0.15
        self.maxSpeed = 20
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class SAILBOAT(Entity):
    def __init__(self, id, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'sailboat.mesh'
        self.uiname = 'SAILBOAT'
        self.eid = id
        self.acceleration = 3
        self.turningRate = 0.1
        self.maxSpeed = 10
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class SLEEK(Entity):
    def __init__(self, id, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'sleek.mesh'
        self.uiname = 'SLEEK'
        self.eid = id
        self.acceleration = 4
        self.turningRate = 0.02
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class BOAT(Entity):
    def __init__(self, id, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'boat.mesh'
        self.uiname = 'BOAT'
        self.eid = id
        self.acceleration = 5
        self.turningRate = 0.1
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class DDG51(Entity):
    def __init__(self, id, engine, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, engine = engine, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'ddg51.mesh'
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

    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)
        self.checkCollision(dtime)

    def checkCollision(self, dtime):
        # checkValue indicates the distance from the target ent to the collision spot of the current ent
        for key, target in self.engine.entityMgr.ents.items():
            if target.uiname == 'CVN68':
                diffZ = target.pos.z - self.pos.z
                diffX = target.pos.x - self.pos.x
                self.distance = ogre.Math.Sqrt(ogre.Math.Sqr(diffZ) + ogre.Math.Sqr(diffX))
                print self.distance.valueDegrees()
                if self.distance.valueDegrees() < target.checkValue:
                    print "Collision"
                    self.speed = 0
                    self.desiredSpeed = 0
                    self.pos.z -= 2
                    self.pos.x -= 2

class ALIENSHIP(Entity):
    def __init__(self, id, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'alienship.mesh'
        self.uiname = 'ALIEN'
        self.eid = id
        self.acceleration  = 10
        self.turningRate   = 0.3
        self.maxSpeed = 60
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

class BOAT2(Entity):
    def __init__(self, id, pos = MyVector(0,0,0), vel = MyVector(0, 0, 0), yaw = 0):
        Entity.__init__(self, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = '5086_Boat.mesh'
        self.uiname = 'BOAT2'
        self.eid = id
        self.acceleration = 5
        self.turningRate = 0.025
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0

