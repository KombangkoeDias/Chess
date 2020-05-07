import pygame
from Piece import ChessPieces
from moves import WhitePawnMoves,BlackPawnMoves,KnightMoves,BishopMoves,RookMoves,QueenMoves,KingMoves
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

def evaluatelose(Squarelist,side):
    value = 0
    ischeck = False
    if (side == whiteside):
        for k in range(8):
            for l in range(8):
                if (Squarelist[k][l].Piece.side == whiteside):
                    walkresult,eatresult = Squarelist[k][l].evaluatepossiblemoves(Squarelist)
                    walkresult,eatresult = Squarelist[k][l].checkPossibleMoves(Squarelist,walkresult,eatresult,whiteside)
                    value += len(walkresult)
                    value += len(eatresult)
        if (value == 0):
            return True
        else:
            return False
    else:
        for k in range(8):
            for l in range(8):
                if (Squarelist[k][l].Piece.side == blackside):
                    walkresult, eatresult = Squarelist[k][l].evaluatepossiblemoves(Squarelist)
                    walkresult, eatresult = Squarelist[k][l].checkPossibleMoves(Squarelist, walkresult, eatresult,blackside)
                    value += len(walkresult)
                    value += len(eatresult)
        if (value == 0):
            return True
        else:
            return False

def findSquarePosition(Squarelist,mySquare):
    for i in range(8):
        for j in range(8):
            if (Squarelist[i][j] == mySquare):
                return (i,j)

def evaluateCheck(Squarelist,side):
    for i in range(8):
        for j in range(8):
            if side == whiteside:
                if (Squarelist[i][j].Piece.type == KingW):
                    for k in range(8):
                        for l in range(8):
                            if (Squarelist[k][l].Piece.side != side and Squarelist[k][l].Piece.type != KingW and Squarelist[k][l].Piece.type != KingB):
                                walk,move = Squarelist[k][l].evaluatepossiblemoves(Squarelist)
                                if (Squarelist[i][j] in walk or Squarelist[i][j] in move):
                                    return (True,i,j)
                    return (False,i,j)
            if side == blackside:
                if (Squarelist[i][j].Piece.type == KingB):
                    for k in range(8):
                        for l in range(8):
                            if (Squarelist[k][l].Piece.side != side and Squarelist[k][l].Piece.type != KingW and Squarelist[k][l].Piece.type != KingB):
                                walk,move = Squarelist[k][l].evaluatepossiblemoves(Squarelist)
                                if (Squarelist[i][j] in walk or Squarelist[i][j] in move):
                                    return (True,i,j)
                    return (False,i,j)


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
            walkresult,eatresult = BishopMoves(Squarelist,a,b,walkresult,eatresult,whiteside)
        if (self.Piece.type == BishopB):
            walkresult,eatresult = BishopMoves(Squarelist,a,b,walkresult,eatresult,blackside)
        if (self.Piece.type == RookW):
            walkresult,eatresult = RookMoves(Squarelist,a,b,walkresult,eatresult,whiteside)
        if (self.Piece.type == RookB):
            walkresult,eatresult = RookMoves(Squarelist,a,b,walkresult,eatresult,blackside)
        if (self.Piece.type == QueenW):
            walkresult,eatresult = QueenMoves(Squarelist,a,b,walkresult,eatresult,whiteside)
        if (self.Piece.type == QueenB):
            walkresult,eatresult = QueenMoves(Squarelist,a,b,walkresult,eatresult,blackside)
        if (self.Piece.type == KingW):
            walkresult,eatresult = KingMoves(Squarelist,a,b,walkresult,eatresult,whiteside)
        if (self.Piece.type == KingB):
            walkresult,eatresult = KingMoves(Squarelist,a,b,walkresult,eatresult,blackside)
        return (walkresult,eatresult)

    def movenow(self,Squarelist,destination):
        firstPiece = self.Piece
        secondPiece = destination.Piece
        (firstpos1, firstpos2) = findSquarePosition(Squarelist, self)
        (secondpos1, secondpos2) = findSquarePosition(Squarelist, destination)
        Squarelist[firstpos1][firstpos2].addPieces(
            ChessPieces('Assets\Pieces\whitePawn.png', (firstPiece.rect.left, firstPiece.rect.top), Empty, None,
                        noside))
        Squarelist[secondpos1][secondpos2].addPieces(
            ChessPieces(firstPiece.imagefile, (secondPiece.rect.left, secondPiece.rect.top), firstPiece.type, firstPiece.order,firstPiece.side))
    def checkPossibleMoves(self,Squarelist, walkresult, eatresult,side):
        newwalkresult = list()
        neweatresult = list()
        for walkmove in walkresult:
            self.movenow(Squarelist,walkmove)
            value,i,j = evaluateCheck(Squarelist,side)
            if (not value):
                newwalkresult.append(walkmove)
            walkmove.movenow(Squarelist,self)
        for eatmove in eatresult:
            firstPiece = self.Piece
            secondPiece = eatmove.Piece
            (firstpos1, firstpos2) = findSquarePosition(Squarelist, self)
            (secondpos1, secondpos2) = findSquarePosition(Squarelist, eatmove)
            Squarelist[firstpos1][firstpos2].addPieces(
                ChessPieces('Assets\Pieces\whitePawn.png', (firstPiece.rect.left, firstPiece.rect.top), Empty, None,
                            noside))
            Squarelist[secondpos1][secondpos2].addPieces(
                ChessPieces(firstPiece.imagefile, (secondPiece.rect.left, secondPiece.rect.top), firstPiece.type,
                            firstPiece.order, firstPiece.side))
            value,i,j = evaluateCheck(Squarelist,side)
            if (not value):
                neweatresult.append(eatmove)
            Squarelist[firstpos1][firstpos2].addPieces(firstPiece)
            Squarelist[secondpos1][secondpos2].addPieces(secondPiece)
        return (newwalkresult,neweatresult)



