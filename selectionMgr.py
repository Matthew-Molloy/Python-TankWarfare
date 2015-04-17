import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import platform

class SelectionMgr(ogre.FrameListener):
    def __init__(self, engine):
        ogre.FrameListener.__init__(self)
        self.engine = engine
        self.gfx = self.engine.gfxMgr
        self.entityMgr = self.engine.entityMgr
        pass

    def init(self):
        self.gfx.root.addFrameListener(self)
        pass

    def tick(self, dt):
        pass

    def stop(self):
        pass

    def frameStarted(self, frameEvent):
        for uid, ent in self.entityMgr.ents.iteritems():
            ent.tick(frameEvent.timeSinceLastFrame)
        return True


