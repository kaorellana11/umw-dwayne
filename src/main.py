import pygame
import player
import pickle
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
    
 



    dwayne = player.Player(sq_size)
    dwayne.rect.x = 0
    dwayne.rect.y = 0
    if os.path.exists("../saves/autosave.pkl",):
        dwayne.rect.x, dwayne.rect.y = pickle.load(open('../saves/autosave.pkl','rb'))
    dwayne_list = pygame.sprite.Group()
    dwayne_list.add(dwayne)

    steps = 3.5

    #Game Loop
    running = True
    while running:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #PUT PIKL STUFF BETWEEN HERE

                
                if os.path.exists("../saves/autosave.pkl"):
                    os.remove("../saves/autosave.pkl")
                pickle.dump([dwayne.rect.x, dwayne.rect.y], open('../saves/autosave.pkl','wb'))
                print("Your data has been saved")
                
                

                #PUT PIKL STUFF BETWEEN HERE
                running = False
                entity_list.append(dwayne)

        #amount of pixels that moves at a time
            

        #Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    dwayne.schmoove(-steps, 0)

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    dwayne.schmoove(steps, 0)

                if event.key == pygame.K_UP or event.key == ord('w'):
                    dwayne.schmoove(0, -steps)

                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    dwayne.schmoove(0, steps)
                    
                #print("hello")

            #stops movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    dwayne.schmoove(steps, 0)

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    dwayne.schmoove(-steps, 0)

                if event.key == pygame.K_UP or event.key == ord('w'):
                    dwayne.schmoove(0, steps)

                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    dwayne.schmoove(0, -steps)
                    

        screen.blit(background, background_box)
        dwayne.update_pos()
        dwayne_list.draw(screen)
        pygame.display.update()
        clock.tick_busy_loop(60)

    
        




## Start counter on 9/27/2022  Number of times kevin has put computer into sleep mode : 7