class Rey:
    def __init__(self, posicion, nombre, color, piezas):
        self.posicion = posicion
        self.nombre = nombre
        self.color = color
        self.piezas = piezas
        self.movimientos = 0

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
                if a.nombre[1] == "p":
                    if a.movimiento_legal[(self.posicion[0] + 1 , self.posicion[1] +1)] or a.movimiento_legal[(self.posicion[0] + 1 , self.posicion[1] - 1)] or a.movimiento_legal[(self.posicion[0] - 1 , self.posicion[1] + 1)] or a.movimiento_legal[(self.posicion[0] - 1 , self.posicion[1] - 1)]:
                        return False
                elif a.movimiento_legal(posicion_final):
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

            if self.movimientos == 0:
                if (self.color == "Negro" and self.posicion == [4,0]):
                    if posicion_final == [2,0]:
                        if self.tablero[0][1] == "" and self.tablero[0][2] == "" and self.tablero[0][3] == "":
                            if self.tablero[0][0].movimientos == 0:
                                self.tablero[0][3] = self.tablero[0][0]
                                self.tablero[0][0]= ""
                                self.tablero[0][3].posicion[0] = posicion_final[0] + 1
                                self.tablero[0][3].posicion[1] = posicion_final[1]
                                return True
                    if  posicion_final == [6,0]:
                        if self.tablero[0][5] == "" and self.tablero[0][6] == "":
                            if self.tablero[0][7].movimientos == 0:
                                print("hola")
                                self.tablero[0][5] = self.tablero[0][7]
                                self.tablero[0][7] = ""
                                self.tablero[0][5].posicion[0] = posicion_final[0] + 1
                                self.tablero[0][5].posicion[1] = posicion_final[1]
                                return True
                            return True
                if (self.color == "Blanco" and self.posicion == [4, 7]):
                    if posicion_final == [2, 7]:
                        if self.tablero[7][1] == "" and self.tablero[7][2] == "" and self.tablero[7][3] == "":
                            if self.tablero[7][0].movimientos == 0:
                                self.tablero[7][3] = self.tablero[7][0]
                                self.tablero[7][0] = ""
                                self.tablero[7][3].posicion[0] = posicion_final[0] + 1
                                self.tablero[7][3].posicion[1] = posicion_final[1]
                                return True
                    if posicion_final == [6, 7]:
                        if self.tablero[7][5] == "" and self.tablero[7][6] == "":
                            if self.tablero[7][7].movimientos == 0:
                                print("hola")
                                self.tablero[7][5] = self.tablero[7][7]
                                self.tablero[7][7] = ""
                                self.tablero[7][5].posicion[0] = posicion_final[0] + 1
                                self.tablero[7][5].posicion[1] = posicion_final[1]
                                return True
                            return True

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
            self.movimientos +=1
            return True
        return False