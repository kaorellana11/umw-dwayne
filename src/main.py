import pygame
#import player


if __name__ == "__main__":
        
    #initialize pygame
    pygame.init()
    clock = pygame.time.Clock()


    #create the screen
    screen = pygame.display.set_mode((520, 520))


    #cosmetic shit
    pygame.display.set_caption("Dwayneson's Pancake Persuit")
    icon = pygame.image.load('..\images\dwayneson.png')
    pygame.display.set_icon(icon)


    #Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((100, 100 ,100))
        pygame.display.update()
        clock.tick_busy_loop(60)