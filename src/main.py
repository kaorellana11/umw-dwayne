import pygame
import entity
import pickle
import GameState
import os

if __name__ == "__main__":
        
    WIDTH = HEIGHT = 525
    sq_size = WIDTH/25

    save_path = "..\saves\\"
    
    
    
    #initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    

    #create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #Titlebar stuff
    pygame.display.set_caption("Dwayneson's Pancake Persuit")
    icon = pygame.image.load('..\images\dwayneson.png')
    pygame.display.set_icon(icon)


    background = pygame.image.load('..\images\path.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_box = screen.get_rect()

    entity_list = []
    
 



    dwayne = entity.Entity(sq_size, "../images/walk")
    dwayne.rect.x = 0
    dwayne.rect.y = 0
    if os.path.exists("../saves/autosave.pkl",):
        dwayne.rect.x, dwayne.rect.y = pickle.load(open('../saves/autosave.pkl','rb'))
    dwayne_list = pygame.sprite.Group()
    dwayne_list.add(dwayne)

    man = entity.Entity(sq_size, "../images/walk")
    man.rect.x = man.rect.y = 212
    npc_list = pygame.sprite.Group()
    npc_list.add(man)

    

    
    velocity = 3.5
    Game = GameState.GameState()
    #Game Loop
    running = True
    while running:        
        Game.i()
        clock.tick_busy_loop(60)

    
        




## Start counter on 9/27/2022  Number of times kevin has put computer into sleep mode : 7