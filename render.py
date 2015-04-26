# Simple ORIENTED Physics for 38Engine
# vel is rate of change of pos
# Sushil Louis
import ogre.renderer.OGRE as ogre
from vector import MyVector
import utils
import math

class Renderable:
    def __init__(self, ent):
        self.ent = ent
        
    def tick(self, dtime):
        #----------position-----------------------------------
        self.ent.node.setPosition(self.ent.pos)
        #------------heading----------------------------------
        self.ent.node.yaw(ogre.Degree(self.ent.yaw))



