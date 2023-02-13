import pygame

def stop_rect():
    global x_speed, y_speed, line_arr, x_swapped, y_swapped
    collision_tolerance = 10
    rectangle.x += x_speed
    rectangle.y += y_speed

    if rectangle.right >= WIDTH or rectangle.left <= 0:
        x_speed *= -1
    if rectangle.bottom >= HEIGHT or rectangle.top <= 0:
        y_speed *= -1
        
    for line in line_arr:
        if rectangle.colliderect(line):
            print("Yeah!")
            if (abs(rectangle.right - line.centerx) < collision_tolerance or abs(rectangle.left - line.centerx) < collision_tolerance) and x_swapped == True:
                print("Swap X: " + str(x_swapped))
                x_speed *= -1
                x_swapped = False
            if (abs(rectangle.bottom - line.centery) < collision_tolerance or abs(rectangle.top - line.centery) < collision_tolerance) and y_swapped == True:
                print("Swap Y: " + str(y_swapped))
                y_speed *= -1
                y_swapped = False
        else:
                x_swapped = True
                y_swapped = True



running = True
pygame.init()
clock = pygame.time.Clock()


WIDTH = HEIGHT = 525
screen = pygame.display.set_mode((WIDTH, HEIGHT))

rectangle = pygame.Rect(0, 40, 30, 30)
ver_line = pygame.Rect(WIDTH/2, 0, 1, HEIGHT)
hor_line = pygame.Rect(0, HEIGHT/2, WIDTH, 1)
line_arr = []
line_arr.append(ver_line)
line_arr.append(hor_line)

x_speed = 4
y_speed = 2

x_swapped = y_swapped = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, (255, 255, 255), rectangle)
    pygame.draw.rect(screen, (255, 255, 255), ver_line)
    pygame.draw.rect(screen, (255, 255, 255), hor_line)
    pygame.draw.circle(screen, (255, 0, 0), rectangle.center, 2) 
    stop_rect()
    pygame.display.update()
    clock.tick(60)