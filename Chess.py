import pygame

from Event import startGame,drawmovesline,drawChoose,animation
from Button import button
from Background import BackgroundPhoto
from square import drawSquare, Square , PawnW, PawnB, KnightW, KnightB, BishopW, BishopB, KingW, KingB, QueenW, QueenB,Empty,RookW,RookB,evaluateCheck,findSquarePosition,evaluatelose
from Piece import ChessPieces, DrawPieces
noside = ''
pygame.init()
whiteside = 'White'
blackside = 'Black'

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (128,0,0)
black = (0,0,0)
gold = (255,215,0)
vegasgold = (197,179,88)
tomago = (255,99,71)
darkgreen = (0,100,0)
yellow = (255,255,0)
orange = (255, 165, 0)
purple = (128,0,128)
lightblue = (173, 216, 230)

Width = 1000
Height = 600

Background = BackgroundPhoto('Assets\Chessbackground.png',[0,0])
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption('Chess Game')

font = pygame.font.Font('freesansbold.ttf', 70)
Arialfont = pygame.font.Font('freesansbold.ttf',70)

text = font.render('Welcome to Chess Game ', True, blue)
Startplaying = Arialfont.render('Want to start playing? ', True, blue)

textRect = text.get_rect()
textRect.center = (Width // 2, 80)

startRect = Startplaying.get_rect()
startRect.center = (Width // 2, 180)

clock = pygame.time.Clock()

def game_intro():
    intro = True
    while intro:
        screen.blit(Background.image, Background.rect)
        screen.blit(text, textRect)
        screen.blit(Startplaying, startRect)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        intro = button(screen, "Start", Width // 2 - 100, Height // 2 + 50, 150, 40, vegasgold, gold, startGame)
        button(screen,"Quit",Width//2-100,Height//2+120,150,40,red,tomago,quit)
        pygame.display.update()
# infinite loop

GameplayBackground = BackgroundPhoto('Assets\Horses.jpg',[0,0])

WhitePawn = list()
WhiteKnight = list()
WhiteBishop = list()
WhiteRook = list()
WhiteKing = list()
WhiteQueen = list()

BlackPawn = list()
BlackKnight = list()
BlackBishop = list()
BlackRook = list()
BlackKing = list()
BlackQueen = list()

Squarelist = list()
for i in range(8):
    mylist = list()
    Squarelist.append(mylist)
def blackposition(i):
    return (230+70*i, 40)
def whiteposition(i):
    return (230+70*i, 530)

for i in range(8):
    WhitePawn.append((230+70*i, 460))
    BlackPawn.append((230+70*i, 110))

for i in range(8):
    if (i == 0 or i == 7):
        WhiteRook.append(whiteposition(i))
        BlackRook.append(blackposition(i))
    elif (i == 1 or i == 6):
        WhiteKnight.append(whiteposition(i))
        BlackKnight.append(blackposition(i))
    elif (i == 2 or i == 5):
        WhiteBishop.append(whiteposition(i))
        BlackBishop.append(blackposition(i))
    elif (i == 3):
        WhiteQueen.append(whiteposition(i))
        BlackQueen.append(blackposition(i))
    else:
        WhiteKing.append(whiteposition(i))
        BlackKing.append(blackposition(i))

def drawPieces():
    for i in range(8):
        for j in range(8):
            newSquare = Squarelist[i][j]
            if (Squarelist[i][j].Piece.type != Empty):
                   DrawPieces(screen,newSquare)
def start_game():
    gamePlay = True
    screen.blit(GameplayBackground.image, GameplayBackground.rect)
    walkresult = list()
    eatresult = list()
    turn = 0
    before = None
    lastmove = None
    for i in range(8):
        for j in range(8):
            """
            if ((i+j) %2 ==0):
                newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, white)
                piecelocation = (newSquare.x + 10, newSquare.y + 10)
                newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation,Empty,None,noside))
            else:
                newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, darkgreen)
                piecelocation = (newSquare.x + 10, newSquare.y + 10)
                newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation,Empty,None,noside))
            if (i == 4 and j == 4):
                newSquare.addPieces(ChessPieces('Assets\Pieces/blackQueen.png', piecelocation, QueenB, 0, blackside))
            if (i == 4 and j == 7):
                newSquare.addPieces(ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation, KnightW, 1, whiteside))
            if (i == 3 and j == 3):
                newSquare.addPieces(ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation, BishopW, 1, whiteside))
            #if (i == 4 and j == 2):
                #newSquare.addPieces(ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation, KnightW, 0, whiteside))
            if (i == 6 and j == 3):
                newSquare.addPieces(ChessPieces('Assets\Pieces\whiteKing.png', piecelocation, KingW, 0, whiteside))
            if (i == 6 and j == 4):
                newSquare.addPieces(ChessPieces('Assets/Pieces/blackBishop.png', piecelocation, BishopB, 0, blackside))
            #if (i == 5 and j == 5):
                #newSquare.addPieces(ChessPieces('Assets/Pieces/blackKnight.png', piecelocation, KnightB, 1, blackside))
            if (i == 6 and j == 1):
                newSquare.addPieces(ChessPieces('Assets\Pieces/blackKing.png', piecelocation, KingB, 0, blackside))
            if (i == 1 and j == 5):
                newSquare.addPieces(ChessPieces('Assets/Pieces/blackRook.png', piecelocation, RookB, 0, blackside))
            if (i == 3 and j == 4):
                newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, PawnW, j, whiteside))
            if (i == 6 and j == 5):
                newSquare.addPieces(ChessPieces('Assets/Pieces/blackPawn.png', piecelocation, PawnB, j, blackside))
            Squarelist[i].append(newSquare)
            """
            if ((i + j) % 2 == 0):
                newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, white)
                piecelocation = (newSquare.x + 10, newSquare.y + 10)
                newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation,Empty,None,noside))
                if (i == 1):
                    newSquare.addPieces(ChessPieces('Assets/Pieces/blackPawn.png',piecelocation ,PawnB,j,blackside))
                if (i == 0):
                    if (j == 0):
                        newSquare.addPieces(ChessPieces('Assets/Pieces/blackRook.png',piecelocation ,RookB,0,blackside))
                    if (j == 2):
                        newSquare.addPieces(ChessPieces('Assets/Pieces/blackBishop.png', piecelocation ,BishopB,0,blackside))
                    if (j == 4):
                        newSquare.addPieces(ChessPieces('Assets\Pieces/blackKing.png', piecelocation ,KingB,0,blackside))
                    if (j == 6):
                        newSquare.addPieces(ChessPieces('Assets/Pieces/blackKnight.png', piecelocation ,KnightB,1,blackside))
                if (i == 6):
                    newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation,PawnW,j,whiteside))
                if (i == 7):
                    if (j == 1):
                        newSquare.addPieces(ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation ,KnightW,0,whiteside))
                    if (j == 3):
                        newSquare.addPieces(ChessPieces('Assets\Pieces\whiteQueen.png', piecelocation ,QueenW,0,whiteside))
                    if (j == 5):
                        newSquare.addPieces(ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation ,BishopW,1,whiteside))
                    if (j == 7):
                        newSquare.addPieces(ChessPieces('Assets\Pieces\whiteRook.png', piecelocation ,RookW,1,whiteside))
                Squarelist[i].append(newSquare)
            else:
                newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, darkgreen)
                piecelocation = (newSquare.x + 10, newSquare.y + 10)
                newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation,Empty,None,noside))
                if (i == 1):
                    newSquare.addPieces(ChessPieces('Assets/Pieces/blackPawn.png',piecelocation ,PawnB,j,blackside))
                if (i == 0):
                    if (j == 1):
                        newSquare.addPieces(ChessPieces('Assets/Pieces/blackKnight.png', piecelocation ,KnightB,0,blackside))
                    if (j == 3):
                        newSquare.addPieces(ChessPieces('Assets\Pieces/blackQueen.png', piecelocation,QueenB,0,blackside))
                    if (j == 5):
                        newSquare.addPieces(ChessPieces('Assets/Pieces/blackBishop.png', piecelocation ,BishopB,1,blackside))
                    if (j == 7):
                        newSquare.addPieces(ChessPieces('Assets/Pieces/blackRook.png',piecelocation ,RookB,1,blackside))
                if (i == 6):
                    newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation,PawnW,j,whiteside))
                if (i == 7):
                    if (j == 0):
                        newSquare.addPieces(ChessPieces('Assets\Pieces\whiteRook.png', piecelocation ,RookW,0,whiteside))
                    if (j == 2):
                        newSquare.addPieces(ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation ,BishopW,0,whiteside))
                    if (j == 4):
                        newSquare.addPieces(ChessPieces('Assets\Pieces\whiteKing.png', piecelocation,KingW,0,whiteside))
                    if (j == 6):
                        newSquare.addPieces(ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation ,KnightW,1,whiteside))
                Squarelist[i].append(newSquare)

    chosen = (10, 10)
    click = list()
    firstSquare = None
    secondSquare = None
    position = None
    changeTurn = True
    #animate = False
    #firstPiece = None
    #secondPiece = None
    while gamePlay:
        screen.blit(GameplayBackground.image,GameplayBackground.rect)
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for i in range(8):
            for j in range(8):
                newSquare = Squarelist[i][j]
                if ((i + j) % 2 == 0):
                    drawSquare(screen, newSquare, newSquare.color)
                    if (len(click) ==1 and newSquare.getclick() and ((newSquare in walkresult) or (newSquare in eatresult))):
                        click.append(newSquare)
                        if (click[1].Piece.type == Empty):
                            print(click[0].Piece.type, click[0].Piece.order, "moves to", i, j)
                    elif (len(click) == 1 and newSquare.getclick()):
                        if (turn == 0 and newSquare.Piece.side == whiteside) or (turn == 1 and newSquare.Piece.side == blackside):
                            if (newSquare != click[0]):
                                click.clear()
                                click.append(newSquare)
                    elif (newSquare.getclick() and newSquare.Piece.type != 'Empty Space'):
                        if (len(click) == 0):
                            if (turn == 0 and newSquare.Piece.side == whiteside) or (turn == 1 and newSquare.Piece.side == blackside):
                                if (newSquare != lastmove):
                                    click.append(newSquare)
                                    # print(i,j)
                                    #print(newSquare.Piece.type,newSquare.Piece.order)


                    """
                    if (len(click) == 2 and newSquare.getclick() and ((newSquare in walkresult) or newSquare in eatresult)):
                        if (newSquare != click[1]):
                            click[1] = newSquare
                    """
                    #newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, white)
                    #Squarelist[i].append(newSquare)
                else:
                    drawSquare(screen,newSquare,newSquare.color)
                    if (len(click) ==1 and newSquare.getclick() and ((newSquare in walkresult) or (newSquare in eatresult))):
                        click.append(newSquare)
                        if (click[1].Piece.type == Empty):
                            print(click[0].Piece.type, click[0].Piece.order, "moves to", i, j)
                    elif (len(click) == 1 and newSquare.getclick()):
                        if (turn == 0 and newSquare.Piece.side == whiteside) or (turn == 1 and newSquare.Piece.side == blackside):
                            if (newSquare != click[0]):
                                click.clear()
                                click.append(newSquare)
                    elif (newSquare.getclick() and newSquare.Piece.type != 'Empty Space'):
                        if (len(click) == 0):
                            if (turn == 0 and newSquare.Piece.side == whiteside) or (turn == 1 and newSquare.Piece.side == blackside):
                                if (newSquare != lastmove):
                                    click.append(newSquare)
                                    # print(i,j)
                                    #print(newSquare.Piece.type, newSquare.Piece.order)
                    """
                    if (len(click) == 2 and newSquare.getclick() and ((newSquare in walkresult) or newSquare in eatresult)):
                        if (newSquare != click[1]):
                            click[1] = newSquare
                    """
                    #newSquare = Square(220 + 70 * i, 30 + 70 * j, 70, 70, darkgreen)
                    #Squarelist[i].append(newSquare)
        #print(len(click))
        if (len(click) == 1):
            selectedSquare = click[0]
            walkresult, eatresult = selectedSquare.evaluatepossiblemoves(Squarelist,(firstSquare,secondSquare))
            if (turn == 1):
                walkresult, eatresult = selectedSquare.checkPossibleMoves(Squarelist,walkresult,eatresult,blackside,(firstSquare,secondSquare))
            elif (turn == 0):
                walkresult, eatresult = selectedSquare.checkPossibleMoves(Squarelist,walkresult,eatresult,whiteside,(firstSquare,secondSquare))
            for walkSquare in walkresult:
                pygame.draw.circle(screen, green, (walkSquare.x + 35, walkSquare.y + 35), 7)
            for eatSquare in eatresult:
                drawSquare(screen, eatSquare, red)

        if (len(click) == 2):
            if (firstSquare != None and secondSquare != None):
                position = findSquarePosition(Squarelist,secondSquare)
                anotherSquare = click[1]
                anotherposition = findSquarePosition(Squarelist,anotherSquare)
                if (position[0]-1 == anotherposition[0] and position[1] == anotherposition[1] and turn == 0):
                    Squarelist[position[0]][position[1]].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png', (secondSquare.Piece.rect.left, secondSquare.Piece.rect.top), Empty,
                                    None,
                                    noside))
                if (position[0]+1 == anotherposition[0] and position[1] == anotherposition[1] and turn == 1):
                    Squarelist[position[0]][position[1]].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png',
                                    (secondSquare.Piece.rect.left, secondSquare.Piece.rect.top), Empty,
                                    None,
                                    noside))
            if (turn == 0 and click[0].Piece.side == whiteside):
                selectedSquare = click[0]
                for walkSquare in walkresult:
                    pygame.draw.circle(screen, green, (walkSquare.x + 35, walkSquare.y + 35), 7)
                for eatSquare in eatresult:
                    drawSquare(screen, eatSquare, red)
                drawSquare(screen, selectedSquare, orange)
                firstPiece = click[0].Piece
                secondPiece = click[1].Piece
                (firstpos1, firstpos2) = findSquarePosition(Squarelist, click[0])
                (secondpos1, secondpos2) = findSquarePosition(Squarelist, click[1])
                if (secondPiece.type != Empty):
                    print(firstPiece.type,firstPiece.order,'at',firstpos1,firstpos2,'eats',secondPiece.type,secondPiece.order,'at',secondpos1,secondpos2)


                Squarelist[firstpos1][firstpos2].addPieces(
                    ChessPieces('Assets\Pieces\whitePawn.png', (firstPiece.rect.left, firstPiece.rect.top), Empty, None,
                                noside))
                animation(Squarelist,screen,(firstPiece.rect.left, firstPiece.rect.top),(secondPiece.rect.left, secondPiece.rect.top),firstPiece)
                #animate = True
                Squarelist[secondpos1][secondpos2].addPieces(
                    ChessPieces(firstPiece.imagefile, (secondPiece.rect.left, secondPiece.rect.top), firstPiece.type,
                                firstPiece.order, firstPiece.side))


                before = click[0]
                if (changeTurn):
                    turn = 1
                else:
                    turn = 2
            if (turn == 1 and click[0].Piece.side == blackside):
                selectedSquare = click[0]
                for walkSquare in walkresult:
                    pygame.draw.circle(screen, green, (walkSquare.x + 35, walkSquare.y + 35), 7)
                for eatSquare in eatresult:
                    drawSquare(screen, eatSquare, red)
                drawSquare(screen, selectedSquare, orange)
                firstPiece = click[0].Piece
                secondPiece = click[1].Piece
                (firstpos1, firstpos2) = findSquarePosition(Squarelist, click[0])
                (secondpos1, secondpos2) = findSquarePosition(Squarelist, click[1])
                if (secondPiece.type != Empty):
                    print(firstPiece.type, firstPiece.order, 'at', firstpos1, firstpos2, 'eats', secondPiece.type,
                          secondPiece.order, 'at', secondpos1, secondpos2)
                Squarelist[firstpos1][firstpos2].addPieces(
                    ChessPieces('Assets\Pieces\whitePawn.png', (firstPiece.rect.left, firstPiece.rect.top), Empty, None,
                                noside))
                animation(Squarelist,screen,(firstPiece.rect.left, firstPiece.rect.top),(secondPiece.rect.left, secondPiece.rect.top),firstPiece)

                Squarelist[secondpos1][secondpos2].addPieces(
                    ChessPieces(firstPiece.imagefile, (secondPiece.rect.left, secondPiece.rect.top), firstPiece.type,
                                firstPiece.order, firstPiece.side))


                before = click[0]
                if (changeTurn):
                    turn = 0
                else:
                    turn = 2

            position = findSquarePosition(Squarelist, click[1])
                #print(position[0], position[1])
                #print(Squarelist[position[0]][position[1]].Piece.type)
            firstSquare = click[0]
            secondSquare = click[1]
            click.clear()
        if (position != None and position[0] == 0 and Squarelist[position[0]][position[1]].Piece.type == PawnW):
            changeTurn = False
            turn = 2
            #print('white in!')
            mylist = drawChoose(screen,whiteside)
            for chooseSquare in mylist:
                if chooseSquare.choose():
                    drawSquare(screen,chooseSquare,yellow)
                    screen.blit(chooseSquare.Piece.image,chooseSquare.Piece.rect)
                if chooseSquare.getclick():
                    Squarelist[position[0]][position[1]].addPieces(chooseSquare.Piece.addlocation((Squarelist[position[0]][position[1]].x+10,Squarelist[position[0]][position[1]].y+10)))
                    changeTurn = True
                    turn = 1
        elif (position != None and position[0] == 7 and Squarelist[position[0]][position[1]].Piece.type == PawnB):
            changeTurn = False
            turn = 2
            #print('black in!')
            mylist = drawChoose(screen,blackside)
            for chooseSquare in mylist:
                if chooseSquare.choose():
                    drawSquare(screen, chooseSquare, yellow)
                    screen.blit(chooseSquare.Piece.image, chooseSquare.Piece.rect)
                if chooseSquare.getclick():
                    Squarelist[position[0]][position[1]].addPieces(chooseSquare.Piece.addlocation(
                        (Squarelist[position[0]][position[1]].x + 10, Squarelist[position[0]][position[1]].y + 10)))
                    changeTurn = True
                    turn = 0
        #print(turn)
        #if (before != None):
            #pygame.draw.circle(screen, lightblue, (before.x + 35, before.y + 35), 7)
        check, first,second = evaluateCheck(Squarelist,whiteside,(firstSquare,secondSquare))
        if check:
            drawSquare(screen,Squarelist[first][second],purple)
            if evaluatelose(Squarelist, whiteside,(firstSquare,secondSquare)):
                print('White loses')
        check,first,second = evaluateCheck(Squarelist,blackside,(firstSquare,secondSquare))
        if check:
            drawSquare(screen,Squarelist[first][second],purple)
            if evaluatelose(Squarelist,blackside,(firstSquare,secondSquare)):
                print('Black loses')
        if (len(click) == 1):
            selectedSquare = click[0]
            drawSquare(screen, selectedSquare, orange)
        #if evaluatelose(Squarelist,whiteside):
            #print('White loses')
        #if evaluatelose(Squarelist,blackside):
            #print('Black loses')
        for i in range(8):
            for j in range(8):
                newSquare = Squarelist[i][j]
                if (newSquare.choose()):
                    chosen = (i, j)
                    if (len(click) != 0):
                        if (newSquare != click[0]):
                            drawSquare(screen, newSquare, yellow)
                    else:
                        drawSquare(screen,newSquare,yellow)
        if (firstSquare != None and secondSquare != None):
            drawmovesline(screen,firstSquare,secondSquare,lightblue,5)
        drawPieces()
        pygame.display.update()

game_intro()
start_game()

