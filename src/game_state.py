import pygame
import os
import entity
import pickle


class GameState():
    def __init__(self):
       self.state = 'main_game'
       
       
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            
                #PUT PIKL STUFF BETWEEN HERE
                running = False
                

    

        screen.blit(background, background_box)
        
        
        
        pygame.display.update()

    def main_game(self):
        
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

    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    dwayne.schmoove(-velocity, 0)

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    dwayne.schmoove(velocity, 0)

                if event.key == pygame.K_UP or event.key == ord('w'):
                    dwayne.schmoove(0, -velocity)

                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    dwayne.schmoove(0, velocity)
                
    #stops movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    dwayne.schmoove(velocity, 0)

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    dwayne.schmoove(-velocity, 0)

                if event.key == pygame.K_UP or event.key == ord('w'):
                    dwayne.schmoove(0, velocity)

                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    dwayne.schmoove(0, -velocity)


        if dwayne.rect.left < 0:
            dwayne.rect.left = 0
        if dwayne.rect.right >= WIDTH:
            dwayne.rect.right = WIDTH
        if dwayne.rect.top < 0:
            dwayne.rect.top = 0
        if dwayne.rect.bottom >= HEIGHT:
            dwayne.rect.bottom = HEIGHT
                

        screen.blit(background, background_box)
        dwayne.update_pos()
        dwayne_list.draw(screen)
        npc_list.draw(screen)
        pygame.display.update()