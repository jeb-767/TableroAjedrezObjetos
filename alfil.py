class Alfil:
    def __init__(self, posicion, nombre, color):
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
        fila = self.posicion[0]
        legal = True
        if self.posicion[1] > posicion_final[1]:
            contador = -1
        else:
            contador = 1
        if self.posicion[0] > posicion_final[0]:
            contador2 = -1
        else:
            contador2 = 1
        for a in range(self.posicion[1], posicion_final[1], contador):
            A = self.tablero[fila][a]
            if A != "" and A != self.tablero[self.posicion[0]][self.posicion[1]]:
                legal = False
                break
            fila += contador2
        if legal == False:
            return False
        else:
            if self.tablero[posicion_final[0]][posicion_final[1]] == "":
                return True
            elif self.tablero[posicion_final[0]][posicion_final[1]].color != self.color:
                return True
            else:
                return False

    def Mover(self, movimineto):
        if self.Movimiento_legal(movimineto):
            self.tablero[movimineto[0]][movimineto[1]] = self
            self.tablero[self.posicion[0]][self.posicion[1]] = ""
            self.posicion = movimineto
            return True
        return False