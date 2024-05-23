from interpreter import draw
from chessPictures import queen

queen_white = queen

# Unimos la reina consigo misma repetidamente para formar una línea de 4 reinas
row = queen_white.join(queen_white).join(queen_white).join(queen_white)

# imagen final
draw(row)
