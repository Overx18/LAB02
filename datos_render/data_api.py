from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos desde variables de entorno
'''DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('PORT')
}'''

def get_db_connection():
    return mysql.connector.connect(
            host="junction.proxy.rlwy.net",   # Por ejemplo, "db.railway.app"
            user="root",           # El usuario de tu base de datos
            password="pIlIsuQhQMjADoGiJiflkvwcdZXEWxOm",    # La contraseña de tu base de datos
            database="bd_universidad",
            port="54785"  # El nombre de tu base de datos
        )


# Ruta de prueba/estado
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

# Obtener todas las carreras
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

# Obtener conteo de alumnos por carrera
@app.route('/api/alumnos/conteo')
def get_alumnos_conteo():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT cp.nomCP, COUNT(a.Código_alumno) as total_alumnos
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

# Obtener alumnos filtrados
@app.route('/api/alumnos/filtrados')
def get_alumnos_filtrados():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT 
                a.Código_alumno,
                a.AP,
                a.Nom,
                a.edad,
                cp.nomCP,
                a.fecha_ingreso_U
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

# Manejo de errores
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port)