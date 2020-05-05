import pygame
from Piece import ChessPieces
from moves import WhitePawnMoves,BlackPawnMoves,KnightMoves,BishopMoves
def drawSquare(screen,mySquare,ic):
    pygame.draw.rect(screen,ic,(mySquare.x,mySquare.y,mySquare.w,mySquare.h))
whiteside = 'White'
blackside = 'Black'
noside = ''
Empty = 'Empty Space'
PawnW = 'WhitePawn'
PawnB = 'BlackPawn'
KnightW = 'WhiteKnight'
KnightB = 'BlackKnight'
BishopW = 'WhiteBishop'
BishopB = 'BlackBishop'
RookW = 'WhiteRook'
RookB = 'BlackRook'
QueenW = 'WhiteQueen'
QueenB = 'BlackQueen'
KingW = 'WhiteKing'
KingB = 'BlackKing'
WhiteList = [PawnW,KnightW,BishopW,RookW,QueenW,KingW]
BlackList = [PawnB,KnightB,BishopB,RookB,QueenB,KingB]
class Square:
    def __init__(self,x,y,w,h,ic):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = ic
        self.chosen = False
        self.click = False
        self.Piece = ChessPieces('Assets\Pieces\whitePawn.png', (0,0),Empty,None,noside)
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
    def addPieces(self,Piece):
        self.Piece = Piece
    def evaluatepossiblemoves(self,Squarelist):
        walkresult = list()
        eatresult = list()
        for i in range(8):
            for j in range(8):
                if Squarelist[i][j] == self:
                    a = i
                    b = j
        if (self.Piece.type == PawnW):
            walkresult,eatresult = WhitePawnMoves(Squarelist,a,b,walkresult,eatresult)
        if (self.Piece.type == PawnB):
            walkresult,eatresult = BlackPawnMoves(Squarelist,a,b,walkresult,eatresult)
        if (self.Piece.type == KnightW):
            walkresult,eatresult = KnightMoves(Squarelist,a,b,walkresult,eatresult,KnightW)
        if (self.Piece.type == KnightB):
            walkresult,eatresult = KnightMoves(Squarelist,a,b,walkresult,eatresult,KnightB)
        if (self.Piece.type == BishopW):
            #print(a,b)
            walkresult,eatresult = BishopMoves(Squarelist,a,b,walkresult,eatresult,whiteside)
        if (self.Piece.type == BishopB):
            #print(a,b)
            walkresult,eatresult = BishopMoves(Squarelist,a,b,walkresult,eatresult,blackside)
        return (walkresult,eatresult)





