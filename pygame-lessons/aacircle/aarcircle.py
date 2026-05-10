import pygame as pg
import pygame.gfxdraw as gfcd

def main():
    # init pygame
    pg.init()
    # create a screen
    screen = pg.display.set_mode((500,500))
    # fill the screen
    screen.fill((255,0,0))
    # create a surface
    s = pg.Surface(screen.get_size(),pg.SRCALPHA,32)
    # draw a line,using pg.draw module
    pg.draw.line(s,(0,0,0),(250,250),(250+200,250))
    
    width =10
    for a_radius in range(width):
        radius = 200
        gfcd.aacircle(s,250,250,radius - a_radius,(0, 0, 0))
    # put it on the screen
    screen.blit(s,(0,0))  
    # draw 2 circle
    pg.draw.circle(s,"green",(50,100),10)  
    pg.draw.circle(s,"black",(50,100),10,1)  

    # update the display
    pg.display.flip()

    try:
        while True:
            event = pg.event.wait()
            if event.type == pg.QUIT:
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_q:
                    break
        pg.display.flip()            

    finally:
        pg.quit()    

if __name__ == '__main__':
    main()


