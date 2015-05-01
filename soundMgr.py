# Networking manager. Manage networking. Create networking threads, find clients/servers, sync entities

class SoundMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):
        import pygame
        from pygame import *

        pygame.init()
        pygame.mixer.init()
        Background = pygame.mixer.Sound("mars.ogg")
        self.Shoot1 = pygame.mixer.Sound("shoot1.ogg")
        self.Shoot2 = pygame.mixer.Sound("shoot2.ogg")
        Background.play(loops=-1)

    def shoot1(self):
        self.Shoot1.play()

    def shoot2(self):
        self.Shoot2.play()

    def tick(self, dt):
        pass

    def stop(self):
        pass

