import pygame
pygame.init()

win = pygame.display.set_mode((1040,640))
pygame.display.set_caption("The Maze")
prize=pygame.image.load("Prize.png")

logo=pygame.image.load("Logo.png")
pygame.display.set_icon(logo)

wall=pygame.image.load("Block.jpg")

clock=pygame.time.Clock()
x = 10
y = 30
rad=6
vel = 10

def maze():
    mazelist=['____________________________________________________',
              '|                                                  |',
              '|  XXX  XX  XX  XX  XXXXXXXXXXXXXXXXXXXXXXXXXX  XXX|',
              '|    X   X   X   X                                 |',
              '|XX  XX  XXX XX  XX   XXXXXXXXXXXXXX  XXXXXXXXXXXXX|',
              '| X   X  X        X   X                            |',
              '| XX  XXXX XX     XXXXX   XXXXXXXXXXXXXXXXXXXX     |',
              '|     X     X         X             X              |',
              '|XX XXX  XX XXXXX     XXXXXXXXXXXXXXX         XXXXX|',
              '|         X     X                                  |',
              '|  XXXXX  XXX   XXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXX|',
              '|  X   X    X                    X       X         |',
              '|XXX  XX XX XXXXXXXXXXXX  XX  XXXXXXXX  XX  XXX  X |',
              '|  X XX   X  X    X   X  XX    X     X   X   X   X |',
              '|  X  XXX X     X     X  X        X XX XXX   X XXX |',
              '|  XX  X  X   X XX  XXX  XXXX  XXXX  X X X XXX X X |',
              '|X  XX XX XXX X  X   X   X  X     X  X X X   X X   |',
              '|  XX   X X   X                   X  XXX    XX XXX |',
              '| XX  XXX   XXX XX   XXXXXXXXXXXXXX    XXXXXX    X |',
              '|  X    X X  X   X    X      X    X  XXX    XXX XX |',
              '|XXX XXXX XX XX  XXXXXX  XXXXX                   X |',
              '|     X X  X  XX      XXXX   XXXXXXXXXXXXXXXXXXXXX |',
              '|  XXXX XXX  XXXX X      XXX                       |',
              '|  X    X    X    XXXXX XX XXXXXXXX    X        XXX|',
              '| XX   XX X XX   XX   X  X    X  X    XXXXXX   XX  |',
              '|  X    X         X   X  XX   X  XXX   X  XXXX  X  |',
              '|X X X       X  XXX   X       X XX     XX  X    X  |',
              '|XX  XXX     X XXX   XX  XXX  X  X   XX    XXXX    |',
              '| X    XXX       XX XX  XX XXXX  X    X      X XX  |',              
              '|        XXXXXXXXX   XXXX     X XXX   XXXX   X  XXX|',
              '|XXXXXXXXX                                                 ',
              '____________________________________________________',

              ]

               

    for i in range(len(mazelist)):
        for j in range(len(mazelist[i])):
            if  mazelist[i][j] in ['X','_','|']:
                win.blit(wall,(20*j,20*i))
        

def gamewindow():
    win.fill((211,211,211))
    maze()

    pygame.draw.rect(win,(0,255,0),(0,20,20,20))
    win.blit(prize,(1020,600))
    
    pygame.draw.circle(win,(255,0,0),(x,y),rad)
    pygame.display.update() 


running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1040-rad-vel:  # Making sure the top right corner of our character is less than the screen width - its width 
        x += vel

    if keys[pygame.K_UP] and y > vel:  # Same principles apply for the y coordinate
        y -= vel

    if keys[pygame.K_DOWN] and y < 640 -rad-vel:
        y += vel

    gamewindow()
    
pygame.quit()
