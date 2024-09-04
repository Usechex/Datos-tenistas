from flask import Flask,request
from flask_cors import CORS

app=Flask(_name_)
CORS(app)

jugadores=[{
"nombre":"juan",
"edad":20,
"estatura":180
}]

@app.route('/insertar', methods = ['POST'])
def registrar_jugador ():

    jugador = request.get_json()
    print(jugador)

    jugadores.append({
            "nombre":jugador["nombre"],
            "edad":jugador["edad"],
            "estatura":jugador["estatura"]
    })
    return jugadores

# Defino mostar jugadores

@app.route('/buscar', methods = ['GET'])
def mostrar_jugadores():
    result=[]

    if not jugadores:
        print("no hay jugadores registrados ")
        return {"error":"no hay jugadores registrados "}
    
    for element in jugadores:
        result.append({
            "name":element["nombre"],
            "age":element["edad"],
            "high":element["estatura"]
        })
    return result


@app.route('/actualizar', methods = ['PUT'])
def actualizar_jugadores():
    opcion = request.get_json()
    print (opcion)

    for element in jugadores:       
        if opcion["nombre"]==element["nombre"]:
       
            if opcion["parametro"]=="edad":
                element["edad"]=opcion["cambio"]
            
            elif opcion["parametro"]=="estatura":
                element["estatura"]=opcion["cambio"]

    return jugadores


@app.route('/eliminar', methods = ['DELETE'])
def eliminar_jugadores():
    borrar=False
    opcion = request.get_json()
    print (opcion)

    for element in jugadores:       
        if opcion["nombre"]==element["nombre"]:
            borrar=True

    if borrar == True:
        jugadores.pop(element["nombre"])
        jugadores.pop(element["edad"])
        jugadores.pop(element["estatura"])
        borrar=False    
        
    return jugadores   


if _name_ == '_main_':
    app.run(host="0.0.0.0",port=5000,debug=False)