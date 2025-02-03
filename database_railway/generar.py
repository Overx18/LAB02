import mysql.connector
import random
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('PORT')
}

def generar_carreras():
    carreras = []
    nombres_carreras = [
        'Ingenieria de Sistemas', 'Medicina Humana', 'Derecho', 
        'Psicologia', 'Ingenieria Civil', 'Administracion',
        'Contabilidad', 'Economia', 'Arquitectura', 'Odontologia',
        'Enfermeria', 'Ingenieria Industrial', 'Ingenieria Electronica',
        'Ingenieria Mecanica', 'Ingenieria Quimica', 'Ingenieria Ambiental',
        'Ingenieria de Software', 'Ingenieria de Telecomunicaciones',
        'Ingenieria Biomedica', 'Ingenieria Aeronautica', 'Ingenieria Minera',
        'Ingenieria de Petroleos', 'Ingenieria Agroindustrial',
        'Ingenieria Agronómica', 'Ingenieria de Alimentos',
        'Ciencias de la Computacion', 'Matematicas', 'Fisica', 'Quimica',
        'Biologia', 'Biotecnologia', 'Genetica', 'Farmacia y Bioquimica',
        'Ciencias de la Nutricion', 'Veterinaria', 'Ciencias Politicas',
        'Relaciones Internacionales', 'Criminologia', 'Antropologia',
        'Arqueologia', 'Sociologia', 'Trabajo Social', 'Historia', 'Filosofia',
        'Lingüistica', 'Literatura', 'Educacion Inicial', 'Educacion Primaria',
        'Educacion Secundaria', 'Educacion Especial', 'Pedagogia',
        'Comunicacion Social', 'Periodismo', 'Publicidad y Marketing',
        'Diseño Grafico', 'Diseño de Modas', 'Diseño Industrial',
        'Cinematografia', 'Fotografia', 'Musica', 'Artes Escénicas',
        'Danza', 'Teatro', 'Artes Plasticas', 'Administracion Hotelera',
        'Gastronomia', 'Turismo', 'Hoteleria', 'Ciencias del Deporte',
        'Ciencias del Mar', 'Oceanografia', 'Astronomia', 'Meteorologia',
        'Geologia', 'Geografia', 'Estadistica', 'Actuaria', 'Administracion Publica',
        'Logistica y Transporte', 'Negocios Internacionales',
        'Mercadotecnia', 'Comercio Exterior', 'Finanzas',
        'Gestion y Administracion de Empresas', 'Ciencias Actuariales',
        'Terapia Ocupacional', 'Terapia Fisica y Rehabilitacion',
        'Radiologia', 'Optometría', 'Bioinformatica', 'Nanotecnologia',
        'Ciencias Forenses', 'Seguridad y Salud en el Trabajo',
        'Desarrollo de Videojuegos', 'Inteligencia Artificial',
        'Ciberseguridad', 'Agronegocios', 'Ecologia', 'Energias Renovables',
        'Gestion Cultural', 'Gestion Ambiental'
    ]
    
    for i in range(100):
        codigo = f'CP{str(i+1).zfill(3)}'
        nombre = f'{nombres_carreras[i % len(nombres_carreras)]}'
        fecha = (datetime(2000, 1, 1) + timedelta(days=i*30)).strftime('%Y-%m-%d')
        observaciones = f'Observaciones para {nombre}'
        carreras.append((codigo, nombre, fecha, observaciones))
    
    return carreras

def generar_alumnos(num_alumnos, carreras):
    alumnos = []
    nombres = ['Juan', 'Ana', 'Pedro', 'Maria', 'Luis', 'Carmen']
    apellidos = ['Garcia', 'Perez', 'Lopez', 'Rodriguez', 'Martinez']
    colores = ['Azul', 'Verde', 'Amarillo', 'Negro', 'Blanco', 'Morado', 'Rojo']
    provincias = ['Lima', 'Callao', 'Arequipa', 'Trujillo', 'Cusco']
    
    for i in range(num_alumnos):
        codigo = f'A{str(i+1).zfill(6)}'
        apellido = random.choice(apellidos)
        nombre = random.choice(nombres)
        edad = random.randint(18, 25)
        sexo = random.choice(['M', 'F'])
        peso = round(random.uniform(50.0, 90.0), 2)
        talla = round(random.uniform(1.50, 1.90), 2)
        color = random.choice(colores)
        prov = random.choice(provincias)
        cod_cp = random.choice(carreras)[0] 
        fecha_ingreso = (datetime(2020, 1, 1) + 
                        timedelta(days=random.randint(0,1000))).strftime('%Y-%m-%d')
        
        alumnos.append((codigo, apellido, nombre, edad, sexo, peso, 
                       talla, color, prov, cod_cp, fecha_ingreso))
    
    return alumnos

def insertar_datos():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        carreras = generar_carreras()
        cursor.executemany(
            "INSERT INTO TCarreraProfesional (codigoCP, nomCP, Fecha_creacion, observaciones) "
            "VALUES (%s, %s, %s, %s)",
            carreras
        )
        
        alumnos = generar_alumnos(100000, carreras) 
        for i in range(0, len(alumnos), 1000):
            cursor.executemany(
                "INSERT INTO TAlumno (Codigo_alumno, AP, Nom, edad, sexo, peso, "
                "talla, color, prov, cod_cp, fecha_ingreso_U) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                alumnos[i:i+1000]
            )
            conn.commit()
            print(f"Insertados {i+1000} alumnos...")
        
        print("Datos generados exitosamente")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    insertar_datos()