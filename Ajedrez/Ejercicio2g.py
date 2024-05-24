from interpreter import draw
from chessPictures import square

# Crear la imagen del cuadrado blanco y su negativo (cuadrado negro)
square_white = square
square_black = square_white.negative()

# Unir alternadamente los cuadrados blanco y negro para crear una fila
row1 = square_black.join(square_white).join(square_black).join(square_white).join(square_black).join(square_white).join(square_black).join(square_white)
row2 = square_white.join(square_black).join(square_white).join(square_black).join(square_white).join(square_black).join(square_white).join(square_black)

# Combinar cuatro filas alternadas
final_picture = row1.up(row2).up(row1).up(row2).up(row1).up(row2).up(row1).up(row2)

# Dibujar la imagen final
draw(final_picture)
