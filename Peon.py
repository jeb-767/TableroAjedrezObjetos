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
        legal = True
        legal1 = True
        if self.color == "Blancas":
            numero = -1
            numero2 = -2
        else:
            numero = 1
            numero2 = 2
        if self.posicion[0] == posicion_final[0]:
            if self.posicion[1] == 1 or self.posicion[1] == 6:
                if (self.posicion[1] + numero2 == posicion_final[1]) or (self.posicion[1] + numero == posicion_final[1]):
                    legal = True
                else:
                    legal = False
            else:
                if self.posicion[1] + numero == posicion_final[1]:
                    legal= True
                else:
                    legal = False
        elif self.posicion[0] != posicion_final[0]:


    def mover(self, posicion_final):
        if self.movimiento_legal(posicion_final):
            self.tablero[posicion_final[1]][posicion_final[0]] = self
            self.tablero[self.posicion[1]][self.posicion[0]] = ""
            return True
        return False