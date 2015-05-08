from vector import Vector3
from vector import MyVector
import ent


class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        print "starting Game mgr"
        self.game1()
        pass

    def init(self):
        pass


    def loadLevel(self):
        self.engine.gfxMgr.setupGameViews()

    def makeWall(self, direction, size, x, z):
	entityMgr = self.engine.entityMgr
        wallMaterial = "Examples/CannonBall"

	for count in range(1, size+1):
	    if direction == 'V':
		xpos = x
		zpos = (count * 200)+100+z
		
            else:
		xpos = (count * 200)+100+x
		zpos = z

	    if xpos < 5000 and xpos > -5000 and zpos < 5000 and zpos > -5000:
		    entity = entityMgr.createEnt(ent.InnerWall, pos=MyVector(xpos,150,zpos),yaw=0)
		    entity.setMaterial(wallMaterial)

    def game1(self):
        x = 0
        for entType in self.engine.entityMgr.entTypes:
            print "GameMgr Creating", str(entType)
            entity = self.engine.entityMgr.createEnt(entType, pos=Vector3(-4500, 0, 0))
            entity.setMaterial("Examples/Camo1")
            print "GameMgr Created: ", entity.uiname, entity.eid
            x += 700
            entity = self.engine.entityMgr.createEnt(entType, pos=Vector3(4500, 0, 0))
            entity.setMaterial("Examples/Camo2")
            print "GameMgr Created: ", entity.uiname, entity.eid

        self.loadMap()

    def loadMap(self):
        entityMgr = self.engine.entityMgr
        wallMaterial = "Examples/CannonBall"
        #Create 4 walls at edge of map
        entity = entityMgr.createEnt(ent.OutterWall, pos=MyVector(-5000,100,0),yaw=90)
        entity.setMaterial(wallMaterial)
        entity = entityMgr.createEnt(ent.OutterWall, pos=MyVector(5000,100,0),yaw=90)
        entity.setMaterial(wallMaterial)
        entity = entityMgr.createEnt(ent.OutterWall, pos=MyVector(0,100,-5000))
        entity.setMaterial(wallMaterial)
        entity = entityMgr.createEnt(ent.OutterWall, pos=MyVector(0,100,5000))
        entity.setMaterial(wallMaterial)

	#Create 9 extra walls
	self.size = 10
	self.makeWall(direction = 'H', size = self.size,x = -1000,z=0)
	self.makeWall(direction = 'V', size = self.size,x = -2000,z=-1000)
	self.makeWall(direction = 'V', size = self.size,x = 2000,z=-1000)
	self.makeWall(direction = 'V', size = self.size,x = 3000,z=-4000)
	self.makeWall(direction = 'V', size = self.size,x = 0,z=-4000)
	self.makeWall(direction = 'V', size = self.size,x = -3000,z=-4000)
	self.makeWall(direction = 'V', size = self.size,x = 3000,z=2000)
	self.makeWall(direction = 'V', size = self.size,x = 0,z=2000)
	self.makeWall(direction = 'V', size = self.size,x = -3000,z=2000)
	
    def tick(self, dt):
        pass

    def stop(self):
        pass
        

