from Piezas.torre import Torre
from Piezas.Peon import Peon
from Piezas.alfil import Alfil
from Piezas.Reina import Reina
from Piezas.Caballo import Caballo
from Piezas.Rey import Rey
t1 = Torre([0,0] , "Br1" , "Negro")
t2 = Torre([0,7] , "Wr1" , "Negro")
a1 = Alfil([2, 0] , "Bb" , "Negro")
r1 = Reina([3,0] , "Bq" , "Negro")
c1 = Caballo([1,0] , "Bn" , "Negro")
p1 = Peon([0,1] , "Bp" , "Negro")
lista = [t1, t2, p1 , a1, r1, c1]
k1 = Rey([4,3] , "Bk" , "Negro" , lista)
p1.lista = lista
#a      b    c      d     e     f     g     h
tablero = [[t1, c1, a1, r1, k1, "Bb", "Bn", "Br2"],   #8
     [p1, "", "", "", "", "", "Bp", "Bp"], #  7
     ["", "", "", "", "", "", "", ""],  # 6
     ["", "", "", "", "", "", "", ""],  # 5
     ["", "", "", "", "", "", "", ""],  # 4
     ["Wp", "", "", "", "", "", "", ""],   #3
     ["", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],  # 2
     [t2, "Wn", "Wb", "Wq", "Wk", "Wb", "Wn", "Wr2"]] #  1

t1.setTablero(tablero)
t2.setTablero(tablero)
p1.setTablero(tablero)
a1.setTablero(tablero)
r1.setTablero(tablero)
c1.setTablero(tablero)
k1.setTablero(tablero)
p1.mover([0,3])


for a in tablero:
     print(a)