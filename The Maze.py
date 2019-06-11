import pygame
pygame.init()

win = pygame.display.set_mode((1020,600))
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
    mazelist=['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
              'X X   X   X   X   X   X   X   X   X   X   X   X   X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X X X X X X X X X X X X X X X X X X X X X X X X X X',
              'X   X   X   X   X   X   X   X   X   X   X   X   X  ',
              'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',

              ]

               

    for i in range(len(mazelist)):
        for j in range(len(mazelist[i])):
            if mazelist[i][j]=='X':
                win.blit(wall,(20*j,20*i))
        

def gamewindow():
    win.fill((211,211,211))
    maze()

    pygame.draw.rect(win,(0,255,0),(0,20,20,20))
    win.blit(prize,(1000,560))
    
    pygame.draw.circle(win,(255,0,0),(x,y),rad)
    pygame.display.update() 


running = True

while running:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1020-rad-vel:  # Making sure the top right corner of our character is less than the screen width - its width 
        x += vel

    if keys[pygame.K_UP] and y > vel:  # Same principles apply for the y coordinate
        y -= vel

    if keys[pygame.K_DOWN] and y < 600 -rad-vel:
        y += vel

    gamewindow()
    
pygame.quit()
