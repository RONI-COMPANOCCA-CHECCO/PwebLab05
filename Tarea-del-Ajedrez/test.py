from interpreter import draw
from chessPictures import *

# Crear un tablero de ajedrez vacío
empty_board = Picture(SQUARE * 8)

# Crear instancias de piezas de ajedrez
bishop_piece = Picture(BISHOP)
king_piece = Picture(KING)
# Añadir más piezas según sea necesario...

# Dibujar el tablero y las piezas
draw(empty_board)
draw(bishop_piece)
draw(king_piece)
# Dibujar más piezas y tableros si es necesario...

# Mantener la ventana abierta
input("Presiona Enter para salir...")
