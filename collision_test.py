import pygame

def stop_rect():
    global speed
    rectangle.x += speed
    if rectangle.right >= WIDTH or rectangle.left <= 0:
        speed *= -1

running = True
pygame.init()
clock = pygame.time.Clock()

WIDTH = HEIGHT = 525
screen = pygame.display.set_mode((WIDTH, HEIGHT))

rectangle = pygame.Rect(10, 10, 30, 30)
line = pygame.Rect(WIDTH/2, 0, 1, HEIGHT)
speed = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, (255, 255, 255), rectangle)
    pygame.draw.rect(screen, (255, 255, 255), line)
    stop_rect()
    pygame.display.flip()
    clock.tick(60)