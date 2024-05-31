class Peon:
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