from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return mysql.connector.connect(
            host="junction.proxy.rlwy.net",
            user="root",         
            password="pIlIsuQhQMjADoGiJiflkvwcdZXEWxOm",  
            database="bd_universidad",
            port="54784" 
        )


@app.route('/')
def index():
    try:
        connection = get_db_connection()
        if connection.is_connected():
            return jsonify({"message": "Conexión exitosa a la base de datos MySQL"}), 200
    except mysql.connector.Error as e:
        return jsonify({"error": f"Error al conectar a la base de datos: {e}"}), 500
    finally:
        if connection.is_connected():
            connection.close()


@app.route('/api/carreras')
def get_carreras():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT codigoCP, nomCP, Fecha_creacion, observaciones 
            FROM TCarreraProfesional
            ORDER BY nomCP
        """)
        carreras = cursor.fetchall()
        return jsonify(carreras)
    finally:
        cursor.close()
        conn.close()

@app.route('/api/alumnos/conteo')
def get_alumnos_conteo():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT cp.nomCP as carrera, COUNT(a.Codigo_alumno) as total_alumnos
            FROM TCarreraProfesional cp
            LEFT JOIN TAlumno a ON cp.codigoCP = a.cod_cp
            GROUP BY cp.nomCP, cp.codigoCP
            ORDER BY cp.nomCP
        """)
        conteo = cursor.fetchall()
        return jsonify(conteo)
    finally:
        cursor.close()
        conn.close()

@app.route('/api/alumnos/filtrados')
def get_alumnos_filtrados():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT 
                a.Codigo_alumno as codigo,
                a.AP as apellido,
                a.Nom as nombre,
                cp.nomCP as carrera
            FROM TAlumno a
            JOIN TCarreraProfesional cp ON a.cod_cp = cp.codigoCP
            WHERE a.fecha_ingreso_U > '2021-01-01'
            AND a.color != 'Rojo'
            AND a.edad BETWEEN 18 AND 25
            ORDER BY a.AP, a.Nom
        """)
        alumnos = cursor.fetchall()
        return jsonify(alumnos)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port)