import pygame

def startGame():
    print("Starting the game now!!!")
def drawmovesline(screen,firstSquare,secondSquare,color,width):
    pygame.draw.line(screen,color,(firstSquare.x+35,firstSquare.y+35),(secondSquare.x+35,secondSquare.y+35),width)
