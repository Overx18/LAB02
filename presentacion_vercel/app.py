# Capa 1: Capa de Presentación (UI)

from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
NEGOCIO_API = os.getenv('NEGOCIO_API_URL', 'http://localhost:5000')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alumnos-por-carrera')
def alumnos_por_carrera():
    try:
        response = requests.get(f'{NEGOCIO_API}/api/alumnos/conteo')
        data = response.json()
        print("Datos recibidos:", data)  # Para debug
        return render_template('alumnos_por_carrera.html', data=data)
    except requests.RequestException as e:
        return render_template('error.html', error=str(e))
    

@app.route('/alumnos-filtrados')
def alumnos_filtrados():
    try:
        response = requests.get(f'{NEGOCIO_API}/api/alumnos/filtrados')
        data = response.json()
        print("Datos filtrados:", data)  # Para debug
        return render_template('alumnos_filtrados.html', data=data)
    except requests.RequestException as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)