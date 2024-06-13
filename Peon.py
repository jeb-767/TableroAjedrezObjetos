from Piezas.Reina import Reina
class Peon:
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
        legal = False
        legal1 = False
        if self.color == "Blancas":
            numero = -1
            numero2 = -2
        else:
            numero = 1
            numero2 = 2
        if self.posicion[1] == posicion_final[1]:
            if self.posicion[0] == 1 or self.posicion[0] == 6:
                if (self.posicion[0] + numero2 == posicion_final[0]) or (self.posicion[0] + numero == posicion_final[0]):
                    for a in range(self.posicion[0], posicion_final[0], numero):
                        A = self.tablero[a][posicion_final[1]]
                        if A == "" or A == self.tablero[self.posicion[0]][self.posicion[1]]:
                            legal = True
                            break
                else:
                    legal = False
            else:
                if self.posicion[0] + numero == posicion_final[0]:
                    legal= True
                else:
                    legal = False
        elif self.posicion[1] != posicion_final[1]:
            if (self.posicion[1] + 1 == posicion_final[1] or self.posicion[1] - 1 == posicion_final[1]) and self.posicion[0] + numero == posicion_final[0] and self.tablero[posicion_final[0]][posicion_final[1]].color != self.color:
                legal = True
            else:
                legal = False
        if legal == True:
                legal1 = True
        if legal1 == True:
            if self.tablero[posicion_final[0]][posicion_final[1]] == "":
                return True
            elif self.tablero[posicion_final[0]][posicion_final[1]].color != self.color:
                return True
            else:
                return False


    def Mover(self, posicion_final):
        if self.Movimiento_legal(posicion_final):
            self.tablero[posicion_final[0]][posicion_final[1]] = self
            self.tablero[self.posicion[0]][self.posicion[1]] = ""
            self.posicion = posicion_final
            return True
        return False