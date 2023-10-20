#Name: Kinz
#Date: 13/10/23
#Basic PyGame Setup Code
import pygame, sys



pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
imgoatedIMG = pygame.image.load('images/imgoated.png') #with .png or .jpg included in the name
imgoatedIMG = pygame.transform.scale(imgoatedIMG, (35, 35))  #resize image Where 35 ,35 is the size, (x,y)


#Setup of Starting objects
locximgoated= 186
locyimgoated= 130
speedimgoated=2

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Pygame intro")
def display():
    window.fill((255,255,255)) #White background
    
    #Walls
    #Rectangle1=pygame.draw.rect(window,(255,25,12),(150,100,20,20))
    #Rectangle2=pygame.draw.rect(window,(255,25,12),(180,100,20,20))
    #Rectangle3=pygame.draw.rect(window,(255,25,12),(210,100,20,20))
    #Rectangle4=pygame.draw.rect(window,(255,25,12),(240,100,20,20))
    #Rectangle5=pygame.draw.rect(window,(255,25,12),(150,130,20,20))
    #Rectangle6=pygame.draw.rect(window,(255,25,12),(150,160,20,20))
    #Rectangle7=pygame.draw.rect(window,(255,25,12),(175,180,20,20))
    #Rectangle8=pygame.draw.rect(window,(255,25,12),(205,180,20,20))
    #Rectangle9=pygame.draw.rect(window,(255,25,12),(235,180,20,20))
    #Rectangle10=pygame.draw.rect(window,(255,25,12),(265,180,20,20))
    #Rectangle11=pygame.draw.rect(window,(255,25,12),(295,180,20,20))
    #Rectangle12=pygame.draw.rect(window,(255,25,12),(295,150,20,20))
    #Rectangle13=pygame.draw.rect(window,(255,25,12),(295,120,20,20))
    #Rectangle14=pygame.draw.rect(window,(255,25,12),(295,90,20,20))
    #Rectangle15=pygame.draw.rect(window,(255,25,12),(240,70,20,20))
    
    #Finish Line
    global Finish
    Finishline = pygame.image.load('images/FinishLine.png') #with .png or .jpg included in the name
    Finishline = pygame.transform.scale(Finishline, (40, 35))  #resize image Where 35 ,35 is the size, (x,y)
    Finish=window.blit(Finishline,(265, 50))
    #Wall list
    #walls = [Rectangle1,Rectangle2,Rectangle3,Rectangle4,Rectangle5,
             #Rectangle6,Rectangle7,Rectangle8,Rectangle9,Rectangle10,
             #Rectangle11,Rectangle12,Rectangle13,Rectangle13,Rectangle14,Rectangle15]
    imgoated=window.blit(imgoatedIMG,(locximgoated, locyimgoated))

def Finishgame(imgoated,Finish):
    return Finish.colliderect(imgoated)

while True:
    display()
    for event in pygame.event.get():
      # if user  QUIT then the screen will close
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

    #value name---pygame check if keys down---->Create a variable that is set to all the key values
    key_input = pygame.key.get_pressed()

    
    #var--------value name-----key Left---speed value--value name------key Right---speed value      
    movex = (key_input[pygame.K_LEFT] * -speedimgoated) + (key_input[pygame.K_RIGHT] * speedimgoated)
    movey = (key_input[pygame.K_UP] * -speedimgoated) + (key_input[pygame.K_DOWN] * speedimgoated)
    #x-location + x-speed = new x-location
    locximgoated += movex
    #y-location + y-speed = new y-location
    locyimgoated += movey
    
    display()
    #For x amount of walls in the "walls" list each will be classified as a collision
    #Also 
    #for i in walls:
        #if collision(imgoated,i):
            #locximgoated -= movex
            #locyimgoated -= movey
            
        #display()
    
    if Finishgame(imgoated,Finish):
        Winmsg = pygame.font.SysFont('consolas', 30)
        window.blit(Winmsg.render("You Win!", True, (0, 0, 0)), (250, 250))
        quit()
        
        
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
