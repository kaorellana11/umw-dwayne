import pygame, sys, os, pickle
from entity import Entity

class GameState():
    def __init__(self):
        self.state = 'lvl_1'

    def returnPlayer(self):
        for row in lvl_arr1:
            for item in row:
                if str(type(item)) == "<class 'entity.Entity'>":
                    return item
    def save_game(self):
        if os.path.exists("../saves/autosave.pkl"):
                    os.remove("../saves/autosave.pkl")
        pickle.dump(self.state, open('../saves/autosave.pkl','wb'))
        print("Your data has been saved")

    def lvl_1(self):
        player = self.returnPlayer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save_game()
                pygame.quit()
                sys.exit()
            
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.schmoove(-1, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.schmoove(1, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.schmoove(0, -1)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    player.schmoove(0, 1)
                if event.key == pygame.K_ESCAPE:
                    self.state = "pause"
                #self.keydown = True
                
                    
        #stops movement
            if event.type == pygame.KEYUP: #and self.keydown == True:
                if (event.key == pygame.K_LEFT or event.key == ord('a')) and self.keydown[0]:
                    player.schmoove(1, 0)
                if (event.key == pygame.K_RIGHT or event.key == ord('d')) and self.keydown[1]:
                    player.schmoove(-1, 0)
                if (event.key == pygame.K_UP or event.key == ord('w')) and self.keydown[2]:
                    player.schmoove(0, 1)
                if (event.key == pygame.K_DOWN or event.key == ord('s')) and self.keydown[3]:
                    player.schmoove(0, -1)
                                
        """
        if dwayne.rect.left < 0:
            dwayne.rect.left = 0
        if dwayne.rect.right >= WIDTH:
            dwayne.rect.right = WIDTH
        if dwayne.rect.top < 0:
            dwayne.rect.top = 0
        if dwayne.rect.bottom >= HEIGHT:
            dwayne.rect.bottom = HEIGHT
        """
        screen.blit(background, background_box)
        
        player.update_pos()
        item_group1.draw(screen)
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
        if self.state == "lvl_1":
            self.lvl_1()

def level_creator(resolution, lvl_string):
    
        row_strings = []

        row_str = ""
        for s in lvl_string:
            try:
                x = int(s)
                row_str += ("*" * x)

            except Exception as e:
                if s == "/":
                    row_strings.append(row_str)
                    row_str = ""
                else:
                    row_str += s
        row_strings.append(row_str)


        arr_width = len(row_strings[0])
        arr_height = len(row_strings)

        lvl_array = []

        if arr_height < arr_width:
            #resolution[0] = width
            sq_size = (resolution[1] / arr_height)
            initial_x = resolution[0] - (sq_size * arr_width) #total width that array occupies
            initial_x /= 2 #gets remainder of width so that screen can be properly letterboxed
            initial_y = 0
        else:
            sq_size = (resolution[0] / arr_width)
            initial_y = resolution[1] - (sq_size * arr_height)
            initial_y /= 2
            initial_x = 0

        cur_row = 0
        cur_col = 0
        for row in range(arr_height):
            lvl_array.append([])
            for c in row_strings[cur_row]:
                if c == "b":
                    pass
                
                elif c == "d":
                    #print("d found")
                    lvl_array[row].append(Entity("../images/walk", sq_size, cur_row, cur_col, initial_x, initial_y))
                elif c == "B":
                    pass
                
                elif c == "t":
                    pass

                elif c == "e":
                    pass

                elif c == "*":
                    lvl_array[row].append(None)
                cur_col += 1
            cur_row += 1
            cur_col = 0
        
        return lvl_array

resolution = [525, 525]

save_path = "..\saves\\"

#initialize pygame
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

#create the screen
screen = pygame.display.set_mode(resolution)

#Titlebar stuff
pygame.display.set_caption("Dwayneson's Pancake Persuit")
icon = pygame.image.load('..\images\dwayneson.png')
pygame.display.set_icon(icon)


background = pygame.image.load('..\images\path.png').convert()
background = pygame.transform.scale(background, resolution)
background_box = screen.get_rect()

entity_list = []


#pre direction shift
"""
    if os.path.exists("../saves/autosave.pkl",):
        dwayne.rect.x, dwayne.rect.y = pickle.load(open('../saves/autosave.pkl','rb'))
    dwayne_list = pygame.sprite.Group()
    dwayne_list.add(dwayne)

    man = old_entity.Entity(sq_size, "../images/walk")
    man.rect.x = man.rect.y = 212
    npc_list = pygame.sprite.Group()
    #npc_list.add(man)
"""

lvl_arr1 = level_creator(resolution, "4/2d1/4/4")
item_group1 = pygame.sprite.Group()
for row in lvl_arr1:
    for item in row:
        if item == None:
            continue
        else:
            item_group1.add(item)
game_state.returnPlayer()

#Game Loop
running = True

while running:
    #player = lvl_arr1[player.]
    game_state.state_manager()
    
    clock.tick_busy_loop(60)
    

## Start counter on 9/27/2022  Number of times kevin has put computer into sleep mode : 8