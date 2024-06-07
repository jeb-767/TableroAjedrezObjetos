class Rey:
    def __init__(self, posicion, nombre, color, piezas):
        self.posicion = posicion
        self.nombre = nombre
        self.color = color
        self.piezas = piezas

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()

    def setTablero(self, tablero):
        self.tablero = tablero

    def movimiento_legal(self, posicion_final):
        legal = True
        legal1 = False
        for a in self.piezas:
            if a.color != self.color:
                if a.movimiento_legal(posicion_final):
                    return False
            else:
                legal = True
        if legal:
            numero = 0
            numero1 = 0
            if self.posicion[0] > posicion_final[0]:
                numero = -1
            elif self.posicion[0] < posicion_final[0]:
                numero = 1

            if self.posicion[1] > posicion_final[1]:
                numero1 = -1
            elif self.posicion[1] < posicion_final[1]:
                numero1 = 1
            if self.posicion[1] + numero1 == posicion_final[1] and self.posicion[0] + numero == posicion_final[0]:
                legal1 = True
        if legal1:
            if self.tablero[posicion_final[1]][posicion_final[0]] == "":
                return True
            elif self.tablero[posicion_final[1]][posicion_final[0]].color != self.color:
                return True
            else:
                return False
    def mover(self, movimineto):
        if self.movimiento_legal(movimineto):
            self.tablero[movimineto[1]][movimineto[0]] = self
            self.tablero[self.posicion[1]][self.posicion[0]] = ""
            self.posicion = movimineto
            return True
        return False