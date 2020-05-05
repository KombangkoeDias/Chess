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
def checkPosition(move):
    if (move[0] > -1 and move[0] < 8 and move[1] > -1 and move[1] < 8):
        return True
    else:
        return False
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
def KnightMoves(Squarelist,a,b,walkresult,eatresult,type):
    allmoves = list()
    moves = list()
    move1 = (a-2,b-1)
    move2 = (a-2,b+1)
    move3 = (a-1,b+2)
    move4 = (a+1,b+2)
    move5 = (a+2,b+1)
    move6 = (a+2,b-1)
    move7 = (a+1,b-2)
    move8 = (a-1,b-2)
    allmoves.append(move1)
    allmoves.append(move2)
    allmoves.append(move3)
    allmoves.append(move4)
    allmoves.append(move5)
    allmoves.append(move6)
    allmoves.append(move7)
    allmoves.append(move8)
    for move in allmoves:
        if checkPosition(move):
            moves.append(move)
    for validmove in moves:
        i = validmove[0]
        j = validmove[1]
        if (Squarelist[i][j].Piece.type == Empty):
            walkresult.append(Squarelist[i][j])
        if (type == KnightW and Squarelist[i][j].Piece.type in BlackList):
            eatresult.append(Squarelist[i][j])
        if (type == KnightB and Squarelist[i][j].Piece.type in WhiteList):
            eatresult.append(Squarelist[i][j])
    return (walkresult,eatresult)