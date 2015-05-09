from vector import MyVector
import ent


class EntityMgr:
    def __init__(self, engine):
        print "starting ent mgr"
        self.engine = engine
        self.ents = {}
        self.nEnts = 0
        self.currentSelectedEntIndex = 0
        self.selectedEntIndecies = []
        self.selectedEnt = None
        self.entTypes = [ent.Tank]
        self.tank1Camo = ["Examples/Camo1","Examples/sandStorm_t1","Examples/up_t1","Examples/Camo1","Examples/1000_t1"]
        self.tank2Camo = ["Examples/Camo2","Examples/sandStorm_t2","Examples/up_t2","Examples/Camo2","Examples/1000_t2"]
        self.walls = ["Examples/CannonBall","Examples/sandStorm_walls","Examples/up_walls","Examples/CannonBall","Examples/1000_walls"]
        self.ground = ["Examples/GrassFloor","Examples/sandStorm_ground","Examples/up_ground","Examples/getLow_ground","Examples/1000_ground"]
        self.sky = []
        pass

    def init(self):
        self.sceneManager = None
        pass

    def tick(self, dt):
        for uid, ent in self.ents.items():
            ent.tick(dt)
            if ent.pos.y < -2000:
                ent.destroy()

    def stop(self):
        pass


    def createEnt(self, entType, pos=MyVector(0, 0, 0), yaw=0):
        ent = entType(str(self.nEnts), engine=self.engine, pos=pos, yaw=yaw)

        self.ents[self.nEnts] = ent
        self.selectedEnt = ent
        self.currentSelectedEntIndex = self.nEnts;
        if (len(self.selectedEntIndecies) > 0):
            self.selectedEntIndecies.pop()
        self.selectedEntIndecies.append(ent)
        self.nEnts = self.nEnts + 1
        return ent

    def selectNextEnt(self):
        print self.currentSelectedEntIndex, "    ", self.nEnts
        if self.currentSelectedEntIndex >= self.nEnts - 1:
            self.currentSelectedEntIndex = 0
        else:
            self.currentSelectedEntIndex += 1
        self.selectedEnt = self.ents[self.currentSelectedEntIndex]
        print "EntMgr selected: ", str(self.selectedEnt)
        return self.selectedEnt

    def getSelected(self):
        return self.selectedEnt

    def nextTheme(self):
       self.tank1Camo = self.tank1Camo[1:] + [self.tank1Camo[0]]
       self.tank2Camo = self.tank2Camo[1:] + [self.tank2Camo[0]]
       self.walls = self.walls[1:] + [self.walls[0]]
       self.ground = self.ground[1:] + [self.ground[0]]

       self.ents[0].setMaterial(self.tank1Camo[0])
       self.ents[1].setMaterial(self.tank2Camo[0])
       self.engine.gfxMgr.ground.setMaterialName(self.ground[0])
       i = 0
       for wall in self.ents:
          if i <= 1:
            pass
          else:
            self.ents[i].setMaterial(self.walls[0])
          i += 1


