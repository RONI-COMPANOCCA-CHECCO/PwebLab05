from interpreter import draw
from chessPictures import queen

# Crear la imagen de la reina
queen_white = queen

# Unir la reina consigo misma repetidamente para formar una línea de 4 reinas
row = queen_white.join(queen_white).join(queen_white).join(queen_white)

# Dibujar la imagen final
draw(row)
