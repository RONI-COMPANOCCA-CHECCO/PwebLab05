from interpreter import draw
from chessPictures import *

#imagen del cuadrado blanco y su negativo (cuadrado negro)
square_white = square
square_black = square_white.negative()

# Unir alternadamente los cuadrados blanco y negro
row = square_black.join(square_white).join(square_black).join(square_white).join(square_black).join(square_white).join(square_black).join(square_white)

# imagen final
draw(row)
