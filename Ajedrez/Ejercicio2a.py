from interpreter import draw
from chessPictures import *

knight_white = knight
knight_black = knight.negative()

row1 = knight_black.join(knight_white)
row2 = knight_white.join(knight_black)

# Combinamos ambas filas
final_picture = row1.up(row2)

# Imagen final
draw(final_picture)
