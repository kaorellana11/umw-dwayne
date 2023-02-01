import pygame
from main import WIDTH
import time

sq_size = WIDTH / 25

def draw_bound(point_1, point_2):
    global line_arr
    if abs(point_1[0] - point_2[0]) > abs(point_1[1] - point_2[1]):
        point_2[1] = point_1[1]
    else:
        point_2[0] = point_1[0]

    line = pygame.Rect(point_1[0], point_1[1], abs(point_1[0] - point_2[0]), abs(point_1[1] - point_2[1]))
    line_arr.append(line)

pygame.init()
clock = pygame.time.Clock()
line_arr = []

screen = pygame.display.set_mode((WIDTH, WIDTH))

background = pygame.image.load('..\images\path.png').convert()
background = pygame.transform.scale(background, (WIDTH, WIDTH))
background_box = screen.get_rect()

coords_1 = ()
point_placed = True




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            coords_1 = pygame.mouse.get_pos()
            coords_1 = list(coords_1)
            print(coords_1)
        if event.type == pygame.MOUSEBUTTONUP:
            coords_2 = pygame.mouse.get_pos()
            coords_2 = list(coords_2)
            print(coords_2)
            draw_bound(coords_1, coords_2)


        screen.fill((60, 60, 60))
        for line in line_arr:
            pygame.draw.rect(screen, (255, 255, 255), line)
            print(line.left)
        pygame.display.update()
        clock.tick_busy_loop(60)