"""
pygame === sdl wrapper
to install : pip install pygame
pygame submodule : image,mixer...

1.we put all the constants in a seperate file name game_constants.py->GameConstants class
2.classes we use : Player,Alien,Explosion,Shot,Bomb,Score

"""
import os
import random
from typing import List
import pygame as pg
from game_constants import GameConstants as gc
from game_roles import *
from game_funcs import load_image,load_sound


if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

main_dir = os.path.split(os.path.abspath(__file__))[0]
# print(main_dir) # d:\pc_programming_live\python_study_live\pygame

if pg.get_sdl_version()[0] == 2:
        pg.mixer.pre_init(44100, 32, 2, 1024)
pg.init()
if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None
# not using full screen mode
fullscreen = False
winstyle = 0
bestdepth = pg.display.mode_ok(gc.SCREENRECT.size, winstyle, 32)  
screen = pg.display.set_mode(gc.SCREENRECT.size,winstyle,bestdepth) # create a game screen
# Load images, assign to sprite classes
# (do this before the classes are used, after screen setup)   
# 1.player's image  
img = load_image(main_dir,"player1.gif")
Player.images = [img,pg.transform.flip(img,1,0)]
# 2.explosion images
img = load_image(main_dir,"explosion1.gif")
Explosion.images = [img,pg.transform.flip(img, 1, 1)]
# 3.alien images
Alien.images = [load_image(main_dir,img) for img in ("alien1.gif", "alien2.gif", "alien3.gif")]
# 4.bomb images
Bomb.images = [load_image(main_dir,"bomb.gif")]
# 5.shot images
Shot.images = [load_image(main_dir,"shot.gif")]

# decorate the game window
icon = pg.transform.scale(Alien.images[0],(32,32))
pg.display.set_icon(icon)
pg.display.set_caption("Alien Game")
pg.mouse.set_visible(0)

 # create the background, tile the bgd image
bgdtile = load_image(main_dir,"background.gif")
background = pg.Surface(gc.SCREENRECT.size)
for x in range(0,gc.SCREENRECT.width,bgdtile.get_width()):
       background.blit(bgdtile,(x,0))
screen.blit(background,(0,0))   
pg.display.flip()    