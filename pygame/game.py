"""
pygame === sdl wrapper
to install : pip install pygame
pygame submodule : image,mixer...

1.we put all the constants in a seperate file name game_constants.py->GameConstants class

"""
import os
import random
from typing import List
import pygame as pg
from game_constants import GameConstants as gc
from game_roles import Player
from game_funcs import load_image,load_sound

if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

main_dir = os.path.split(os.path.abspath(__file__))[0]
# print(main_dir) # d:\pc_programming_live\python_study_live\pygame

pg.init()
pg.mixer.init()
load_sound(main_dir,"boom.wav")
img = load_image(main_dir,"player1.gif")
Player.images = [img, pg.transform.flip(img, 1, 0)]
# print(gc.ALIEN_ODDS)
player  = Player()
print(player.gunpos)