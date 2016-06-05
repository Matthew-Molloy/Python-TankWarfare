# Entity class to hold information about entities for 38Engine
# Sushil Louis

#from vector import MyVector
import ogre.renderer.OGRE as ogre
from physics import Physics

class Entity:
    mesh = 'robot.mesh'
    pos  = ogre.Vector3(0, 0, 0)
    vel  = ogre.Vector3(0, 0, 0)
    yaw  = 0
    aspects = []
    aspectTypes = [Physics,]
    
    def __init__(self, id, pos = ogre.Vector3(0,0,0), mesh = 'robot.mesh', vel = ogre.Vector3(0, 0, 0), yaw = 0):
        self.id = id
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.yaw = yaw
        self.initAspects()
        self.deltaSpeed = 10
        

    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self))
        

    def tick(self, dtime):
        print "Ent tick", str(self.vel)
        for aspect in self.aspects:
            aspect.tick(dtime)


    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s, yaw: %f" % (self.id, str(self.pos), str(self.vel), self.yaw)
        return x


