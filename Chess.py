import pygame
from numpy import vectorize

from Event import startGame
from Button import button
from Background import BackgroundPhoto
from square import drawSquare
from Piece import DrawPawnPieces

pygame.init()


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (128,0,0)
black = (0,0,0)
gold = (255,215,0)
vegasgold = (197,179,88)
tomago = (255,99,71)
darkgreen = (0,100,0)

Width = 1000
Height = 600

Background = BackgroundPhoto('Assets\Chessbackground.png',[0,0])
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption('Chess Game')

font = pygame.font.Font('freesansbold.ttf', 70)
Arialfont = pygame.font.Font('freesansbold.ttf',70)

text = font.render('Welcome to Chess Game ', True, blue)
Startplaying = Arialfont.render('Want to start playing? ', True, blue)

textRect = text.get_rect()
textRect.center = (Width // 2, 80)

startRect = Startplaying.get_rect()
startRect.center = (Width // 2, 180)

clock = pygame.time.Clock()

check = 0



def game_intro():
    intro = True
    while intro:
        screen.blit(Background.image, Background.rect)
        screen.blit(text, textRect)
        screen.blit(Startplaying, startRect)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        intro = button(screen, "Start", Width // 2 - 100, Height // 2 + 50, 150, 40, vegasgold, gold, startGame)
        button(screen,"Quit",Width//2-100,Height//2+120,150,40,red,tomago,quit)
        pygame.display.update()
        clock.tick(15)
# infinite loop

GameplayBackground = BackgroundPhoto('Assets\Horses.jpg',[0,0])

WhitePawn = list()
for i in range(8):
    WhitePawn.append((230+70*i, 460))
def start_game():
    gamePlay = True
    while gamePlay:
        screen.blit(GameplayBackground.image, GameplayBackground.rect)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for i in range(8):
            for j in range(8):
                if ((i+j) % 2 == 0):
                    drawSquare(screen, 220+70*j, 30+70*i, 70, 70,white)
                else:
                    drawSquare(screen, 220+70*i, 30+70*j, 70, 70,darkgreen)
        DrawPawnPieces(screen,WhitePawn)
        pygame.display.update()

game_intro()
start_game()