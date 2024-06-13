from torre import Torre
from alfil import Alfil
class Reina:
    def __init__(self, posicion , nombre , color):
        self.posicion = posicion
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()

    def SetTablero(self, tablero):
        self.tablero = tablero

    def Movimiento_legal(self, posicion_final):
        if Torre.Movimiento_legal(self, posicion_final) or Alfil.Movimiento_legal(self, posicion_final):
            return True
    def Mover(self, posicion_final):
        if self.Movimiento_legal(posicion_final):
            self.tablero[posicion_final[0]][posicion_final[1]] = self
            self.tablero[self.posicion[0]][self.posicion[1]] = ""
            self.posicion = posicion_final
            return True
        return False