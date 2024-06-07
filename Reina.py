from Piezas.torre import Torre
from Piezas.alfil import Alfil
class Reina:
    def __init__(self, posicion , nombre , color):
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
        if Torre.movimiento_legal(self, posicion_final) or Alfil.movimiento_legal(self, posicion_final):
            return True
    def mover(self, posicion_final):
        if self.movimiento_legal(posicion_final):
            self.tablero[posicion_final[1]][posicion_final[0]] = self
            self.tablero[self.posicion[1]][self.posicion[0]] = ""
            self.posicion = posicion_final
            return True
        return False