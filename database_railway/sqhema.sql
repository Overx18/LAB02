CREATE TABLE TCarreraProfesional (
    codigoCP VARCHAR(10) PRIMARY KEY,
    nomCP VARCHAR(100),
    Fecha_creacion DATE,
    observaciones TEXT
);

CREATE TABLE TAlumno (
    Código_alumno VARCHAR(10) PRIMARY KEY,
    AP VARCHAR(50),
    Nom VARCHAR(50),
    edad INT,
    sexo CHAR(1),
    peso DECIMAL(5,2),
    talla DECIMAL(5,2),
    color VARCHAR(20),
    prov VARCHAR(50),
    cod_cp VARCHAR(10),
    fecha_ingreso_U DATE,
    FOREIGN KEY (cod_cp) REFERENCES TCarreraProfesional(codigoCP)
);