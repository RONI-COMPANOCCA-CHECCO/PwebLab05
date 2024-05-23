from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = self.img[::-1]
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = [line[::-1] for line in self.img]
        return Picture(horizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negative_img = [[self._invColor(char) for char in line] for line in self.img]
        return Picture(negative_img)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        joined_img = [self.img[i] + p.img[i] for i in range(len(self.img))]
        return Picture(joined_img)

    def up(self, p):
        """ Devuelve una nueva figura poniendo la figura recibida como argumento,
            encima de la figura actual """
        return Picture(p.img + self.img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura recibida como argumento,
            sobre la figura actual """
        return Picture(self.img + p.img)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        repeated_img = [line * n for line in self.img]
        return Picture(repeated_img)

    def verticalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual debajo,
            la cantidad de veces que indique el valor de n """
        repeated_img = self.img * n
        return Picture(repeated_img)

    # Extra: Sólo para realmente viciosos 
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        rotated_img = ["".join(row) for row in zip(*self.img[::-1])]
        return Picture(rotated_img)


