
class Torre:
    def __init__(self, posicion , nombre , color):
        self.posicion = posicion
        self.nombre = nombre
        self.color = color
        self.movimientos = 0

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()
    def SetTablero(self, tablero):
        self.tablero = tablero
        
    def Movimiento_legal(self, posicion_final):
        legal = True
        if self.posicion[1] == posicion_final[1]:
            if self.posicion[0] > posicion_final[0]:
                numero = -1
            else:
                numero = 1
            for a in range(self.posicion[0], posicion_final[0], numero):
                A = self.tablero[a][posicion_final[1]]
                if A != "" and A != self.tablero[self.posicion[0]][self.posicion[1]]:
                    legal = False
                    break
        elif self.posicion[0] == posicion_final[0]:
            if self.posicion[1] < posicion_final[1]:
                numero = 1
            else:
                numero = -1
            for F in range(self.posicion[1], posicion_final[1], numero):
                A = self.tablero[posicion_final[0]][F]
                if A != "" and A != self.tablero[self.posicion[0]][self.posicion[1]]:
                    legal = False
                    break
        elif self.posicion[1] != posicion_final[1] or self.posicion[0] != posicion_final[0]:
            return False
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
            self.movimientos += 1
            return True
        return False