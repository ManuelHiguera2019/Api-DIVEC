from flask import Flask, jsonify
app = Flask(__name__)

import  mysql.connector

conexion = mysql.connector.connect(
    port='3306',
    user='root',
    password='',
    database='divec'
)

cursor = conexion.cursor()

@app.route("/api/v1/appdivec/")

def hello():
    query = "SELECT * FROM materia"
    selectProf = 'SELECT * from profesor WHERE id = %s'
    selectDia = 'SELECT * from dia WHERE id = %s'
    selectHora = 'SELECT * from hora WHERE id = %s'
    selectAula = 'SELECT * from aula WHERE id = %s'
    selectEdificio = 'SELECT * from edificio WHERE id = %s'
    selectDetalle = 'SELECT * from detalle_materia WHERE id = %s'
    selectPeriodo = 'SELECT * from periodo WHERE id = %s'

    selectIdCarrera = 'SELECT * from carrera_materia WHERE id_detalle_materia = %s'
    selectCarrera = 'SELECT * from carrera WHERE id = %s'


    cursor.execute(query)
    registros = cursor.fetchall()
    lista = []
    validation = []
    for registro in registros:

        cursor.execute(selectProf, (registro[4],))
        profesor = cursor.fetchall()
        cursor.execute(selectDia, (registro[5],))
        dia = cursor.fetchall()
        cursor.execute(selectHora, (registro[6],))
        hora = cursor.fetchall()
        cursor.execute(selectAula, (registro[7],))
        aula = cursor.fetchall()
        cursor.execute(selectEdificio, (registro[8],))
        edificio = cursor.fetchall()
        cursor.execute(selectDetalle, (registro[9],))
        detalle = cursor.fetchall()
        cursor.execute(selectPeriodo, (detalle[0][4],))
        periodo = cursor.fetchall()

        cursor.execute(selectIdCarrera, (detalle[0][0],))
        idCarrera = cursor.fetchall()
        cursor.execute(selectCarrera, (idCarrera[0][1],))
        carrera = cursor.fetchall()

        if len(idCarrera) > 1 and registro[1] not in validation:
            cursor.execute(selectCarrera, (idCarrera[1][1],))
            carrera2 = cursor.fetchall()

            r = {
                'nrc': registro[1],
                'carrera': carrera[0][1] + '/' + carrera2[0][1],
                'clave': detalle[0][1],
                'materia': detalle[0][2],
                'creditos': detalle[0][3],
                'cupos': registro[2],
                'disponible': registro[3],
                'hora': hora[0][1],
                'dias': dia[0][1],
                'edificio': edificio[0][1],
                'aula': aula[0][1],
                'periodo': periodo[0][1],
                'maestro': profesor[0][1]
            }
            lista.append(r)
            validation.append(registro[1])
        if len(idCarrera) == 1 and registro[1] not in validation:
            r = {
                'nrc': registro[1],
                'carrera': carrera[0][1],
                'clave': detalle[0][1],
                'materia': detalle[0][2],
                'creditos': detalle[0][3],
                'cupos': registro[2],
                'disponible':registro[3],
                'hora': hora[0][1],
                'dias': dia[0][1],
                'edificio': edificio[0][1],
                'aula': aula[0][1],
                'periodo': periodo[0][1],
                'maestro': profesor[0][1]
            }
            lista.append(r)
            validation.append(registro[1])
    return jsonify(lista)

    print(rows)
app.run()