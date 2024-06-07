from math import sqrt
class Caballo:
    def __init__(self, posicion, nombre, color):
        self.posicion = posicion
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()

    def setTablero(self, tablero):
        self.tablero = tablero
    def movimiento_legal(self, posicion_final):
        mov1 = posicion_final[0] - self.posicion[0]
        mov2 = posicion_final[1] - self.posicion[1]
        movimiento1 = sqrt((mov1 ** 2) + (mov2 ** 2))
        if movimiento1 == sqrt(5) and self.posicion[0] != posicion_final[0] and self.posicion[1] != posicion_final[1]:
            if self.tablero[posicion_final[1]][posicion_final[0]] == "":
                return True
            elif self.tablero[posicion_final[1]][posicion_final[0]].color != self.color:
                return True
            else:
                return False
        else:
            return False
    def mover(self, movimineto):
        if self.movimiento_legal(movimineto):
            self.tablero[movimineto[1]][movimineto[0]] = self
            self.tablero[self.posicion[1]][self.posicion[0]] = ""
            self.posicion = movimineto
            return True
        return False