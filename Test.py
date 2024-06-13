from Piezas.torre import Torre
from Piezas.Peon import Peon
from Piezas.alfil import Alfil
from Piezas.Reina import Reina
from Piezas.Caballo import Caballo
from Piezas.Rey import Rey
t1 = Torre([0,0] , "Br1" , "Negro")
t2 = Torre([7,0] , "Wr1" , "Blanco")
a1 = Alfil([7,0] , "Bb" , "Negro")
r1 = Reina([3,0] , "Bq" , "Negro")
c1 = Caballo([1,0] , "Bn" , "Negro")
p1 = Peon([0,6] , "Bp" , "Blanco")
t3 = Torre([7,0] , "Br2" , "Negro")
lista = [t1, t2, p1 , a1, r1, c1]
k1 = Rey([0,4] , "Bk" , "Negro" , lista)
#a      b    c      d     e     f     g     h
tablero = [[t1, "", a1, "", k1, "", "", t3],   #8
     ["", "", "", "", "", "", "", ""], #  7
     ["", "", "", p1, "", "", "", ""],  # 6
     ["", "", "", "", "", "", "", ""],  # 5
     ["", "", "", "", "", "", "", ""],  # 4
     ["Wp", "", "", "", "", "", "", ""],   #3
     ["", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],  # 2
     ["", "Wn", "Wb", "Wq", "Wk", "Wb", "Wn", "Wr2"]] #  1

t1.SetTablero(tablero)
t2.SetTablero(tablero)
p1.SetTablero(tablero)
a1.SetTablero(tablero)
r1.SetTablero(tablero)
c1.SetTablero(tablero)
k1.SetTablero(tablero)
k1.Mover([1,3])


for a in tablero:
     print(a)