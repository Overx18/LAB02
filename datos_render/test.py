import mysql.connector
from mysql.connector import Error

def test_connection():
    try:
        # Reemplaza los valores por los de tu configuración de Railway
        connection = mysql.connector.connect(
            host="junction.proxy.rlwy.net",   # Por ejemplo, "db.railway.app"
            user="root",           # El usuario de tu base de datos
            password="pIlIsuQhQMjADoGiJiflkvwcdZXEWxOm",    # La contraseña de tu base de datos
            database="bd_universidad",
            port="54784"  # El nombre de tu base de datos
        )
        
        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
    
    except Error as e:
        print(f"Error al conectar: {e}")
    
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")

# Llamar a la función
test_connection()
