from interpreter import draw
from chessPictures import *

# Crear la imagen del cuadrado blanco y su negativo (cuadrado negro)
square_white = square
square_black = square.negative()

# Crear una fila alternada de cuadrados blancos y negros
row1 = square_black.join(square_white).horizontalRepeat(4)
row2 = square_white.join(square_black).horizontalRepeat(4)

# Crear el tablero combinando las filas alternadas
board = row1.up(row2).verticalRepeat(4)

# Piezas negras
rock_black = rock.superimpose(square_black)
rock_black1 = rock.superimpose(square_white)
knight_black = knight.superimpose(square_black)
knight_black1 = knight.superimpose(square_white)
bishop_black = bishop.superimpose(square_black)
bishop_black1 = bishop.superimpose(square_white)
queen_black = queen.superimpose(square_white)
king_black = king.superimpose(square_black)

pawn_black = pawn.superimpose(square_white)
pawn_black1 = pawn.superimpose(square_black)

# Piezas blancas
rock_white = rock.negative().superimpose(square_white)
rock_white1 = rock.negative().superimpose(square_black)
knight_white = knight.negative().superimpose(square_white)
knight_white1 = knight.negative().superimpose(square_black)
bishop_white = bishop.negative().superimpose(square_white)
bishop_white1 = bishop.negative().superimpose(square_black)
queen_white = queen.negative().superimpose(square_black)
king_white = king.negative().superimpose(square_white)

pawn_white1 = pawn.negative().superimpose(square_white)
pawn_white = pawn.negative().superimpose(square_black)

# Fila de piezas negras
row_black_pieces = rock_black.join(knight_black1).join(bishop_black).join(queen_black).join(king_black).join(bishop_black1).join(knight_black).join(rock_black1)
# Fila de peones negros
row_black_pawns = pawn_black.join(pawn_black1).join(pawn_black).join(pawn_black1).join(pawn_black).join(pawn_black1).join(pawn_black).join(pawn_black1)
# Fila de piezas blancas
row_white_pieces = rock_white.join(knight_white1).join(bishop_white).join(queen_white).join(king_white).join(bishop_white1).join(knight_white).join(rock_white1)
# Fila de peones blancos
row_white_pawns = pawn_white.join(pawn_white1).join(pawn_white).join(pawn_white1).join(pawn_white).join(pawn_white1).join(pawn_white).join(pawn_white1)

# Crear el tablero completo con las piezas
board_with_pieces = (
    row_black_pieces
    .up(row_black_pawns)
    .up(board.crop(0, 0, board.width, square.height * 4))
    .up(row_white_pawns)
    .up(row_white_pieces)
)

# Dibujar la imagen final con las piezas
draw(board_with_pieces)
