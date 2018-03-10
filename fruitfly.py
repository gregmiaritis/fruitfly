import pygame
from pygame.locals import*
from random import randint


pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255,153,5)
oranged = (218,149,12)
red = (255,0,0)
redd = (255,99,71)
screen = pygame.display.set_mode((890, 550), 0, 32)

#display name
pygame.display.set_caption("Fruit Fly")
pause = False

#pause
def unpause():
    global pause
    pause = False

def paused():
    screen.blit(pygame.image.load("./img/paused.png"), (0, 0))
    
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",700,410,100,50,orange,oranged,unpause)
        button("Quit",700,470,100,50,red,redd,quit_game)

        pygame.display.update()

#menu
def game_intro():

    intro = True
    
    screen.blit(pygame.image.load("./img/1st.png"), (0, 0))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play",700,410,150,50,orange,oranged,game)
        button("Quit",700,470,150,50,red,redd,quit_game)

        pygame.display.update()

#buttons
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action() 
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

#quit
def quit_game():
    pygame.quit()
    quit()

#text_buttons
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game():
        global pause
        x_pos = 0
        y_pos = 0
        x_click = 0
        y_click = 0
        x_orange = 0
        y_orange = randint(0, 450)


        point = 0
        speed = 2
        missed = False


        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = True
                        paused()
               
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == MOUSEMOTION:
                    x_pos, y_pos = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONDOWN:
                    x_click, y_click = pygame.mouse.get_pos()

           
                

            position = (x_pos - 50, y_pos - 50)

            x_orange += 1

            if x_orange * speed > 890 and not missed:
                x_orange = 0
                y_orange = randint(0, 450)


                missed = True

           

            
            # Background and Score
            if point <= 5:
                screen.blit(pygame.image.load("./img/background.png"), (0, 0))
            elif point >= 6 and point <= 10:
                screen.blit(pygame.image.load("./img/background2.png"), (0, 0))
            elif point >= 11 and  point <= 15:
                screen.blit(pygame.image.load("./img/background3.png"), (0, 0))
            elif point >= 16 and  point <= 20:
                screen.blit(pygame.image.load("./img/background4.png"), (0, 0))
            elif point >= 21 and  point <= 25:
                screen.blit(pygame.image.load("./img/background5.png"), (0, 0))
            elif point >= 26 and  point <= 30:
                screen.blit(pygame.image.load("./img/backgroundmoon1.png"), (0, 0))
            elif point >= 31 and  point <= 35:
                screen.blit(pygame.image.load("./img/backgroundmoon2.png"), (0, 0))
            elif point >= 36 and  point <= 40:
                screen.blit(pygame.image.load("./img/backgroundmoon3.png"), (0, 0))
            elif point >=41 and  point <= 45:
                screen.blit(pygame.image.load("./img/backgroundmoon4.png"), (0, 0))
            elif point >= 46 and  point <= 50:
                screen.blit(pygame.image.load("./img/backgroundmoon5.png"), (0, 0))
            elif point >= 51 and  point <= 55:
                screen.blit(pygame.image.load("./img/background.png"), (0, 0))
            elif point >= 56 and point <= 60:
                screen.blit(pygame.image.load("./img/background2.png"), (0, 0))
            elif point >= 61 and  point <= 65:
                screen.blit(pygame.image.load("./img/background3.png"), (0, 0))
            elif point >= 66 and  point <= 70:
                screen.blit(pygame.image.load("./img/background4.png"), (0, 0))
            elif point >= 71 and  point <= 75:
                screen.blit(pygame.image.load("./img/background5.png"), (0, 0))
            elif point >= 76 and  point <= 80:
                screen.blit(pygame.image.load("./img/backgroundmoon1.png"), (0, 0))
            elif point >= 81 and  point <= 85:
                screen.blit(pygame.image.load("./img/backgroundmoon2.png"), (0, 0))
            elif point >= 86 and  point <= 90:
                screen.blit(pygame.image.load("./img/backgroundmoon3.png"), (0, 0))
            elif point >=91 and  point <= 95:
                screen.blit(pygame.image.load("./img/backgroundmoon4.png"), (0, 0))
            elif point >= 96 and  point <= 100:
                screen.blit(pygame.image.load("./img/backgroundmoon5.png"), (0, 0))
                
            
            screen.blit(pygame.font.SysFont("arial", 40).render("Score " + str(point), True, white), (690, 500))
            if x_click in range(x_orange * speed - 30, x_orange * speed + 30) and y_click in range(y_orange - 30, y_orange + 30):
               
                pygame.mixer.music.load("./sound/hit.wav")
                pygame.mixer.music.play()
                point += 1
                speed += 1
                x_orange = 0
                y_orange = randint(50, 500)

            screen.blit(pygame.image.load("./assets/orange.png"), (x_orange * speed, y_orange))

            if missed:
                x_orange = -50
                y_orange = -50
                screen.blit(pygame.image.load("./img/youlose.png"), (0, 0))
                pygame.display.flip()
                pygame.time.delay(3000)
                game_intro()
                
            screen.blit(pygame.image.load("./assets/target.gif").convert(), position)
           
            pygame.display.update()

            


game_intro()
