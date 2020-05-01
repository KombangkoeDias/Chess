import pygame
from numpy import vectorize

from Background import Background

pygame.init()


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (128,0,0)
black = (0,0,0)
gold = (255,215,0)
vegasgold = (197,179,88)

Width = 1000
Height = 600

Background = Background('Chessbackground.png',[0,0])
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

# infinite loop 
while True:
    screen.blit(Background.image,Background.rect)
    screen.blit(text,textRect)
    screen.blit(Startplaying,startRect)
    pygame.draw.rect(screen, vegasgold, (Width//2 - 100, Height//2 + 50, 150, 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
    pygame.display.update()