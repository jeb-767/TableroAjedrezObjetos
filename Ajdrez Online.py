from Piezas.torre import Torre
from Piezas.Peon import Peon
from Piezas.alfil import Alfil
from Piezas.Reina import Reina
from Piezas.Caballo import Caballo
from Piezas.Rey import Rey
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ListaPiezas = []

TorreNegra1 = Torre([0,0] , "Br1" , "Negro")
TorreNegra2 = Torre([7,0], "Br2" , "Negro")
CaballoNegro1 = Caballo([1,0], "Bn", "Negro")
CaballoNegro2 = Caballo([6,0], "Bn2", "Negro")
AlfilNegro1 = Alfil([2,0] , "Bb" , "Negro")
AlfilNegro2 = Alfil([5,0] , "Bb2" , "Negro")
ReinaNegra = Reina([3,0] , "Bq" , "Negro")

PeonNegro1 = Peon([0,1] , "Bp" , "Negro")
PeonNegro2 = Peon([1,1] , "Bp" , "Negro")
PeonNegro3 = Peon([2,1] , "Bp" , "Negro")
PeonNegro4 = Peon([3,1] , "Bp" , "Negro")
PeonNegro5 = Peon([4,1] , "Bp" , "Negro")
PeonNegro6 = Peon([5,1] , "Bp" , "Negro")
PeonNegro7 = Peon([6,1] , "Bp" , "Negro")
PeonNegro8 = Peon([7,1] , "Bp" , "Negro")

TorreBlanca1 = Torre([0,7] , "Wr1" ,"Blanco")
TorreBlanca2 = Torre([7,7], "Wr2" , "Blanco")
CaballoBlanco1 = Caballo([1,7] , "Wn" , "Blanco")
CaballoBlanco2 = Caballo([6,7] , "Wn" , "Blanco")
AlfilBlanco1 = Alfil([2,7] , "Wb" , "Blanco")
AlfilBlanco2 = Alfil([5,7] , "Wb" , "Blanco")
ReinaBlanca = Reina([3,7] , "Wq" , "Blanco")

PeonNegro1 = Peon([0,1] , "Bp" , "Negro")
PeonNegro2 = Peon([1,1] , "Bp" , "Negro")
PeonNegro3 = Peon([2,1] , "Bp" , "Negro")
PeonNegro4 = Peon([3,1] , "Bp" , "Negro")
PeonNegro5 = Peon([4,1] , "Bp" , "Negro")
PeonNegro6 = Peon([5,1] , "Bp" , "Negro")
PeonNegro7 = Peon([6,1] , "Bp" , "Negro")
PeonNegro8 = Peon([7,1] , "Bp" , "Negro")




ReyNegro = Rey([4,0] , "Bk" , "Negro")

ListaPiezas.append(TorreBlanca1)

   #a      b    c      d     e     f     g     h
tablero = [[TorreNegra1,CaballoNegro1, AlfilNegro1, ReinaNegra, ReyNegro, AlfilNegro2, CaballoNegro2, TorreNegra2],   #8
     [PeonNegro1, PeonNegro2, PeonNegro3, PeonNegro4, PeonNegro5, PeonNegro6, PeonNegro7, PeonNegro8], #  7
     ["", "", "", "", "", "", "", ""],  # 6
     ["", "", "", "", "", "", "", ""],  # 5
     ["", "", "", "", "", "", "", ""],  # 4
     ["", "", "", "", "", "", "", ""],   #3
     ["", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],  # 2
     [TorreBlanca1, "Wn", "Wb", "Wq", "Wk", "Wb", "Wn", "Wr2"]] #  1

TorreBlanca1.setTablero(tablero)
TorreBlanca2.setTablero(tablero)
TorreNegra1.setTablero(tablero)
TorreNegra2.setTablero(tablero)
TorreNegra1.mover([0,3])
TorreBlanca1.mover([0,4])
for a in tablero:
    print(a)
@app.route("/movimiento_externo" , methods=["POST"])
def movimiento_externo():
    global movimiento_n
    global blancas
    Tablero[0][0]=Reina()
#    datos = request.json
    #movimiento = datos["movimiento"]
    #mov = [0, 0, 0, 0]
    #contarMovimientos(movimiento_n)
    #mov[0] = str(movimiento[0]).upper()
    #mov[2] = str(movimiento[2]).upper()
    #mov[1] = int(movimiento[1])
    #mov[3] = int(movimiento[3])
    #canviarnumeros(mov)
    #x = m[mov[1]][mov[0]]
    #y = m[mov[3]][mov[2]]
    #contarMovimientos(movimiento_n)
    #blancas = comprobarMovimientos(x)
    #legal = movimiento_legal(blancas, mov, x, y)
    #if legal is False:
    #    print("MOVIMIENTO ILEGAL")
    #else:
    #    movimiento_n += 1

#return jsonify(resultado = m)

app.run(debug=True)
