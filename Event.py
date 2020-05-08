import pygame
from Piece import ChessPieces,DrawPieces
from square import Square
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
noside = ''
whiteside = 'White'
blackside = 'Black'
white = (255,255,255)
darkgreen = (0,100,0)
def drawPieces(screen,Squarelist):
    for i in range(8):
        for j in range(8):
            newSquare = Squarelist[i][j]
            if (Squarelist[i][j].Piece.type != Empty):
                   DrawPieces(screen,newSquare)
def drawSquare(screen,mySquare,ic):
    pygame.draw.rect(screen,ic,(mySquare.x,mySquare.y,mySquare.w,mySquare.h))
def startGame():
    print("Starting the game now!!!")
def drawmovesline(screen,firstSquare,secondSquare,color,width):
    pygame.draw.line(screen,color,(firstSquare.x+35,firstSquare.y+35),(secondSquare.x+35,secondSquare.y+35),width)
def drawChoose(screen,side):
    if (side == whiteside):
        myfirstSquare = Square(900,20,70,70,white)
        mysecondSquare = Square(900,90,70,70,white)
        mythirdSquare = Square(900,160,70,70,white)
        myfourthSquare = Square(900,230,70,70,white)
        drawSquare(screen,myfirstSquare,myfirstSquare.color)
        drawSquare(screen,mysecondSquare,mysecondSquare.color)
        drawSquare(screen,mythirdSquare,mythirdSquare.color)
        drawSquare(screen,myfourthSquare,myfourthSquare.color)
        Queen = ChessPieces('Assets\Pieces\whiteQueen.png', (910,30), 'WhiteQueen', 0,whiteside)
        Rook = ChessPieces('Assets\Pieces\whiteRook.png', (910,100), 'WhiteRook', 0,whiteside)
        Bishop = ChessPieces('Assets\Pieces\whiteBishop.png', (910, 170), 'WhiteBishop', 0, whiteside)
        Knight = ChessPieces('Assets\Pieces\whiteKnight.png', (910, 240), 'WhiteKnight', 0, whiteside)
        myfirstSquare.addPieces(Queen)
        mysecondSquare.addPieces(Rook)
        mythirdSquare.addPieces(Bishop)
        myfourthSquare.addPieces(Knight)
        screen.blit(Knight.image,Knight.rect)
        screen.blit(Bishop.image,Bishop.rect)
        screen.blit(Rook.image,Rook.rect)
        screen.blit(Queen.image,Queen.rect)
        return [myfirstSquare,mysecondSquare,mythirdSquare,myfourthSquare]
    if (side == blackside):
        myfirstSquare = Square(900, 20, 70, 70, darkgreen )
        mysecondSquare = Square(900, 90, 70, 70, darkgreen)
        mythirdSquare = Square(900, 160, 70, 70, darkgreen)
        myfourthSquare = Square(900, 230, 70, 70, darkgreen)
        drawSquare(screen, myfirstSquare, myfirstSquare.color)
        drawSquare(screen, mysecondSquare, mysecondSquare.color)
        drawSquare(screen, mythirdSquare, mythirdSquare.color)
        drawSquare(screen, myfourthSquare, myfourthSquare.color)
        Queen = ChessPieces('Assets\Pieces/blackQueen.png', (910, 30), 'BlackQueen', 0, blackside)
        Rook = ChessPieces('Assets\Pieces/blackRook.png', (910, 100), 'BlackRook', 0, blackside)
        Bishop = ChessPieces('Assets\Pieces/blackBishop.png', (910, 170), 'BlackBishop', 0, blackside)
        Knight = ChessPieces('Assets\Pieces/blackKnight.png', (910, 240), 'BlackKnight', 0, blackside)
        myfirstSquare.addPieces(Queen)
        mysecondSquare.addPieces(Rook)
        mythirdSquare.addPieces(Bishop)
        myfourthSquare.addPieces(Knight)
        screen.blit(Knight.image, Knight.rect)
        screen.blit(Bishop.image, Bishop.rect)
        screen.blit(Rook.image, Rook.rect)
        screen.blit(Queen.image, Queen.rect)
        return [myfirstSquare,mysecondSquare,mythirdSquare,myfourthSquare]
def animation(squarelist,screen,firstlocation,secondlocation,myPiece):
    firstx = firstlocation[0]
    firsty = firstlocation[1]
    secondx = secondlocation[0]
    secondy = secondlocation[1]
    differencex = secondx - firstx
    differencey = secondy - firsty
    for i in range(100):
        movementx = differencex/100 *i
        movementy = differencey/100 *i
        pygame.time.delay(1)
        myPiece.addlocation((firstx + movementx,firsty + movementy))
        for i in range(8):
            for j in range(8):
                newSquare = squarelist[i][j]
                drawSquare(screen, newSquare, newSquare.color)
        drawPieces(screen, squarelist)
        screen.blit(myPiece.image,(firstx + movementx,firsty + movementy))
        pygame.display.update()