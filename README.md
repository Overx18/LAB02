# LAB02-INSTALACION
### CASTILLO CARRANZA JOSE RICHARD
## 1. Crear un repositorio en GitHub que incluya el zip brindado
## 2. Para la capa de presentacion:
##### a. En vercel.com. loguear su GitHub, seleccionar el repositorio respectivo, crear un proyecto
##### b. Subir el arhivo .env de la carpeta: presentacion_vercel
##### c. Configurar el Root Directory: presentacion_vercel
##### d. Configurar el Build Comand: pip install -r requirements.txt
##### f. Esperar a que este Desplegado
## 3. Para la capa de logica de negocio:
##### a. En render.com loguear su GitHub, seleccionar el repositorio respectivo, crear un proyecto  y despues crear un Web Service  que se llame LAB02_NEGOCIO
##### b. Subir el arhivo .env de la carpeta negocio_render
##### c. Configurar el Root Directory: negocio_render
##### d. Configurar el Build Comand: pip install -r requirements.txt
##### e. Configurar el Start Comand: gunicorn api:app
##### f. Esperar a que este Desplegado
## 4. Para la capa de acceso de datos:
##### a. En render.com crear otro Web Service  que se llame LAB02_DATOS
##### b. Subir el arhivo .env de la carpeta: datos_vercel
##### c. Configurar el Root Directory: datos_render
##### d. Configurar el Build Comand: pip install -r requirements.txt
##### e. Configurar el Start Comand: gunicorn data_api:app
##### f. Esperar a que este Desplegado
## 5. Para la capa de base de datos:
##### a. En railway, crear un proyecto MySql
##### b. Eliminar todas las variables de entorno creada por railway, luego insertar el .env de la carpeta: database_railway
##### c. Ir a Settings a Networking eliminar ese dominio y crear uno nuevo: junction.proxy.rlwy.net  y con Custom Port: 54784 ##### d. Redesplegar
##### e. Ir a la carpeta: database_railway y ejecutar las 4 consultas del archivo schema.sql
##### f. Ir a la carpeta: database_railwayy ejecutar generar.py(genera 100000 datos en el server mysql)
