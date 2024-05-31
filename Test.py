from Piezas.torre import Torre
from Piezas.Peon import Peon
t1 = Torre([0,0] , "Br1" , "Negro")
t2 = Torre([0,7] , "Wr1" , "Blanco")
p1 = Peon([0 , 3] , "Bp" , "Blanco")
#a      b    c      d     e     f     g     h
tablero = [[t1, "Bn", "Bb", "Bq", "Bk", "Bb", "Bn", "Br2"],   #8
     ["", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp"], #  7
     ["", "", "", "", "", "", "", ""],  # 6
     [p1, "", "", "", "", "", "", ""],  # 5
     ["", "", "", "", "", "", "", ""],  # 4
     ["Wp", "", "", "", "", "", "", ""],   #3
     ["", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],  # 2
     [t2, "Wn", "Wb", "Wq", "Wk", "Wb", "Wn", "Wr2"]] #  1

t1.setTablero(tablero)
t2.setTablero(tablero)
p1.setTablero(tablero)
t1.mover([0,3])
for a in tablero:
     print(a)