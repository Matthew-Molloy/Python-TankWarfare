# Networking manager. Manage networking. Create networking threads, find clients/servers, sync entities
import pygame
from pygame import *

class SoundMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):

	self._songs = ['1000.ogg','mars.ogg','sandStorm.ogg', 'up.ogg', 'getLow.ogg']
        currentsong = 0

        pygame.init()
	self.PlayList = pygame.mixer.music
        self.play_next_song()
        self.Shoot1 = pygame.mixer.Sound("shoot1.ogg")
        self.Shoot2 = pygame.mixer.Sound("shoot2.ogg")
        #self.Background.play(loops=-1)
	self.win = pygame.mixer.Sound("Win.ogg")

    def shoot1(self):
        self.Shoot1.play()

    def shoot2(self):
        self.Shoot2.play()

    def tick(self, dt):
        pass

    def stop(self):
        pass
  
    def play_next_song(self):
       self._songs = self._songs[1:] + [self._songs[0]] # move current song to the back of the list 
       self.PlayList.load(self._songs[0])
       self.PlayList.play()
