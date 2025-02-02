-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS bd_universidad;
USE bd_universidad;

-- Crear tabla de Carreras Profesionales
CREATE TABLE TCarreraProfesional (
    codigoCP VARCHAR(10) PRIMARY KEY,
    nomCP VARCHAR(100) NOT NULL,
    Fecha_creacion DATE NOT NULL,
    observaciones TEXT
);

-- Crear tabla de Alumnos
CREATE TABLE TAlumno (
    Código_alumno VARCHAR(10) PRIMARY KEY,
    AP VARCHAR(50) NOT NULL,
    Nom VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    sexo CHAR(1) NOT NULL,
    peso DECIMAL(5,2),
    talla DECIMAL(5,2),
    color VARCHAR(20),
    prov VARCHAR(50),
    cod_cp VARCHAR(10) NOT NULL,
    fecha_ingreso_U DATE NOT NULL,
    FOREIGN KEY (cod_cp) REFERENCES TCarreraProfesional(codigoCP)
);

-- Crear índices para mejorar el rendimiento
CREATE INDEX idx_fecha_ingreso ON TAlumno(fecha_ingreso_U);
CREATE INDEX idx_color ON TAlumno(color);
CREATE INDEX idx_edad ON TAlumno(edad);