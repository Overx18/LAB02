import mysql.connector
import random
from datetime import datetime, timedelta

def generar_datos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="jricastica",
        password="123",
        database="bd_universidad"
    )
    cursor = conexion.cursor()

    # Generar carreras
    carreras = []
    for i in range(100):
        codigo = f'CP{str(i+1).zfill(3)}'
        nombre = f'Carrera Profesional {i+1}'
        fecha = (datetime(2000, 1, 1) + timedelta(days=i*30)).strftime('%Y-%m-%d')
        carreras.append((codigo, nombre, fecha, f'Observaciones para {nombre}'))

    cursor.executemany(
        "INSERT INTO TCarreraProfesional (codigoCP, nomCP, Fecha_creacion, observaciones) VALUES (%s, %s, %s, %s)",
        carreras
    )

    # Generar alumnos
    colores = ['Azul', 'Verde', 'Amarillo', 'Negro', 'Blanco', 'Morado']
    provincias = ['Lima', 'Callao', 'Arequipa', 'Trujillo', 'Cusco']
    
    for i in range(100000):
        codigo = f'A{str(i+1).zfill(6)}'
        apellido = f'Apellido{i+1}'
        nombre = f'Nombre{i+1}'
        edad = random.randint(18, 25)
        sexo = random.choice(['M', 'F'])
        peso = random.uniform(50.0, 90.0)
        talla = random.uniform(1.50, 1.90)
        color = random.choice(colores)
        prov = random.choice(provincias)
        cod_cp = f'CP{str(random.randint(1,100)).zfill(3)}'
        fecha_ingreso = (datetime(2020, 1, 1) + timedelta(days=random.randint(0,1000))).strftime('%Y-%m-%d')

        cursor.execute(
            "INSERT INTO TAlumno VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (codigo, apellido, nombre, edad, sexo, peso, talla, color, prov, cod_cp, fecha_ingreso)
        )

        if i % 1000 == 0:  # Commit cada 1000 registros
            conexion.commit()

    conexion.commit()
    cursor.close()
    conexion.close()

if __name__ == "__main__":
    generar_datos()