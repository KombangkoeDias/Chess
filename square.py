import pygame
def drawSquare(screen,x, y, w,h, ic):
    pygame.draw.rect(screen,ic,(x,y,w,h))
class Square:
    def __init__(self,x,y,w,h,ic):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = ic
        self.chosen = False
        self.click = False
    def choose(self):
        mouse = pygame.mouse.get_pos()
        if (self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y):
            self.chosen = True
            return True
        else:
            self.chosen = False
            return False
    def getclick(self):
        mouse = pygame.mouse.get_pos()
        if (self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y):
            if (pygame.mouse.get_pressed()[0] == 1):
                self.click = True
                return True
            else:
                self.click = False
                return False






