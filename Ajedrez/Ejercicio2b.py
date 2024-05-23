from interpreter import draw
from chessPictures import *

# Creamos los imágenes de los caballos
knight_white = knight
knight_black = knight.negative()

# Reflejar horizontalmente los caballos para que miren hacia la derecha
knight_white_mirrored = knight_white.verticalMirror()
knight_black_mirrored = knight_black.verticalMirror()

# Unimos las imagenes como vemos en el imagen que deseamos realizar
row1 = knight_black_mirrored.join(knight_white_mirrored)
row2 = knight_white.join(knight_black)

# Combinamos ambas filas
final_picture = row1.up(row2)

draw(final_picture)
