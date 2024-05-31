class Alfil:
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
        fila = self.posicion[1]
        legal = True
        if movimiento[0] > movimiento[2]:
            contador = -1
        else:
            contador = 1
        if movimiento[1] > movimiento[3]:
            contador2 = -1
        else:
            contador2 = 1
        for a in range(movimiento[0], movimiento[2], contador):
            A = m[fila][a]
            if A != "" and A != x:
                legal = False
                break
            fila += contador2
        if legal == False:
            print("El movimiento no es legal")
            return False
        else:
            print("El movimiento es legal")
            self.mover(movimiento)
            return True

    def mover(self, movimineto):
        if self.movimiento_legal(movimineto):
            self.tablero[movimineto[1]][movimineto[0]] = self
            self.tablero[self.posicion[1]][self.posicion[0]] = ""
            return True
        return False
