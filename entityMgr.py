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
        pass

    def init(self):
        self.sceneManager = None
        pass

    def tick(self, dt):
        for uid, ent in self.ents.items():
            ent.tick(dt)
            if ent.pos.z > 5000:
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

    def createGent(self, mid, mmesh, mpos, myaw, mmaterial):
        e = self.sceneManager.createEntity(mid, mmesh)
        e.setMaterialName(mmaterial)
        fileRoot = mmesh.split('.')
        materialName = fileRoot[0] + ".material"
        node = self.sceneManager.getRootSceneNode().createChildSceneNode(mid + 'node', mpos)
        node.attachObject(e)
        return node


