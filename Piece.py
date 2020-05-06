import pygame


class ChessPieces:
    def __init__(self, image_file, location,type,order,side):
        pygame.sprite.Sprite.__init__(self)
        self.imagefile = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.type = type
        self.side = side
        self.order = order
def DrawPieces(screen,Square):
    screen.blit(Square.Piece.image,Square.Piece.rect)
def DrawPawnPieces(screen, PawnList, side):
    for pawnlocation in PawnList:
        if (side == 'white'):
            Pawn = ChessPieces('Assets\Pieces\whitePawn.png', pawnlocation,'WhitePawn',None)
            screen.blit(Pawn.image, Pawn.rect)
        else:
            Pawn = ChessPieces('Assets/Pieces/blackPawn.png', pawnlocation,'BlackPawn',None)
            screen.blit(Pawn.image, Pawn.rect)

def DrawKnightPieces(screen, KnightList, side):
    for knightlocation in KnightList:
        if (side == 'white'):
            Knight = ChessPieces('Assets\Pieces\whiteKnight.png', knightlocation,'WhiteKnight',None)
            screen.blit(Knight.image, Knight.rect)
        else:
            Knight = ChessPieces('Assets/Pieces/blackKnight.png', knightlocation,'BlackKnight',None)
            screen.blit(Knight.image, Knight.rect)

def DrawBishopPieces(screen, BishopList,side):
    for bishoplocation in BishopList:
        if (side == 'white'):
            Bishop = ChessPieces('Assets\Pieces\whiteBishop.png', bishoplocation,'WhiteBishop',None)
            screen.blit(Bishop.image, Bishop.rect)
        else:
            Bishop = ChessPieces('Assets/Pieces/blackBishop.png', bishoplocation,'BlackBishop',None)
            screen.blit(Bishop.image, Bishop.rect)

def DrawRookPieces(screen, RookList,side):
    for rooklocation in RookList:
        if (side == 'white'):
            Rook = ChessPieces('Assets\Pieces\whiteRook.png', rooklocation,'WhiteRook',None)
            screen.blit(Rook.image, Rook.rect)
        else:
            Rook = ChessPieces('Assets/Pieces/blackRook.png', rooklocation,'BlackRook',None)
            screen.blit(Rook.image,Rook.rect)

def DrawKingPieces(screen, KingList,side):
    for kinglocation in KingList:
        if (side == 'white'):
            King = ChessPieces('Assets\Pieces\whiteKing.png', kinglocation,'WhiteKing',None)
            screen.blit(King.image, King.rect)
        else:
            King = ChessPieces('Assets\Pieces/blackKing.png', kinglocation,'BlackKing',None)
            screen.blit(King.image,King.rect)

def DrawQueenPieces(screen, QueenList,side):
    for queenlocation in QueenList:
        if (side == 'white'):
            Queen = ChessPieces('Assets\Pieces\whiteQueen.png', queenlocation,'WhiteQueen',None)
            screen.blit(Queen.image, Queen.rect)
        else:
            Queen = ChessPieces('Assets\Pieces/blackQueen.png', queenlocation,'BlackQueen',None)
            screen.blit(Queen.image, Queen.rect)

