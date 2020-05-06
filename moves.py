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
def BishopMoves(Squarelist,a,b,walkresult,eatresult,side):
    i = 1
    while(checkPosition((a+i,b+i))):
        first = a+i
        second = b+i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i+=1
    i = 1
    while(checkPosition((a+i,b-i))):
        first = a+i
        second = b-i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i+=1
    i = 1
    while(checkPosition((a-i,b+i))):
        first = a-i
        second = b+i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i+=1
    i = 1
    while(checkPosition((a-i,b-i))):
        first = a-i
        second = b-i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i+=1
    return (walkresult,eatresult)
def RookMoves(Squarelist,a,b,walkresult,eatresult,side):
    i = 1
    while (checkPosition((a + i, b))):
        first = a + i
        second = b
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a - i, b))):
        first = a - i
        second = b
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a , b + i))):
        first = a
        second = b + i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a, b - i))):
        first = a
        second = b - i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    return (walkresult, eatresult)
def QueenMoves(Squarelist,a,b,walkresult,eatresult,side):
    i = 1
    while (checkPosition((a + i, b + i))):
        first = a + i
        second = b + i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a + i, b - i))):
        first = a + i
        second = b - i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a - i, b + i))):
        first = a - i
        second = b + i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a - i, b - i))):
        first = a - i
        second = b - i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a + i, b))):
        first = a + i
        second = b
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a - i, b))):
        first = a - i
        second = b
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a, b + i))):
        first = a
        second = b + i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    i = 1
    while (checkPosition((a, b - i))):
        first = a
        second = b - i
        if (Squarelist[first][second].Piece.type != Empty):
            if (side != Squarelist[first][second].Piece.side and Squarelist[first][second].Piece.side != noside):
                eatresult.append(Squarelist[first][second])
            break
        walkresult.append(Squarelist[first][second])
        i += 1
    return (walkresult, eatresult)
def KingMoves(Squarelist,a,b,walkresult,eatresult,side):
    eightmoves = [(a-1,b-1),(a-1,b),(a-1,b+1),(a,b-1),(a,b+1),(a+1,b-1),(a+1,b),(a+1,b+1)]
    for move in eightmoves:
        first = move[0]
        second = move[1]
        if (checkPosition(move)):
            if (Squarelist[first][second].Piece.type != Empty):
                if (side != Squarelist[first][second].Piece.side):
                    newSquarelist = list(Squarelist)
                    mytype = Squarelist[first][second].Piece.type
                    newSquarelist[first][second].Piece.type = Empty
                    check = 0
                    for i in range(8):
                        for j in range(8):
                            if (newSquarelist[i][j].Piece.side != newSquarelist[a][b].Piece.side and newSquarelist[i][j].Piece.type != KingW and newSquarelist[i][j].Piece.type != KingB):
                                walkmove, eatmove = newSquarelist[i][j].evaluatepossiblemoves(Squarelist)
                                if (Squarelist[first][second] in walkmove or Squarelist[first][second] in eatmove):
                                    check = 1

                    eightadjacentmoves = [(first - 1, second - 1), (first - 1, second), (first - 1, second + 1),
                                          (first, second - 1), (first, second + 1), (first + 1, second - 1),
                                          (first + 1, second), (first + 1, second + 1)]
                    for adjacentmove in eightadjacentmoves:
                        if (checkPosition(adjacentmove)):
                            adjacentfirst = adjacentmove[0]
                            adjacentsecond = adjacentmove[1]
                            if side == whiteside:
                                if (Squarelist[adjacentfirst][adjacentsecond].Piece.side != side and
                                        Squarelist[adjacentfirst][adjacentsecond].Piece.type == KingB):
                                    check = 1
                            if side == blackside:
                                if (Squarelist[adjacentfirst][adjacentsecond].Piece.side != side and
                                        Squarelist[adjacentfirst][adjacentsecond].Piece.type == KingW):
                                    check = 1
                    if (check == 0):
                        eatresult.append(Squarelist[first][second])
                    newSquarelist[first][second].Piece.type = mytype
            else:
                check = 0
                for i in range(8):
                    for j in range(8):
                        if (Squarelist[i][j].Piece.side != Squarelist[a][b].Piece.side and Squarelist[i][j].Piece.type != KingW and Squarelist[i][j].Piece.type != KingB):
                            walkmove, eatmove = Squarelist[i][j].evaluatepossiblemoves(Squarelist)
                            if (Squarelist[first][second] in walkmove or Squarelist[first][second] in eatmove):
                                check = 1
                eightadjacentmoves = [(first - 1, second - 1), (first - 1, second), (first- 1, second + 1), (first, second - 1), (first, second + 1), (first + 1, second - 1),
                              (first + 1, second), (first + 1, second + 1)]
                for adjacentmove in eightadjacentmoves:
                    if (checkPosition(adjacentmove)):
                        adjacentfirst = adjacentmove[0]
                        adjacentsecond = adjacentmove[1]
                        if side == whiteside:
                            if (Squarelist[adjacentfirst][adjacentsecond].Piece.side != side and Squarelist[adjacentfirst][adjacentsecond].Piece.type == KingB):
                                check = 1
                        if side == blackside:
                            if (Squarelist[adjacentfirst][adjacentsecond].Piece.side != side and Squarelist[adjacentfirst][adjacentsecond].Piece.type == KingW):
                                check = 1
                if (check == 0):
                    walkresult.append(Squarelist[first][second])
    return (walkresult,eatresult)