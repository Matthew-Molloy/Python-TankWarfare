# Entity class to hold information about entities for 38Engine
# Sushil Louis
import ogre.renderer.OGRE as ogre

from vector import MyVector
from physics import Physics
from render import Renderable


class Entity:
    aspectTypes = [Physics, Renderable]

    def __init__(self, id, engine, pos=MyVector(0, 0, 0), mesh='robot.mesh', vel=MyVector(0, 0, 0), yaw=0):
        self.id = id
        self.material = None
        self.yawOffset = 0
        self.collision = False
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.deltaSpeed = 30
        self.deltaYaw = .5
        self.speed = 0.0
        self.heading = 0.0
        self.aspects = []
        self.initAspects()
        self.engine = engine
        self.uiname = None

    def setMaterial(self, material):
        self.ent.setMaterialName(material)


    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self))


    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)
        self.checkCollision(dtime)

    def destroy(self):
        ogreObj = self.node.detachObject(self.id)
        light = self.node.detachObject('light' + self.id)
        self.engine.gfxMgr.sceneManager.destroyLight(light)
        self.engine.gfxMgr.sceneManager.destroyEntity(ogreObj)
        self.engine.gfxMgr.sceneManager.destroySceneNode(self.node)
        del self.engine.entityMgr.ents[int(self.id)]

    def __str__(self):
        x = "Entity: %s \nPos: %s, Vel: %s,  mesh = %s\nSpeed: %f, Heading: %f" % (
            self.id, str(self.pos), str(self.vel), self.mesh, self.speed, self.heading)
        return x


class Tank(Entity):
    def __init__(self, id, engine, pos=MyVector(0, 0, 0), vel=MyVector(0, 0, 0), yaw=0):
        Entity.__init__(self, id, engine=engine, pos=pos, vel=vel, yaw=yaw)
        self.mesh = 'tank.mesh'
        self.uiname = 'TANK'
        self.eid = id
        self.yawOffset = 90
        self.acceleration = 5
        self.turningRate = 0.2
        self.maxSpeed = 20
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.engine = engine
        self.checkValue = 500
        self.health = 100
        self.oElement = "Tank " + str(id)

        self.node = self.engine.gfxMgr.sceneManager.getRootSceneNode().createChildSceneNode(self.pos)
        self.ent = self.engine.gfxMgr.sceneManager.createEntity(self.eid, self.mesh)
        self.node.attachObject(self.ent)

        self.light = self.engine.gfxMgr.sceneManager.createLight('light' + self.id)
        self.light.type = ogre.Light.LT_POINT
        self.node.attachObject(self.light)

    def checkCollision(self, dtime):
        # checkValue indicates the distance from the target ent to the collision spot of the current ent
        for key, target in self.engine.entityMgr.ents.items():
            diffZ = target.pos.z - self.pos.z
            diffX = target.pos.x - self.pos.x
            self.distance = ogre.Math.Sqrt(ogre.Math.Sqr(diffZ) + ogre.Math.Sqr(diffX))

            if target.uiname == 'TANK' and target.eid is not self.eid:
                if self.distance.valueDegrees() < target.checkValue:
                    self.collision = True
                    self.speed = 0
                    self.desiredSpeed = 0

            if target.uiname == 'IWALL' and target.eid is not self.eid:
                if self.distance.valueDegrees() < target.checkValue:
                    self.collision = True
                    self.speed = 0
                    self.desiredSpeed = 0
	     	   
            if target.uiname == 'CBALL' and target.tankID != self.eid:
                if self.distance.valueDegrees() < target.checkValue:
                    self.collision = True
                    target.pos.y -= 10000
                    self.health -= 5
                    ele = self.engine.widgetMgr.overlayManager.getOverlayElement(self.oElement)
                    ele.setCaption(self.oElement + " Health: " + str(self.health))

    def shoot(self):
        ent = self.engine.entityMgr.createEnt(CannonBall, pos=MyVector(self.pos.x, 250, self.pos.z))
        ent.setMaterial("Examples/Camo1")
        ent.tankID = self.eid
        ent.desiredHeading = self.desiredHeading


    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)
            self.checkCollision(dtime)

        if self.health <= 0:
            self.destroy()


class CannonBall(Entity):
    def __init__(self, id, engine, tankID='Null', pos=None, vel=MyVector(0, 0, 0), yaw=0):
        Entity.__init__(self, id, engine=engine, pos=pos, vel=vel, yaw=yaw)
        self.mesh = 'Sphere20.mesh'
        self.material = "Examples/CannonBall"
        self.uiname = 'CBALL'
        self.eid = id
        self.yawOffset = 90
        self.acceleration = 500
        self.turningRate = 0.2
        self.maxSpeed = 32
        self.desiredSpeed = 500
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.engine = engine
        self.checkValue = 300
        self.tankID = tankID

        self.node = self.engine.gfxMgr.sceneManager.getRootSceneNode().createChildSceneNode(self.pos)
        self.ent = self.engine.gfxMgr.sceneManager.createEntity(self.eid, self.mesh)
        self.node.attachObject(self.ent)

        self.light = self.engine.gfxMgr.sceneManager.createLight('light' + self.id)
        self.light.type = ogre.Light.LT_POINT
        self.node.attachObject(self.light)

    def checkCollision(self, dtime):
        for key, target in self.engine.entityMgr.ents.items():
            diffZ = target.pos.z - self.pos.z
            diffX = target.pos.x - self.pos.x
            self.distance = ogre.Math.Sqrt(ogre.Math.Sqr(diffZ) + ogre.Math.Sqr(diffX))

            if target.uiname == 'OWALL' or target.uiname == "IWALL":
                if self.distance.valueDegrees() < target.checkValue:
                    self.collision = True
                    self.pos.y -= 10000


class OutterWall(Entity):
    def __init__(self, id, engine, tankID='Null', pos=None, vel=MyVector(0, 0, 0), yaw=0):
        Entity.__init__(self, id, engine=engine, pos=pos, vel=vel, yaw=yaw)
        self.mesh = 'Wall3.mesh'
        self.material = "Examples/CannonBall"
        self.uiname = 'OWALL'
        self.eid = id
        self.yawOffset = 0
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.engine = engine
        self.checkValue = 400
        self.tankID = tankID

        self.node = self.engine.gfxMgr.sceneManager.getRootSceneNode().createChildSceneNode(self.pos)
        self.ent = self.engine.gfxMgr.sceneManager.createEntity(self.eid, self.mesh)
        self.node.attachObject(self.ent)
        self.node.rotate(ogre.Vector3(0, 1, 0), ogre.Math.DegreesToRadians(yaw))

        self.light = self.engine.gfxMgr.sceneManager.createLight('light' + self.id)
        self.light.type = ogre.Light.LT_POINT
        self.node.attachObject(self.light)

    def checkCollision(self, dtime):
        pass


class InnerWall(Entity):
    def __init__(self, id, engine, tankID='Null', pos=None, vel=MyVector(0, 0, 0), yaw=0):
        Entity.__init__(self, id, engine=engine, pos=pos, vel=vel, yaw=yaw)
        self.mesh = 'wallCube.mesh'
        self.material = "Examples/CannonBall"
        self.uiname = 'IWALL'
        self.eid = id
        self.yawOffset = 0
        self.acceleration = 0
        self.turningRate = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.engine = engine
        self.checkValue = 300
        self.tankID = tankID

        self.node = self.engine.gfxMgr.sceneManager.getRootSceneNode().createChildSceneNode(self.pos)
        self.ent = self.engine.gfxMgr.sceneManager.createEntity(self.eid, self.mesh)
        self.node.attachObject(self.ent)
        self.node.rotate(ogre.Vector3(0, 1, 0), ogre.Math.DegreesToRadians(yaw))

        self.light = self.engine.gfxMgr.sceneManager.createLight('light' + self.id)
        self.light.type = ogre.Light.LT_POINT
        self.node.attachObject(self.light)


    def checkCollision(self, dtime):
        pass


