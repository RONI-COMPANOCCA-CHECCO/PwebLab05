from interpreter import draw
from chessPictures import queen

# Crear la imagen de la reina
queen_white = queen

# Reflejar horizontalmente la reina
queen_white_mirrored = queen_white.horizontalMirror()

# Unir la reina consigo misma
row1 = queen_white.join(queen_white)
row2 = queen_white_mirrored.join(queen_white_mirrored)

# Combinamos ambas filas
final_picture = row1.up(row2)

# Dibujamos la imagen final
draw(final_picture)
