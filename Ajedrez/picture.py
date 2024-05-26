# Picture.py
from colors import *

class Picture:
    def __init__(self, img):
        self.img = img
        self.width = len(img[0])
        self.height = len(img)

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = [row[::-1] for row in self.img]
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = self.img[::-1]
        return Picture(horizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negative = []
        for row in self.img:
            new_row = ''.join(self._invColor(c) for c in row)
            negative.append(new_row)
        return Picture(negative)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        new_img = [r1 + r2 for r1, r2 in zip(self.img, p.img)]
        return Picture(new_img)

    def up(self, p):
        return Picture(p.img + self.img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        return Picture(self.img + p.img)
  
    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        new_img = [row * n for row in self.img]
        return Picture(new_img)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
            la cantidad de veces que indique el valor de n """
        return Picture(self.img * n)

    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        rotated = list(zip(*self.img[::-1]))
        return Picture([''.join(row) for row in rotated])
    
    def superimpose(self, other):
        new_img = []
        for row_self, row_other in zip(self.img, other.img):
            new_row = ""
            for char_self, char_other in zip(row_self, row_other):
                new_row += char_self if char_self != " " else char_other
            new_img.append(new_row)
        return Picture(new_img)
    
    def crop(self, x, y, width, height):
        cropped_img = [row[x:x + width] for row in self.img[y:y + height]]
        return Picture(cropped_img)
