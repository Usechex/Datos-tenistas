from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

jugadores = [{
    "nombre": "juan",
    "edad": 20,
    "altura": 180
}]


@app.route('/insertar', methods=['POST'])
def registrar_jugador():
    jugador = request.get_json()
    print(jugador)

    jugadores.append({
        "nombre": jugador["nombre"],
        "edad": jugador["edad"],
        "altura": jugador["estatura"] 
    })
    return {"message": "Jugador registrado", "jugadores": jugadores}


@app.route('/buscar', methods=['GET'])
def mostrar_jugadores():
    if not jugadores:
        return {"error": "No hay jugadores registrados"}, 404

    result = []
    for element in jugadores:
        result.append({
            "nombre": element["nombre"],
            "edad": element["edad"],
            "altura": element["altura"]
        })
    return {"jugadores": result}


@app.route('/actualizar', methods=['PUT'])
def actualizar_jugadores():
    opcion = request.get_json()
    print(opcion)

    for element in jugadores:
        if opcion["nombre"] == element["nombre"]:
            if opcion["parametro"] == "edad":
                element["edad"] = opcion["cambio"]
            elif opcion["parametro"] == "altura":
                element["altura"] = opcion["cambio"]

    return {"message": "Jugador actualizado", "jugadores": jugadores}


@app.route('/eliminar', methods=['DELETE'])
def eliminar_jugadores():
    opcion = request.get_json()
    print(opcion)

    for i, element in enumerate(jugadores):
        if opcion["nombre"] == element["nombre"]:
            jugadores.pop(i)
            return {"message": "Jugador eliminado", "jugadores": jugadores}

    return {"error": "Jugador no encontrado"}, 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
