
CREATE DATABASE IF NOT EXISTS personas;

USE personas;

CREATE TABLE IF NOT EXISTS personas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255),
    correo VARCHAR(255),
    fecha DATE
);

