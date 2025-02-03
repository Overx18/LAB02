from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

DATOS_API_URL = os.getenv('DATOS_API_URL')

@app.route('/', methods=['GET'])
def health_check():
    """Endpoint para verificar que el servicio está funcionando"""
    return jsonify({
        "status": "healthy",
        "service": "business-api"
    })

@app.route('/api/alumnos/conteo', methods=['GET'])
def obtener_conteo_alumnos():
    """Obtiene el conteo de alumnos por carrera y aplica lógica de negocio si es necesario"""
    try:
        response = requests.get(f'{DATOS_API_URL}/api/alumnos/conteo')
        response.raise_for_status()
        datos = response.json()

        datos_ordenados = sorted(datos, key=lambda x: x['total_alumnos'], reverse=True)
        
        return jsonify(datos_ordenados)
    
    except requests.RequestException as e:
        return jsonify({"error": f"Error al obtener datos: {str(e)}"}), 500

@app.route('/api/alumnos/filtrados', methods=['GET'])
def obtener_alumnos_filtrados():
    try:
        response = requests.get(f'{DATOS_API_URL}/api/alumnos/filtrados')
        response.raise_for_status()
        datos = response.json()
        
        print("Datos recibidos:", datos)
        
        return jsonify(datos)
    except requests.RequestException as e:
        return jsonify({"error": f"Error al obtener datos: {str(e)}"}), 500

@app.route('/api/carreras', methods=['GET'])
def obtener_carreras():
    """Obtiene la lista de carreras con información adicional de negocio"""
    try:
        response = requests.get(f'{DATOS_API_URL}/api/carreras')
        response.raise_for_status()
        
        carreras = response.json()
        
        response_conteo = requests.get(f'{DATOS_API_URL}/api/alumnos/conteo')
        response_conteo.raise_for_status()
        
        conteo = {item['carrera']: item['total_alumnos'] 
                 for item in response_conteo.json()}
        
        for carrera in carreras:
            carrera['total_alumnos'] = conteo.get(carrera['nombre'], 0)
            carrera['estado'] = 'Alta demanda' if carrera['total_alumnos'] > 1000 else 'Normal'
        
        return jsonify(carreras)
    
    except requests.RequestException as e:
        return jsonify({"error": f"Error al obtener datos: {str(e)}"}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port)