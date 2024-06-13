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

    def SetTablero(self, tablero):
        self.tablero = tablero

    def Movimiento_legal(self, posicion_final):
        legal = True
        legal1 = False
        for a in self.piezas:
            if a.color != self.color:
                if a.nombre[1] == "p":
                    if a.matar([posicion_final[0], posicion_final[1]]):
                        return False
                elif a.nombre[1] != "p":
                    if a.Movimiento_legal(posicion_final):
                        return False
                else:

                    legal = True
        if legal:
            numero = 0
            numero1 = 0
            if self.posicion[1] > posicion_final[1]:
                numero = -1
            elif self.posicion[1] < posicion_final[1]:
                numero = 1

            if self.posicion[0] > posicion_final[0]:
                numero1 = -1
            elif self.posicion[0] < posicion_final[0]:
                numero1 = 1

            if self.movimientos == 0:
                if (self.color == "Negro" and self.posicion == [0,4]):
                    if posicion_final == [0,2]:
                        if self.tablero[1][0] == "" and self.tablero[2][0] == "" and self.tablero[3][0] == "":
                            if self.tablero[0][0].movimientos == 0:
                                self.tablero[0][3] = self.tablero[0][0]
                                self.tablero[0][0]= ""
                                self.tablero[0][3].posicion[1] = posicion_final[1] + 1
                                self.tablero[0][3].posicion[0] = posicion_final[0]
                                return True
                    if  posicion_final == [0,6]:
                        if self.tablero[5][0] == "" and self.tablero[6][0] == "":
                            if self.tablero[7][0].movimientos == 0:
                                print("hola")
                                self.tablero[0][5] = self.tablero[7][0]
                                self.tablero[0][7] = ""
                                self.tablero[0][5].posicion[1] = posicion_final[1] + 1
                                self.tablero[0][5].posicion[0] = posicion_final[0]
                                return True
                            return True
                if (self.color == "Blanco" and self.posicion == [7,4]):
                    if posicion_final == [7,2]:
                        if self.tablero[7][1] == "" and self.tablero[7][2] == "" and self.tablero[7][3] == "":
                            if self.tablero[7][0].movimientos == 0:
                                self.tablero[7][3] = self.tablero[7][0]
                                self.tablero[7][0] = ""
                                self.tablero[7][3].posicion[0] = posicion_final[0] + 1
                                self.tablero[7][3].posicion[1] = posicion_final[1]
                                return True
                    if posicion_final == [7,6]:
                        if self.tablero[7][5] == "" and self.tablero[7][6] == "":
                            if self.tablero[7][7].movimientos == 0:
                                print("hola")
                                self.tablero[7][5] = self.tablero[7][7]
                                self.tablero[7][7] = ""
                                self.tablero[7][5].posicion[1] = posicion_final[1] + 1
                                self.tablero[7][5].posicion[0] = posicion_final[0]
                                return True
                            return True

            if self.posicion[0] + numero1 == posicion_final[0] and self.posicion[1] + numero == posicion_final[1]:
                legal1 = True


        if legal1:
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
            self.movimientos +=1
            return True
        return False