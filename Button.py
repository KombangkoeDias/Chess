import pygame
def button(screen,msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    smallText = pygame.font.Font('freesansbold.ttf',20)
    text = smallText.render(msg,True, (0,0,0))
    Rect = text.get_rect()
    Rect.center = ((x+(w/2)),(y+h/2))
    screen.blit(text,Rect)