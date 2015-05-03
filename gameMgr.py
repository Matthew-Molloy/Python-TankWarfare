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


    def game1(self):
        x = 0
        for entType in self.engine.entityMgr.entTypes:
            print "GameMgr Creating", str(entType)
            entity = self.engine.entityMgr.createEnt(entType, pos=Vector3(x, 0, 0))
            entity.setMaterial("Examples/Camo1")
            print "GameMgr Created: ", entity.uiname, entity.eid
            x += 700
            entity = self.engine.entityMgr.createEnt(entType, pos=Vector3(x, 0, 0))
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

    def tick(self, dt):
        pass

    def stop(self):
        pass
        

