from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(self.img[::-1])

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for line in self.img:
        neg_line = ''.join([self._invColor(char) for char in line])
        negative.append(neg_line)
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joined_img = [self.img[i] + p.img[i] for i in range(len(self.img))]
    return Picture(joined_img)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(p.img + self.img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeated_img = [line * n for line in self.img]
    return Picture(repeated_img)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
        la cantidad de veces que indique el valor de n """
    return Picture(self.img * n)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
    rotated_img = list(zip(*self.img[::-1]))
    return Picture([''.join(row) for row in rotated_img])