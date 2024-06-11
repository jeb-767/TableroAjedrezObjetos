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
    def setTablero(self, tablero):
        self.tablero = tablero

    def movimiento_legal(self, posicion_final):
        legal = False
        legal1 = False
        if self.color == "Blancas":
            numero = -1
            numero2 = -2
        else:
            numero = 1
            numero2 = 2
        if self.posicion[0] == posicion_final[0]:
            if self.posicion[1] == 1 or self.posicion[1] == 6:
                if (self.posicion[1] + numero2 == posicion_final[1]) or (self.posicion[1] + numero == posicion_final[1]):
                    for a in range(self.posicion[1], posicion_final[1], numero):
                        A = self.tablero[a][posicion_final[0]]
                        if A == "" or A == self.tablero[self.posicion[1]][self.posicion[0]]:
                            legal = True
                            break
                else:
                    legal = False
            else:
                if self.posicion[1] + numero == posicion_final[1]:
                    legal= True
                else:
                    legal = False
        elif self.posicion[0] != posicion_final[0]:
            if (self.posicion[0] + 1 == posicion_final[0] or self.posicion[0] - 1 == posicion_final[0]) and self.posicion[1] + numero == posicion_final[1] and self.tablero[posicion_final[1]][posicion_final[0]].color != self.color:
                legal = True
            else:
                legal = False
        print(posicion_final[1])
        if legal == True:
            if (self.color == "Blanco" and posicion_final[1] == 0) or (self.color == "Negro" and posicion_final[1] == 7):
                print("Reina")
                if self.color == "Blanco":
                    self = Reina(posicion_final , "Wq", self.color)
                elif self.color == "Negro":
                    self = Reina(posicion_final , "Bq", self.color)
                return True
            else:
                legal1 = True
        if legal1 == True:
            if self.tablero[posicion_final[1]][posicion_final[0]] == "":
                return True
            elif self.tablero[posicion_final[1]][posicion_final[0]].color != self.color:
                return True
            else:
                return False


    def mover(self, posicion_final):
        if self.movimiento_legal(posicion_final):
            self.tablero[posicion_final[1]][posicion_final[0]] = self
            self.tablero[self.posicion[1]][self.posicion[0]] = ""
            self.posicion = posicion_final
            return True
        return False