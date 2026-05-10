"""
define classes of the Role in the game
"""
import random
from typing import List
import pygame as pg
from game_constants import GameConstants as gc

class Player(pg.sprite.Sprite):
    """Representing the player as a moon buggy type car."""

    speed = 10
    bounce = 24
    gun_offset = -11
    images: List[pg.Surface] = []

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=gc.SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(gc.SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def gunpos(self):
        pos = self.facing * self.gun_offset + self.rect.centerx
        return pos, self.rect.top

class Alien(pg.sprite.Sprite):
    speed = 13
    animcycle = 12
    images: List[pg.Surface] = []

    def __init__(self,*groups):
        pg.sprite.Sprite.__init__(self,*groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1,1)) * Alien.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = gc.SCREENRECT.right

    def update(self, *args, **kwargs):
       self.rect.move_ip(self.facing,0)        
       if not gc.SCREENRECT.contains(self.rect):
           self.facing = -self.facing 
           self.rect.top = self.rect.bottom + 1
           self.rect = self.rect.clamp(gc.SCREENRECT)
       self.frame = self.frame + 1   
       self.image = self.images[self.frame // self.animcycle % 3] #divide by zero?

class Explosion(pg.sprite.Sprite):
    defaultlife =12
    animcycle = 3
    images:List[pg.Surface] = []  

    def __init__(self,actor, *groups):
        pg.sprite.Sprite.__init__(self,*groups)    
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife  
    
    def update(self, *args, **kwargs):
        self.life = self.life -1 
        self.image = self.images[self.life // self.animcycle % 2]
        if self.life <= 0:
            self.kill()

class Shot(pg.sprite.Sprite):
    speed = -11
    images: List[pg.Surface] = []

    def __init__(self,pos, *groups):
         pg.sprite.Sprite.__init__(self,*groups)
         self.image = self.images[0]
         self.rect = self.image.get_rect(midbottom=pos)

    def update(self, *args, **kwargs):
        self.rect.move_ip(0,self.speed)     
        if self.rect.top < 0:
            self.kill()

class Bomb(pg.sprite.Sprite):
    speed = 9
    images: List[pg.Surface] = []

    def __init__(self, alien, explosion_group,*groups):
        pg.sprite.Sprite.__init__(self,*groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=alien.rect.move(0, 5).midbottom)
        self.explosion_group = explosion_group

    def update(self, *args, **kwargs):
        self.rect.move_ip(0,self.speed)
        if self.rect.bottom > 470:
            Explosion(self,self.explosion_group)
            self.kill()

class Score(pg.sprite.Sprite):

    def __init__(self, *groups):
       pg.sprite.Sprite.__init__(self,*groups)
       self.font = pg.font.Font(None, 20)   
       self.font.set_italic(1)
       self.color = 'white'
       self.lastscore = -1
       self.update()
       self.rect = self.image.get_rect().move(10,450)       

    def update(self, *args, **kwargs):
        if gc.SCORE !=self.lastscore:
            self.lastscore = gc.SCORE 
            msg = f"Score: {gc.SCORE}"
            self.image = self.font.render(msg,0,self.color)