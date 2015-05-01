from vector import Vector3


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
            ent = self.engine.entityMgr.createEnt(entType, pos=Vector3(x, 0, 0))
            ent.setMaterial("Examples/Camo1")
            print "GameMgr Created: ", ent.uiname, ent.eid
            x += 700
            ent = self.engine.entityMgr.createEnt(entType, pos=Vector3(x, 0, 0))
            ent.setMaterial("Examples/Camo2")
            print "GameMgr Created: ", ent.uiname, ent.eid


    def tick(self, dt):
        pass

    def stop(self):
        pass
        

