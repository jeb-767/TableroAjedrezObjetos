class Alfil:
    def __init__(self, posicion, nombre):
        self.posicion = posicion
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()

    def setTablero(self, tablero):
        self.tablero = tablero

    def movimiento_legal(self, posicion_final):
        legal = True
        if self.posicion[0] == posicion_final[0]:
            if self.posicion[1] > posicion_final[1]:
                numero = -1
            else:
                numero = 1
            for a in range(self.posicion[1], posicion_final[1], numero):
                A = self.tablero[a][posicion_final[0]]
                if A != "" and A != self.tablero[self.posicion[1]][self.posicion[0]]:
                    legal = False
                    break
        elif self.posicion[1] == posicion_final[1]:
            if self.posicion[0] < posicion_final[0]:
                numero = 1
            else:
                numero = -1
            for F in range(self.posicion[0], posicion_final[0], numero):
                A = self.tablero[posicion_final[1]][F]
                if A != "" and A != self.tablero[self.posicion[1]][self.posicion[0]]:
                    legal = False
                    break
        elif self.posicion[0] != posicion_final[0] or self.posicion[1] != posicion_final[1]:
            return False
        if legal == False:
            return False
        else:
            return True

    def mover(self, movimineto):
        if self.movimiento_legal(movimineto):
            self.tablero[movimineto[1]][movimineto[0]] = self
            self.tablero[self.posicion[1]][self.posicion[0]] = ""
            return True
        return False