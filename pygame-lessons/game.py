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
def main(winstyle=0):

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

    # load the sound effects
    boom_sound = load_sound(main_dir,"boom.wav")
    shot_sound = load_sound(main_dir,"car_door.wav")
    # play the backgroud music
    if pg.mixer:
        music_path = os.path.join(main_dir,"data","house_lo.wav")
        pg.mixer.music.load(music_path)
        pg.mixer.music.play(-1)

    # Initialize Game Groups
    aliens = pg.sprite.Group()
    shots = pg.sprite.Group()
    bombs = pg.sprite.Group()
    all = pg.sprite.RenderUpdates()
    lastalien = pg.sprite.GroupSingle()

    # # Create Some Starting Values
    alienreload = gc.ALIEN_RELOAD
    # create a clock
    clock = pg.time.Clock()
    # initialize our starting sprites
    # PLAYER
    player = Player(all)
    Alien(aliens,all,lastalien) # note, this 'lives' because it goes into a sprite group

    if pg.font:
        all.add(Score(all))

    # Run our main loop whilst the player is alive.
    while player.alive():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("quit....")
                return # has to use inside a function
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                print("escape pressed...")
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if not fullscreen:
                        print("Changing to FULLSCREEN")
                        screen_bk = screen.copy()      # save the current state
                        screen = pg.display.set_mode(
                            gc.SCREENRECT.size,winstyle|pg.FULLSCREEN,bestdepth
                        )
                        # render the new screen
                        screen.blit(screen_bk,(0,0))
                        
                    else:
                        print("Changing to windowed mode")
                        screen_bk = screen.copy()
                        screen = pg.display.set_mode(
                            gc.SCREENRECT.size,winstyle,bestdepth
                        )
                        screen.blit(screen_bk)
                    pg.display.flip()
                    fullscreen = not fullscreen     
            keystate = pg.key.get_pressed()
            # clear/erase the last drawn sprites  
            all.clear(screen,background)       
            # update all the sprites
            all.update()
            # handle player input
            direction = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]   # ← → to move  
            player.move(direction)
            # space bar to shoot
            firing = keystate[pg.K_SPACE]
            if not player.reloading and firing and len(shots) < gc.MAX_SHOTS:
                Shot(
                    player.gunpos,all,shots
                )
                if pg.mixer and shot_sound is not None:
                    shot_sound.play()  
            player.reloading = firing
            # Create new alien
            if alienreload:
                alienreload = alienreload -1
            elif not int(random.random() * gc.ALIEN_ODDS):
                Alien(aliens, all, lastalien)
                alienreload = gc.ALIEN_RELOAD
            # Drop bombs    
            if lastalien and not int(random.random()*gc.BOMB_ODDS):
                Bomb(lastalien.sprite, all, bombs, all)
                
            # Detect collisions between aliens and players.                       
if __name__ == "__main__":
    main()      
    pg.quit()      
        
