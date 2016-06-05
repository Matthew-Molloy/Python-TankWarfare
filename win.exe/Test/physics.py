# Simple Physics for 38Engine
# vel is rate of change of pos
# Sushil Louis


class Physics:
    def __init__(self, ent):
        self.ent = ent
        
    def tick(self, dtime):
        #print "Physics tick", dtime
        self.ent.pos = self.ent.pos + (self.ent.vel * dtime)

