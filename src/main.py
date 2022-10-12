import pygame
import player


if __name__ == "__main__":
        
    WINDOW_SIZE = (520, 520)
    
    
    #initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    

    #create the screen
    screen = pygame.display.set_mode(WINDOW_SIZE)

    
    background = pygame.image.load('..\images\path.png').convert()
    background = pygame.transform.scale(background, WINDOW_SIZE)
    background_box = screen.get_rect()


    #Titlebar stuff
    pygame.display.set_caption("Dwayneson's Pancake Persuit")
    icon = pygame.image.load('..\images\dwayneson.png').convert()
    pygame.display.set_icon(icon)

    dwayne = player.Player()
    dwayne.rect.x = 0
    dwayne.rect.y = 0
    dwayne_list = pygame.sprite.Group
    dwayne_list.add(player)


    #Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        #Controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                pass
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                pass
            if event.key == pygame.K_UP or event.key == ord('w'):
                pass
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                pass
        if event.type == pygame.KEYUP:
            #fill with opposite of previous if statement
            pass

        screen.blit(background, background_box)
        dwayne_list.draw(screen)
        pygame.display.update()
        clock.tick_busy_loop(60)
        




## Start counter on 9/27/2022  Number of times kevin has put computer into sleep mode : 5
