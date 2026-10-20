# PoliRestaurante: CRUD con Driver y ORM

Proyecto académico desarrollado en Python para demostrar dos mecanismos de acceso a una base de datos PostgreSQL:

1. Acceso directo mediante el driver `psycopg` y sentencias SQL.
2. Acceso mediante SQLAlchemy ORM y objetos persistentes.

El proyecto utiliza una tabla del modelo de datos de PoliRestaurante y permite ejecutar operaciones CRUD sobre categorías.

## Objetivo

Implementar y comparar dos estrategias de acceso a datos sobre una misma tabla creada manualmente en PostgreSQL:

- CRUD mediante driver.
- CRUD mediante ORM.

Las dos implementaciones trabajan sobre la tabla `categorias` de PoliRestaurante.

## Tecnologías utilizadas

- Python 3.12
- PostgreSQL 18
- Psycopg 3
- SQLAlchemy 2
- Python Dotenv
- Visual Studio Code

## Estructura del proyecto

```text
CRUD_PYTHON_DRIVER_ORM/
├── config/
│   ├── __init__.py
│   └── database.py
├── driver/
│   ├── __init__.py
│   ├── categoria_dao.py
│   └── menu_driver.py
├── orm/
│   ├── __init__.py
│   ├── categoria_dao.py
│   ├── menu_orm.py
│   └── modelos.py
├── sql/
│   └── crear_base_datos.sql
├── .env.example
├── .gitignore
├── main.py
├── probar_conexion.py
├── probar_driver.py
├── probar_orm.py
├── README.md
└── requirements.txt
```

## Modelo de datos

La base de datos y la tabla se crean manualmente mediante PostgreSQL.

### Base de datos

```sql
CREATE DATABASE polirestaurante_crud_python;
```

### Tabla de categorías

```sql
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(300),
    activa BOOLEAN NOT NULL DEFAULT TRUE
);
```

El campo `id` utiliza `SERIAL`, por lo que PostgreSQL genera automáticamente el identificador de cada categoría.

## CRUD mediante driver

La implementación con driver está ubicada en:

```text
driver/categoria_dao.py
```

Utiliza `psycopg` y sentencias SQL escritas directamente:

- `INSERT` para crear categorías.
- `SELECT` para consultar categorías.
- `UPDATE` para actualizar categorías.
- `DELETE` para eliminar categorías.

Métodos implementados:

```python
crear()
obtener_por_id()
obtener_por_nombre()
obtener_todas()
actualizar()
eliminar()
```

El menú interactivo de esta implementación está ubicado en:

```text
driver/menu_driver.py
```

## CRUD mediante ORM

La implementación ORM está ubicada en:

```text
orm/categoria_dao.py
```

Utiliza SQLAlchemy ORM para trabajar con objetos y sesiones, sin escribir directamente las operaciones SQL del CRUD.

La clase `Categoria`, ubicada en `orm/modelos.py`, está mapeada a la tabla `categorias`:

```python
class Categoria(Base):
    __tablename__ = "categorias"
```

Métodos implementados:

```python
crear()
obtener_por_id()
obtener_por_nombre()
obtener_todas()
actualizar()
eliminar()
```

El menú interactivo de esta implementación está ubicado en:

```text
orm/menu_orm.py
```

## Diferencia entre driver y ORM

### Acceso mediante driver

El DAO ejecuta sentencias SQL directamente:

```python
cursor.execute(
    """
    SELECT id, nombre, descripcion, activa
    FROM categorias
    WHERE id = %s;
    """,
    (categoria_id,)
)
```

### Acceso mediante ORM

El DAO trabaja con objetos de Python:

```python
categoria = sesion.get(
    Categoria,
    categoria_id
)
```

Ambas implementaciones acceden a la misma tabla de PostgreSQL, pero utilizan estrategias diferentes.

## Requisitos previos

Antes de ejecutar el proyecto es necesario instalar:

- Python 3.12 o superior.
- PostgreSQL.
- Git.

También debe existir la base de datos y la tabla definidas en:

```text
sql/crear_base_datos.sql
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Riiperk/Trabajo-ORM-PoliRestaurante.git
cd Trabajo-ORM-PoliRestaurante
```

### 2. Crear el entorno virtual

En Windows PowerShell:

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 5. Configurar las variables de entorno

Copiar el archivo de ejemplo:

```powershell
Copy-Item .env.example .env
```

Editar `.env` y configurar la contraseña real de PostgreSQL:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=polirestaurante_crud_python
DB_USER=postgres
DB_PASSWORD=CONTRASENA_REAL
```

El archivo `.env` no debe subirse al repositorio.

## Creación manual de la base de datos

Abrir PostgreSQL:

```powershell
psql -U postgres -h localhost -p 5432 -d postgres
```

Crear la base:

```sql
CREATE DATABASE polirestaurante_crud_python;
```

Conectarse:

```sql
\c polirestaurante_crud_python
```

Crear la tabla:

```sql
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(300),
    activa BOOLEAN NOT NULL DEFAULT TRUE
);
```

Salir:

```sql
\q
```

## Ejecución

Para iniciar la aplicación:

```powershell
python main.py
```

El menú principal permite elegir:

```text
1. CRUD con driver y SQL manual
2. CRUD con SQLAlchemy ORM
0. Salir
```

Cada implementación incluye las siguientes operaciones:

```text
1. Crear categoría
2. Listar categorías
3. Consultar categoría por ID
4. Actualizar categoría
5. Eliminar categoría
0. Regresar al menú principal
```

## Pruebas

### Probar conexión

```powershell
python probar_conexion.py
```

### Probar CRUD con driver

```powershell
python probar_driver.py
```

### Probar CRUD con ORM

```powershell
python probar_orm.py
```

### Verificar sintaxis

```powershell
python -m compileall config driver orm main.py probar_conexion.py probar_driver.py probar_orm.py
```

## Arquitectura

```text
Menú de consola
       |
       v
DAO Driver o DAO ORM
       |
       v
PostgreSQL
       |
       v
Tabla categorias
```

## Conclusiones

El proyecto demuestra que una misma tabla puede gestionarse mediante dos enfoques:

- El driver proporciona control directo sobre las consultas SQL.
- El ORM permite trabajar mediante clases, objetos y sesiones.

La separación de cada estrategia en su propio DAO facilita la comparación, el mantenimiento y la comprensión de las responsabilidades de acceso a datos.

## Autor

Riiperk

Proyecto académico de Desarrollo de Aplicaciones Web.