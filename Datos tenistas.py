from flask import Flask, request
from flask_cors import CORS
import mysql.connector

#################### Conexión a MySQL ################################
conexion = mysql.connector.connect(user="root", password="", 
                                   host="127.0.0.1", 
                                   database="tenis", 
                                   port="3306")
print(conexion)

cursor = conexion.cursor(dictionary=True)  # Usar cursor como diccionario para obtener resultados con nombres de columnas
######################################################################
app = Flask(__name__)
CORS(app)



@app.route('/insertar', methods=['POST'])
def registrar_jugador():

    
    jugador = request.get_json()

    if not isinstance(jugador["estatura"], float):
        return {"error": "la estatura de el jugador no puede ser diferente de un numero formato metros.centimetros", "estatura": jugador["estatura"]}, 400

    if not isinstance(jugador["nombre"], str):
        return {"error": "el nombre de el jugador no puede ser diferente de un string", "nombre": jugador["nombre"]}, 400
    
    if not isinstance(jugador["nacionalidad"],str):
        return {"error": "la nacionalidad de el jugador no puede ser diferente de un string", "nombre": jugador["nacionalidad"]}, 400
    
    if not isinstance(jugador["edad"], int):
        return {"error": "La edad de el jugador debe ser un numero entero", "nombre": jugador["edad"]}, 400

    if (jugador["edad"] >=30 or jugador["edad"] <= 10) :
        return {"error": "esa no es una edad valida", "edad": jugador["edad"]}, 400

    if not isinstance(jugador["cedula"], int):
        return {"error": "La cedula de el jugador debe ser un numero entero", "nombre": jugador["cedula"]}, 400
  

    try:
        sql = "INSERT INTO jugadores (nombre, edad, estatura,nacionalidad,cedula,sangre) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (jugador['nombre'], jugador['edad'], jugador['estatura'],jugador['nacionalidad'],jugador["cedula"],jugador["sangre"])

        cursor.execute(sql, values)
        conexion.commit()

        cursor.execute("SELECT * FROM jugadores")
        jugadores_bd = cursor.fetchall()  
        
        return {"message": "Jugador registrado", "jugadores": jugadores_bd}, 201
    
    except mysql.connector.Error as e:
        return {"error": str(e)}, 500


@app.route('/buscar', methods=['GET'])
def mostrar_jugadores():

    try:
        cursor.execute("SELECT * FROM jugadores")
        jugadores_bd = cursor.fetchall()  

        if not jugadores_bd:
            return {"error": "No hay jugadores registrados"}, 404
        
        lista_jugadores = []
        for element in jugadores_bd:
            lista_jugadores.append({
                'id': element['id'],
                'nombre': element['nombre'],
                'edad': element['edad'],
                'estatura': element['estatura'],
                'nacionalidad':element['nacionalidad'],
                'cedula':element['cedula'],
                'sangre':element['sangre']
            })

        return {"jugadores": lista_jugadores}, 200 
    except mysql.connector.Error as e:
        return {"error": str(e)}, 500


@app.route('/actualizar', methods=['PUT'])
def actualizar_jugadores():
    cursor.execute("SELECT * FROM jugadores")
    jugadores_bd = cursor.fetchall()

    opcion = request.get_json()
    print(opcion)
    if opcion["parametro"] == "estatura" and not isinstance(opcion["cambio"], int):
            return {"error": "la estatura no se puede actualizar con un valor que no sea entero", "estatura": opcion["cambio"]}, 400

    if opcion["parametro"] == "edad":
        if not isinstance(opcion["cambio"], int):
            return {"error": "la edad no se puede actualizar con un valor que no sea entero", "edad": opcion["cambio"]}, 400

    try:
        sql = "UPDATE jugadores SET " + opcion["parametro"] + " = %s WHERE nombre = %s"
        sql = f"UPDATE jugadores SET  {opcion["parametro"]} = %s WHERE nombre = %s"
        values = (opcion["cambio"], opcion["nombre"])
        cursor.execute(sql, values)
        conexion.commit()

        cursor.execute("SELECT * FROM jugadores")
        jugadores_bd = cursor.fetchall()  
        return {"message": "Jugador actualizado", "jugadores": jugadores_bd}, 200
    except mysql.connector.Error as e:
        return {"error": str(e)}, 500


@app.route('/eliminar', methods=['DELETE'])
def eliminar_jugadores():

    opcion = request.get_json()
    print(opcion)
    
    cursor.execute("SELECT * FROM jugadores")
    jugadores_bd = cursor.fetchall()  

    if not isinstance(opcion["nombre"], str):
        return {"error": "este no es un nombre valido", "nombre": opcion["nombre"]}, 400
    
    if jugadores_bd==[]:
        return {"error": "No hay jugadores registrados"}, 404    

    for i, element in enumerate(jugadores_bd):
        
        if opcion["nombre"] == element["nombre"]:

            try:
                sql = "DELETE FROM jugadores WHERE nombre = %s"
                values = (opcion["nombre"],)
                cursor.execute(sql, values)
                conexion.commit()

                cursor.execute("SELECT * FROM jugadores")
                jugadores_bd = cursor.fetchall()  
                return {"message": "Jugador eliminado", "jugadores": jugadores_bd}, 200
            except mysql.connector.Error as e:
                return {"error": str(e)}, 500

    return {"error": "Jugador no encontrado"}, 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
