import pygame as pg

class GameConstants:
    # data ->constants
    MAX_SHOTS = 2  # player bullets on screen
    ALIEN_ODDS = 22 # chances for an alien to appear
    BOMB_ODDS = 60 # chances a new bomb will drop
    ALIEN_RELOAD = 12 # frames between new aliens
    SCREENRECT = pg.Rect(0, 0, 640, 480) 
    SCORE = 0  # INIT SCORE
    