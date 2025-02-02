import mysql.connector
import random
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos
db_config = {
    'host': os.getenv('mysql.railway.internal'),
    'user': os.getenv('root'),
    'password': os.getenv('pIlIsuQhQMjADoGiJiflkvwcdZXEWxOm'),
    'database': os.getenv('bd_universidad')
}

def generar_carreras():
    carreras = []
    nombres_carreras = [
        'Ingeniería de Sistemas', 'Medicina Humana', 'Derecho', 
        'Psicología', 'Ingeniería Civil', 'Administración',
        'Contabilidad', 'Economía', 'Arquitectura', 'Odontología',
        'Enfermería', 'Ingeniería Industrial', 'Ingeniería Electrónica',
        'Ingeniería Mecánica', 'Ingeniería Química', 'Ingeniería Ambiental',
        'Ingeniería de Software', 'Ingeniería de Telecomunicaciones',
        'Ingeniería Biomédica', 'Ingeniería Aeronáutica', 'Ingeniería Minera',
        'Ingeniería de Petróleos', 'Ingeniería Agroindustrial',
        'Ingeniería Agronómica', 'Ingeniería de Alimentos',
        'Ciencias de la Computación', 'Matemáticas', 'Física', 'Química',
        'Biología', 'Biotecnología', 'Genética', 'Farmacia y Bioquímica',
        'Ciencias de la Nutrición', 'Veterinaria', 'Ciencias Políticas',
        'Relaciones Internacionales', 'Criminología', 'Antropología',
        'Arqueología', 'Sociología', 'Trabajo Social', 'Historia', 'Filosofía',
        'Lingüística', 'Literatura', 'Educación Inicial', 'Educación Primaria',
        'Educación Secundaria', 'Educación Especial', 'Pedagogía',
        'Comunicación Social', 'Periodismo', 'Publicidad y Marketing',
        'Diseño Gráfico', 'Diseño de Modas', 'Diseño Industrial',
        'Cinematografía', 'Fotografía', 'Música', 'Artes Escénicas',
        'Danza', 'Teatro', 'Artes Plásticas', 'Administración Hotelera',
        'Gastronomía', 'Turismo', 'Hotelería', 'Ciencias del Deporte',
        'Ciencias del Mar', 'Oceanografía', 'Astronomía', 'Meteorología',
        'Geología', 'Geografía', 'Estadística', 'Actuaría', 'Administración Pública',
        'Logística y Transporte', 'Negocios Internacionales',
        'Mercadotecnia', 'Comercio Exterior', 'Finanzas',
        'Gestión y Administración de Empresas', 'Ciencias Actuariales',
        'Terapia Ocupacional', 'Terapia Física y Rehabilitación',
        'Radiología', 'Optometría', 'Bioinformática', 'Nanotecnología',
        'Ciencias Forenses', 'Seguridad y Salud en el Trabajo',
        'Desarrollo de Videojuegos', 'Inteligencia Artificial',
        'Ciberseguridad', 'Agronegocios', 'Ecología', 'Energías Renovables',
        'Gestión Cultural', 'Gestión Ambiental'
    ]
    
    for i in range(100):
        codigo = f'CP{str(i+1).zfill(3)}'
        nombre = f'{nombres_carreras[i % len(nombres_carreras)]} {i+1}'
        fecha = (datetime(2000, 1, 1) + timedelta(days=i*30)).strftime('%Y-%m-%d')
        observaciones = f'Observaciones para {nombre}'
        carreras.append((codigo, nombre, fecha, observaciones))
    
    return carreras

def generar_alumnos(num_alumnos, carreras):
    alumnos = []
    nombres = ['Juan', 'Ana', 'Pedro', 'María', 'Luis', 'Carmen']
    apellidos = ['García', 'Pérez', 'López', 'Rodríguez', 'Martínez']
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
        cod_cp = random.choice(carreras)[0]  # Código de carrera aleatorio
        fecha_ingreso = (datetime(2020, 1, 1) + 
                        timedelta(days=random.randint(0,1000))).strftime('%Y-%m-%d')
        
        alumnos.append((codigo, apellido, nombre, edad, sexo, peso, 
                       talla, color, prov, cod_cp, fecha_ingreso))
    
    return alumnos

def insertar_datos():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Insertar carreras
        carreras = generar_carreras()
        cursor.executemany(
            "INSERT INTO TCarreraProfesional (codigoCP, nomCP, Fecha_creacion, observaciones) "
            "VALUES (%s, %s, %s, %s)",
            carreras
        )
        
        # Insertar alumnos
        alumnos = generar_alumnos(100000, carreras)  # Generar 100,000 alumnos
        for i in range(0, len(alumnos), 1000):  # Insertar en lotes de 1000
            cursor.executemany(
                "INSERT INTO TAlumno (Código_alumno, AP, Nom, edad, sexo, peso, "
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