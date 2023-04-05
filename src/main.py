import pygame, sys, os, pickle
import old_entity

WIDTH = HEIGHT = 525

def draw_bound(self, surface):
    global bound_arr
    bound_arr = []



if __name__ == "__main__":
    class GameState():
        def __init__(self):
            self.state = 'main_game'
            self.keydown = [None, None, None, None]

        def main_game(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #PUT PIKL STUFF BETWEEN HERE
                    if os.path.exists("../saves/autosave.pkl"):
                        os.remove("../saves/autosave.pkl")
                    pickle.dump([dwayne.rect.x, dwayne.rect.y], open('../saves/autosave.pkl','wb'))
                    print("Your data has been saved")
                    #PUT PIKL STUFF BETWEEN HERE
                    pygame.quit()
                    sys.exit()
                    entity_list.append(dwayne)

                
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        dwayne.schmoove(-velocity, 0)
                        self.keydown[0] = True
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        dwayne.schmoove(velocity, 0)
                        self.keydown[1] = True
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        dwayne.schmoove(0, -velocity)
                        self.keydown[2] = True
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        dwayne.schmoove(0, velocity)
                        self.keydown[3] = True
                    if event.key == pygame.K_ESCAPE:
                        self.keydown = [False, False, False, False]
                        dwayne.move_x = 0
                        dwayne.move_y = 0
                        self.state = "pause"
                    #self.keydown = True
                    
                        
            #stops movement
                if event.type == pygame.KEYUP: #and self.keydown == True:
                    if (event.key == pygame.K_LEFT or event.key == ord('a')) and self.keydown[0]:
                        dwayne.schmoove(velocity, 0)
                        self.keydown[0] = False
                    if (event.key == pygame.K_RIGHT or event.key == ord('d')) and self.keydown[1]:
                        dwayne.schmoove(-velocity, 0)
                        self.keydown[1] = False
                    if (event.key == pygame.K_UP or event.key == ord('w')) and self.keydown[2]:
                        dwayne.schmoove(0, velocity)
                        self.keydown[2] = False
                    if (event.key == pygame.K_DOWN or event.key == ord('s')) and self.keydown[3]:
                        dwayne.schmoove(0, -velocity)
                        self.keydown[3] = False
                                 

            if dwayne.rect.left < 0:
                dwayne.rect.left = 0
            if dwayne.rect.right >= WIDTH:
                dwayne.rect.right = WIDTH
            if dwayne.rect.top < 0:
                dwayne.rect.top = 0
            if dwayne.rect.bottom >= HEIGHT:
                dwayne.rect.bottom = HEIGHT
                        
            
            #print(dwayne.move_x)
            #print(self.keydown)
            screen.blit(background, background_box)
            dwayne.update_pos()
            dwayne_list.draw(screen)
            npc_list.draw(screen)
            pygame.display.update()
            
        def pause(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if os.path.exists("../saves/autosave.pkl"):
                        os.remove("../saves/autosave.pkl")
                    pickle.dump([dwayne.rect.x, dwayne.rect.y], open('../saves/autosave.pkl','wb'))
                    print("Your data has been saved")
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = "main_game"
                        print("Main")

            screen.fill((255, 255, 255))

        def state_manager(self):
            if self.state == "pause":
                self.pause()
            if self.state == "main_game":
                self.main_game()

    #WIDTH = HEIGHT = 525
    sq_size = WIDTH/25
    
    save_path = "..\saves\\"
    
    
    
    #initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    game_state = GameState()
    

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
    
 



    dwayne = old_entity.Entity(sq_size, "../images/walk")
    dwayne.rect.x = 0
    dwayne.rect.y = 0
    if os.path.exists("../saves/autosave.pkl",):
        dwayne.rect.x, dwayne.rect.y = pickle.load(open('../saves/autosave.pkl','rb'))
    dwayne_list = pygame.sprite.Group()
    dwayne_list.add(dwayne)

    man = old_entity.Entity(sq_size, "../images/walk")
    man.rect.x = man.rect.y = 212
    npc_list = pygame.sprite.Group()
    #npc_list.add(man)

    

    
    velocity = 3.5
    
 
    

    #Game Loop
    running = True
    
    game_state.level_creator("bbbb/b2b/b2b/bbbb")
    while running:
        game_state.state_manager()
        
        clock.tick_busy_loop(60)
        

## Start counter on 9/27/2022  Number of times kevin has put computer into sleep mode : 8