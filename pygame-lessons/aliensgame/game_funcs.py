import os
import pygame as pg


def load_image(main_dir,file):
    file = os.path.join(main_dir,"data",file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    return surface.convert()

def load_sound(main_dir,file):
    if not pg.mixer: # the mixer submodule needs to init,just use pg.mixer.init() to initialize it
        return None
    file = os.path.join(main_dir,"data",file)
    try:
        sound = pg.mixer.Sound(file) # sound effect
        return sound
    except pg.error:
         print(f"Warning, unable to load, {file}")
    return None