from Piezas.torre import Torre
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ListaPiezas = []

TorreBlanca1 = Torre([0,7] , "Wr1")
TorreBlanca2 = Torre([7,7], "Wr2")
TorreNegra1 = Torre([0,0] , "Br1")
TorreNegra2 = Torre([7,0], "Br2")

ListaPiezas.append(TorreBlanca1)

   #a      b    c      d     e     f     g     h
tablero = [[TorreNegra1, "Bn", "Bb", "Bq", "Bk", "Bb", "Bn", "Br2"],   #8
     ["", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp"], #  7
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