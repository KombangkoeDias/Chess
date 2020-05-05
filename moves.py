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
import pygame
def WhitePawnMoves(Squarelist,a,b,walkresult,eatresult):
    if (a == 6):
        if (Squarelist[a - 1][b].Piece.type == Empty):
            walkresult.append(Squarelist[a - 1][b])
        if (Squarelist[a - 2][b].Piece.type == Empty):
            walkresult.append(Squarelist[a - 2][b])
        if (b-1 > -1 and Squarelist[a - 1][b - 1].Piece.type in BlackList):
            eatresult.append(Squarelist[a - 1][b - 1])
        if (b+1 < 8 and Squarelist[a - 1][b + 1].Piece.type in BlackList):
            eatresult.append(Squarelist[a - 1][b + 1])
    elif (a < 7 and a > 0):
        if (Squarelist[a - 1][b].Piece.type == Empty):
            walkresult.append(Squarelist[a - 1][b])
        if (b-1 > -1 and Squarelist[a - 1][b - 1].Piece.type in BlackList):
            eatresult.append(Squarelist[a-1][b-1])
        if (b+1 < 8 and Squarelist[a - 1][b + 1].Piece.type in BlackList):
            eatresult.append(Squarelist[a - 1][b + 1])
    return (walkresult,eatresult)
def BlackPawnMoves(Squarelist,a,b,walkresult,eatresult):
    if (a == 1):
        if (Squarelist[a + 1][b].Piece.type == Empty):
            walkresult.append(Squarelist[a + 1][b])
        if (Squarelist[a + 2][b].Piece.type == Empty):
            walkresult.append(Squarelist[a + 2][b])
        if (b-1 > -1 and Squarelist[a + 1][b - 1].Piece.type in BlackList):
            eatresult.append(Squarelist[a + 1][b - 1])
        if (b+1 < 8 and Squarelist[a + 1][b + 1].Piece.type in BlackList):
            eatresult.append(Squarelist[a + 1][b + 1])
    elif (a > 1 and a < 7):
        if (Squarelist[a + 1][b].Piece.type == Empty):
            walkresult.append(Squarelist[a + 1][b])
        if (b - 1 > -1 and Squarelist[a + 1][b - 1].Piece.type in BlackList):
            eatresult.append(Squarelist[a + 1][b-1])
        if (b + 1 < 8 and Squarelist[a + 1][b + 1].Piece.type in BlackList):
            eatresult.append(Squarelist[a + 1][b + 1])
    return (walkresult,eatresult)