class SelectionMgr():
    def __init__(self, engine):
        self.engine = engine
        self.gfx = self.engine.gfxMgr
        self.entityMgr = self.engine.entityMgr
        pass

    def init(self):
        pass

    def startCheck(self, point):
        if point.x <= 111.0 and point.x >= -112.0 and point.z >= -950.0 and point.z <= -535.0:
            return True

    def instructionsCheck(self, point):
        if point.x <= 39.7 and point.x >= -75.4 and point.z >= 83.61 and point.z <= 110.46:
            return True

    def creditsCheck(self, point):
        if point.x <= -2.88 and point.x >= -75.94 and point.z >= 128.1 and point.z <= 151.88:
            return True

    def tick(self, dt):
        pass

    def stop(self):
        pass


