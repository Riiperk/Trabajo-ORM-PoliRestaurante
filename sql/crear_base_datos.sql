-- ============================================================
-- Base de datos manual para la actividad de acceso a datos
-- Dominio: PoliRestaurante
-- ============================================================

-- Ejecutar este comando conectado a la base postgres.
CREATE DATABASE polirestaurante_crud_python;

-- Después conectarse manualmente:
-- \c polirestaurante_crud_python

-- Tabla perteneciente al modelo de PoliRestaurante.
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(300),
    activa BOOLEAN NOT NULL DEFAULT TRUE
);