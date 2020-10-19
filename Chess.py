import pygame
"""
Chess Game Github : Kombangkoe Dias
"""
from Event import drawmovesline,drawChoose,animation
from Button import button
from Background import BackgroundPhoto
from square import drawSquare, Square , PawnW, PawnB, KnightW, KnightB, BishopW, BishopB, KingW, KingB, QueenW, QueenB,Empty,RookW,RookB,evaluateCheck,findSquarePosition,evaluatelose
from Piece import ChessPieces, DrawPieces
from moves import checkPosition
noside = ''
pygame.init() # initiate the pygame library
whiteside = 'White'  # string used to differentiate between white piece and black piece
blackside = 'Black'  # string used to differentiate between white piece and black piece

# colors used in the game.
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

# screen width and height
Width = 1000
Height = 600

# visions of the game's first screen.
Background = BackgroundPhoto('Assets\Chessbackground.png',[0,0])
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption('Chess Game')

font = pygame.font.Font('freesansbold.ttf', 70)
Arialfont = pygame.font.Font('freesansbold.ttf',70)
newfont = pygame.font.Font('freesansbold.ttf',30)

text = font.render('Welcome to Chess Game ', True, blue)
Startplaying = Arialfont.render('Want to start playing? ', True, blue)

whiteWinText = newfont.render('White wins',True,black)
whiteRect = whiteWinText.get_rect()
whiteRect.center = (Width//2, 310)

blackWinText = newfont.render('Black wins',True,white)
blackRect = blackWinText.get_rect()
blackRect.center = (Width//2,310)

textRect = text.get_rect()
textRect.center = (Width // 2, 80)

startRect = Startplaying.get_rect()
startRect.center = (Width // 2, 180)

clock = pygame.time.Clock()



def game_intro():
    intro = True
    # when the player doesn't click start intro will still be true.
    while intro:
        screen.blit(Background.image, Background.rect)  # draw background.
        screen.blit(text, textRect)  # draw the first text.
        screen.blit(Startplaying, startRect)  # draw the second text.
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:  # quit event.
                pygame.quit()
                quit()
        button(screen, "Start", Width // 2 - 100, Height // 2 + 50, 150, 40, vegasgold, gold, start_game)  # draw the start button.
        button(screen,"Quit",Width//2-100,Height//2+120,150,40,red,tomago,quit) # draw the quit button.
        pygame.display.update()  # update the screen every cycle for hover effects on button.

GameplayBackground = BackgroundPhoto('Assets\Horses.jpg',[0,0])

Squarelist = list()  # list contains all square object on the board.

def drawPieces():
    global Squarelist
    # iterate through all squares.
    for i in range(8):
        for j in range(8):
            newSquare = Squarelist[i][j]  # look at the current square.
            if (Squarelist[i][j].Piece.type != Empty):  # if the position should have piece then draw it.
                   DrawPieces(screen,newSquare)

def setBoard():
    Squarelist.clear()
    for i in range(8):
        mylist = list()
        Squarelist.append(mylist)
    for i in range(8):
        for j in range(8):
            if ((i + j) % 2 == 0):
                newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, white)
                piecelocation = (newSquare.x + 10, newSquare.y + 10)
                newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, Empty, None, noside))
                if (i == 1):
                    newSquare.addPieces(ChessPieces('Assets/Pieces/blackPawn.png', piecelocation, PawnB, j, blackside))
                if (i == 0):
                    if (j == 0):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackRook.png', piecelocation, RookB, 0, blackside))
                    if (j == 2):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackBishop.png', piecelocation, BishopB, 0, blackside))
                    if (j == 4):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces/blackKing.png', piecelocation, KingB, 0, blackside))
                    if (j == 6):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackKnight.png', piecelocation, KnightB, 1, blackside))
                if (i == 6):
                    newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, PawnW, j, whiteside))
                if (i == 7):
                    if (j == 1):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation, KnightW, 0, whiteside))
                    if (j == 3):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whiteQueen.png', piecelocation, QueenW, 0, whiteside))
                    if (j == 5):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation, BishopW, 1, whiteside))
                    if (j == 7):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whiteRook.png', piecelocation, RookW, 1, whiteside))
                Squarelist[i].append(newSquare)
            else:
                newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, lightblue)
                piecelocation = (newSquare.x + 10, newSquare.y + 10)
                newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, Empty, None, noside))
                if (i == 1):
                    newSquare.addPieces(ChessPieces('Assets/Pieces/blackPawn.png', piecelocation, PawnB, j, blackside))
                if (i == 0):
                    if (j == 1):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackKnight.png', piecelocation, KnightB, 0, blackside))
                    if (j == 3):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces/blackQueen.png', piecelocation, QueenB, 0, blackside))
                    if (j == 5):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackBishop.png', piecelocation, BishopB, 1, blackside))
                    if (j == 7):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackRook.png', piecelocation, RookB, 1, blackside))
                if (i == 6):
                    newSquare.addPieces(ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, PawnW, j, whiteside))
                if (i == 7):
                    if (j == 0):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whiteRook.png', piecelocation, RookW, 0, whiteside))
                    if (j == 2):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation, BishopW, 0, whiteside))
                    if (j == 4):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whiteKing.png', piecelocation, KingW, 0, whiteside))
                    if (j == 6):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation, KnightW, 1, whiteside))
                Squarelist[i].append(newSquare)

def start_game():
    print("Starting the game now!")
    global Squarelist
    blackWin = False
    whiteWin = False
    gamePlay = True
    screen.blit(GameplayBackground.image, GameplayBackground.rect)
    walkresult = list()
    eatresult = list()
    turn = 0
    before = None
    lastmove = None
    fiftycheck = 0
    blackthreemovelist = list()
    whitethreemovelist = list()

    setBoard()

    click = list()
    firstSquare = None
    secondSquare = None
    position = None
    changeTurn = True
    whitekingMove = False
    blackkingMove = False
    whiterook0move = False
    whiterook1move = False
    blackrook0move = False
    blackrook1move = False

    time = 0
    listOfSquareList = list()

    def goBack():
        print('go back run!')

    while gamePlay:
        whiterookmove = (whiterook0move,whiterook1move)
        blackrookmove = (blackrook0move,blackrook1move)
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
            if (turn == 1):
                walkresult, eatresult = selectedSquare.evaluatepossiblemoves(Squarelist, (firstSquare, secondSquare),blackkingMove)
                walkresult, eatresult = selectedSquare.checkPossibleMoves(Squarelist,walkresult,eatresult,blackside,(firstSquare,secondSquare),blackkingMove)
            elif (turn == 0):
                walkresult, eatresult = selectedSquare.evaluatepossiblemoves(Squarelist, (firstSquare, secondSquare),whitekingMove)
                walkresult, eatresult = selectedSquare.checkPossibleMoves(Squarelist,walkresult,eatresult,whiteside,(firstSquare,secondSquare),whitekingMove)
            if (click[0].Piece.type == KingW):
                if (whiterook0move):
                    if (Squarelist[7][2] in walkresult):
                        walkresult.remove(Squarelist[7][2])
                if (whiterook1move):
                    if (Squarelist[7][6] in walkresult):
                        walkresult.remove(Squarelist[7][6])


                for walk in walkresult:
                    (i, j) = findSquarePosition(Squarelist,walk)
                    eightmoves = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1),
                                  (i + 1, j - 1),
                                  (i + 1, j), (i + 1, j + 1)]
                    for position in eightmoves:
                        if (checkPosition(position)):
                            if (Squarelist[position[0]][position[1]].Piece.type == KingB):
                                walkresult.remove(walk)

            if (click[0].Piece.type == KingB):
                if (blackrook0move):
                    if (Squarelist[0][2] in walkresult):
                        walkresult.remove(Squarelist[0][2])
                    if (Squarelist[0][6] in walkresult):
                        walkresult.remove(Squarelist[0][6])
                for walk in walkresult:
                    (i, j) = findSquarePosition(Squarelist, walk)
                    eightmoves = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1),
                                  (i + 1, j - 1),
                                  (i + 1, j), (i + 1, j + 1)]
                    for position in eightmoves:
                        if (checkPosition(position)):
                            if (Squarelist[position[0]][position[1]].Piece.type == KingW):
                                walkresult.remove(walk)
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
                    fiftycheck = 0
                    #print(fiftycheck)
                else:
                    if (firstPiece.type == PawnW):
                        fiftycheck = 0
                    else:
                        fiftycheck += 1
                    #print(fiftycheck)
                if (len(whitethreemovelist) < 6):
                    whitethreemovelist.append((secondpos1,secondpos2))
                    print(whitethreemovelist)
                else:
                    for i in range(5):
                        whitethreemovelist[i] = whitethreemovelist[i + 1]
                    whitethreemovelist.pop(5)
                    whitethreemovelist.append((secondpos1,secondpos2))
                    print(whitethreemovelist)
                if (click[0].Piece.type == KingW):
                    whitekingMove = True
                if (click[0].Piece.type == RookW and click[0].Piece.order == 0):
                    whiterook0move = True
                    #print("whiterook0 moves")
                if (click[0].Piece.type == RookW and click[0].Piece.order == 1):
                    whiterook1move = True
                    #print("whiterook1 moves")
                if (click[0].Piece.type == KingW and findSquarePosition(Squarelist,click[0]) == (7,4) and findSquarePosition(Squarelist,click[1]) == (7,6) and not whiterook1move
                    and Squarelist[7][7].Piece.type == RookW and Squarelist[7][7].Piece.order == 1):
                    Squarelist[7][4].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png', (firstPiece.rect.left, firstPiece.rect.top), Empty,
                                    None,
                                    noside))
                    animation(Squarelist,screen,(firstPiece.rect.left, firstPiece.rect.top),(Squarelist[7][6].Piece.rect.left,Squarelist[7][6].Piece.rect.top),firstPiece)
                    Squarelist[7][6].addPieces(
                        ChessPieces(firstPiece.imagefile, (secondPiece.rect.left, secondPiece.rect.top),
                                    firstPiece.type,
                                    firstPiece.order, firstPiece.side))
                    Squarelist[7][5].addPieces(ChessPieces(Squarelist[7][7].Piece.imagefile, (
                    Squarelist[7][5].Piece.rect.left, Squarelist[7][5].Piece.rect.top), Squarelist[7][7].Piece.type,
                                                           Squarelist[7][7].Piece.order, Squarelist[7][7].Piece.side))
                    Squarelist[7][7].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png',
                                    (Squarelist[7][7].Piece.rect.left, Squarelist[7][7].Piece.rect.top), Empty, None,
                                    noside))
                elif (click[0].Piece.type == KingW and findSquarePosition(Squarelist,click[0]) == (7,4) and findSquarePosition(Squarelist,click[1]) == (7,2) and not whiterook0move
                    and Squarelist[7][0].Piece.type == RookW and Squarelist[7][0].Piece.order == 0):
                    Squarelist[7][4].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png', (firstPiece.rect.left, firstPiece.rect.top), Empty,
                                    None,
                                    noside))
                    animation(Squarelist, screen, (firstPiece.rect.left, firstPiece.rect.top),
                              (Squarelist[7][2].Piece.rect.left, Squarelist[7][2].Piece.rect.top), firstPiece)
                    Squarelist[7][2].addPieces(
                        ChessPieces(firstPiece.imagefile, (secondPiece.rect.left, secondPiece.rect.top),
                                    firstPiece.type,
                                    firstPiece.order, firstPiece.side))
                    Squarelist[7][3].addPieces(ChessPieces(Squarelist[7][0].Piece.imagefile, (
                        Squarelist[7][3].Piece.rect.left, Squarelist[7][3].Piece.rect.top), Squarelist[7][0].Piece.type,
                                                           Squarelist[7][0].Piece.order, Squarelist[7][0].Piece.side))
                    Squarelist[7][0].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png',
                                    (Squarelist[0][0].Piece.rect.left, Squarelist[0][0].Piece.rect.top), Empty, None,
                                    noside))
                else:
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
                    fiftycheck = 0
                    #print(fiftycheck)
                else:
                    if (firstPiece.type == PawnB):
                        fiftycheck = 0
                    else:
                        fiftycheck += 1
                    #print(fiftycheck)
                if (len(blackthreemovelist) < 6):
                    blackthreemovelist.append((secondpos1,secondpos2))
                    print(blackthreemovelist)
                else:
                    for i in range(5):
                        blackthreemovelist[i] = blackthreemovelist[i+1]
                    blackthreemovelist.pop(5)
                    blackthreemovelist.append((secondpos1,secondpos2))
                    print(blackthreemovelist)
                if (click[0].Piece.type == KingB):
                    blackkingMove = True
                if (click[0].Piece.type == RookB and click[0].Piece.order == 0):
                    blackrook0move = True
                    print("blackrook0 moves")

                if (click[0].Piece.type == RookB and click[0].Piece.order == 1):
                    blackrook1move = True
                    print("blackrook1 moves")

                if (click[0].Piece.type == KingB and findSquarePosition(Squarelist,click[0]) == (0,4) and findSquarePosition(Squarelist,click[1]) == (0,6) and not blackrook1move
                    and Squarelist[0][7].Piece.type == RookB and Squarelist[0][7].Piece.order == 1):
                    Squarelist[0][4].addPieces(ChessPieces('Assets\Pieces\whitePawn.png', (firstPiece.rect.left, firstPiece.rect.top), Empty, None,
                                noside))
                    animation(Squarelist,screen,(firstPiece.rect.left, firstPiece.rect.top),(Squarelist[0][6].Piece.rect.left,Squarelist[0][6].Piece.rect.top),firstPiece)
                    Squarelist[0][6].addPieces(ChessPieces(firstPiece.imagefile, (secondPiece.rect.left, secondPiece.rect.top), firstPiece.type,
                                firstPiece.order, firstPiece.side))
                    Squarelist[0][5].addPieces(ChessPieces(Squarelist[0][7].Piece.imagefile,(Squarelist[0][5].Piece.rect.left,Squarelist[0][5].Piece.rect.top), Squarelist[0][7].Piece.type,
                                               Squarelist[0][7].Piece.order,Squarelist[0][7].Piece.side))
                    #print(Squarelist[0][7].Piece.type)
                    Squarelist[0][7].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png', (Squarelist[0][7].Piece.rect.left, Squarelist[0][7].Piece.rect.top), Empty,None,noside))

                elif (click[0].Piece.type == KingB and findSquarePosition(Squarelist,click[0]) == (0,4) and findSquarePosition(Squarelist,click[1]) == (0,2) and not blackrook0move
                    and Squarelist[0][0].Piece.type == RookB and Squarelist[0][0].Piece.order == 0):
                    Squarelist[0][4].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png', (firstPiece.rect.left, firstPiece.rect.top), Empty,
                                    None,
                                    noside))
                    animation(Squarelist, screen, (firstPiece.rect.left, firstPiece.rect.top),
                              (Squarelist[0][2].Piece.rect.left, Squarelist[0][2].Piece.rect.top), firstPiece)
                    Squarelist[0][2].addPieces(
                        ChessPieces(firstPiece.imagefile, (secondPiece.rect.left, secondPiece.rect.top),
                                    firstPiece.type,
                                    firstPiece.order, firstPiece.side))
                    Squarelist[0][3].addPieces(ChessPieces(Squarelist[0][0].Piece.imagefile, (
                        Squarelist[0][3].Piece.rect.left, Squarelist[0][3].Piece.rect.top), Squarelist[0][0].Piece.type,
                                                           Squarelist[0][0].Piece.order, Squarelist[0][0].Piece.side))
                    Squarelist[0][0].addPieces(
                        ChessPieces('Assets\Pieces\whitePawn.png',
                                    (Squarelist[0][0].Piece.rect.left, Squarelist[0][0].Piece.rect.top), Empty, None,
                                    noside))
                else:
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

            newSquareListTest = Squarelist.copy()

            listOfSquareList.append(newSquareListTest)
            time += 1
            print(time)

            click.clear()
        #check for pawn reach the end(to turn in to queen)
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
        whiteavailablemoves = 0
        blackavailablemoves = 0
        for i in range(8):
            for j in range(8):
                if (turn == 1 and Squarelist[i][j].Piece.side == blackside):
                    #print('in1')
                    walk,move = Squarelist[i][j].evaluatepossiblemoves(Squarelist,(firstSquare,secondSquare),blackkingMove)
                    blackavailablemoves += len(walk)
                    blackavailablemoves += len(move)
                if (turn == 0 and Squarelist[i][j].Piece.side == whiteside):
                    #print('in0')
                    walk,move = Squarelist[i][j].evaluatepossiblemoves(Squarelist,(firstSquare,secondSquare),whitekingMove)
                    whiteavailablemoves += len(walk)
                    whiteavailablemoves += len(move)

        #print(whiteavailablemoves,blackavailablemoves)
        if (whiteavailablemoves == 0 and turn == 0):
            check,i,j = evaluateCheck(Squarelist,whiteside,(firstSquare,secondSquare),whitekingMove)
            if (not check):
                print('draw because white has no moves left')
                turn = 3 #stalemate
        elif (blackavailablemoves == 0 and turn == 1):
            check,i,j = evaluateCheck(Squarelist,blackside,(firstSquare,secondSquare),blackkingMove)
            if (not check):
                print('draw because black has no moves left')
                turn = 3 #stalemate

        if (fiftycheck == 50):
            print('draw because no moves occur for 50 turns') # the fifty-move rule
            turn = 3
        if (len(whitethreemovelist) == 6 and len(blackthreemovelist) == 6 and turn < 2):
            if ((whitethreemovelist[0] == whitethreemovelist[2] == whitethreemovelist[4] and whitethreemovelist[1]
                    == whitethreemovelist[3] == whitethreemovelist[5]) or (blackthreemovelist[0] == blackthreemovelist[2]
                    == blackthreemovelist[4] and blackthreemovelist[1] == blackthreemovelist[3] == blackthreemovelist[5])):
                print('draw because same moves for 3 times') # threefold repetition
                turn = 3
        check, first,second = evaluateCheck(Squarelist,whiteside,(firstSquare,secondSquare),whitekingMove)
        if check:
            drawSquare(screen,Squarelist[first][second],purple)
            if evaluatelose(Squarelist, whiteside,(firstSquare,secondSquare),whitekingMove):
                print('Black wins')
                turn = 2
                blackWin = True

        check,first,second = evaluateCheck(Squarelist,blackside,(firstSquare,secondSquare),blackkingMove)
        if check:
            drawSquare(screen,Squarelist[first][second],purple)
            if evaluatelose(Squarelist,blackside,(firstSquare,secondSquare),blackkingMove):
                print('White wins')
                turn = 2
                whiteWin = True
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
                        if (newSquare != click[0] and turn != 2):
                            drawSquare(screen, newSquare, yellow)
                    else:
                        if (turn != 2):
                            drawSquare(screen,newSquare,yellow)
        if (firstSquare != None and secondSquare != None):
            drawmovesline(screen,firstSquare,secondSquare,lightblue,5)


        mybutton = button(screen, "Back", Width // 2 - 450, Height // 2 + 50, 150, 40, vegasgold, gold, goBack)

        if ((not mybutton) and time > 0 and time <= len(listOfSquareList)):
            time-=1
            print(time)
            Squarelist = list(listOfSquareList[time])

        drawPieces()
        blackWinSquare = Square(350, 280, 300, 100, black)
        whiteWinSquare = Square(350, 280, 300, 100, white)
        if (blackWin):
            drawSquare(screen, blackWinSquare, blackWinSquare.color)
            screen.blit(blackWinText,blackRect)
            button(screen,"New Game",370,330,120,30,vegasgold,gold,start_game)
            button(screen,"Quit",510,330,120,30,vegasgold,gold,quit)
        if (whiteWin):
            drawSquare(screen, whiteWinSquare, whiteWinSquare.color)
            screen.blit(whiteWinText,whiteRect)
            button(screen,"New Game",370,330,120,30,vegasgold,gold,start_game)
            button(screen,"Quit",510,330,120,30,vegasgold,gold,quit)

        pygame.display.update()

game_intro()



