import pygame
class ChessPieces:
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
def DrawPawnPieces(screen,WhitePawn):
    for pawnlocation in WhitePawn:
        Pawn = ChessPieces('Assets\Pieces\whitePawn.png',pawnlocation)
        screen.blit(Pawn.image,Pawn.rect)


