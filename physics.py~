# Simple ORIENTED Physics for 38Engine
# vel is rate of change of pos
# Sushil Louis

import math

import utils


class Physics:
    def __init__(self, ent):
        self.ent = ent

    def tick(self, dtime):
        # ----------position-----------------------------------
        timeScaledAcceleration = self.ent.acceleration * dtime
        self.ent.speed += utils.clamp(self.ent.desiredSpeed - self.ent.speed, -timeScaledAcceleration,
                                      timeScaledAcceleration)

        self.ent.vel.x = math.degrees(math.cos(math.radians(-self.ent.heading + self.ent.yawOffset))) * self.ent.speed
        self.ent.vel.z = math.degrees(math.sin(math.radians(-self.ent.heading + self.ent.yawOffset))) * self.ent.speed
        self.ent.vel.y = 0

        self.ent.pos = self.ent.pos + (self.ent.vel * dtime)

        #------------heading----------------------------------
        if self.ent.desiredHeading > 360:
            self.ent.desiredHeading -= 360
        if self.ent.desiredHeading < 0:
            self.ent.desiredHeading += 360

        self.ent.yaw = (self.ent.desiredHeading - self.ent.heading)
        self.ent.heading = self.ent.desiredHeading

