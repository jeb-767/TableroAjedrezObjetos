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
        if self.posicion[0] > posicion_final[0]:
            contador = -1
        else:
            contador = 1
        if self.posicion[1] > posicion_final[1]:
            contador2 = -1
        else:
            contador2 = 1
        for a in range(self.posicion[0], posicion_final[0], contador):
            A = self.tablero[fila][a]
            if A != "" and A != self.tablero[self.posicion[1]][self.posicion[0]]:
                legal = False
                break
            fila += contador2
        if legal == False:
            return False
        else:
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