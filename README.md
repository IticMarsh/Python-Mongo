# CRUD de Películas

Este es un CRUD (Create, Read, Update, Delete) para gestionar películas utilizando Python con FastAPI y MongoDB.

## Requisitos

- Python 3.x
- MongoDB
- Paquetes Python: `fastapi`, `pymongo`

## Estructura del Proyecto

- `db/`: Carpeta que contiene el cliente de MongoDB y la configuración de la base de datos.
- `model/`: Carpeta que contiene la definición del modelo de datos.
- `schema/`: Carpeta que contiene los esquemas de datos.
- `main.py`: Archivo principal que contiene la lógica de la aplicación.

## Funcionamiento

1. **Crear una película**: 
    - Para agregar una nueva película, se utiliza la función `insert_film` pasando los datos de la película como parámetro. Esto insertará los datos en la base de datos MongoDB y devolverá el ID de la película recién creada.

2. **Obtener una película por ID**:
    - Utilizando la función `get_film`, se puede obtener una película específica proporcionando su ID como parámetro. Esto recuperará los datos de la película desde la base de datos y los devolverá como un objeto JSON.

3. **Actualizar una película**:
    - Para actualizar una película existente, se utiliza la función `update_film`, pasando el ID de la película a actualizar y los nuevos datos de la película. Esto actualizará los datos en la base de datos y devolverá la película actualizada.

4. **Eliminar una película**:
    - Utilizando la función `delete_film`, se puede eliminar una película proporcionando su ID como parámetro. Esto eliminará la película de la base de datos.

5. **Listar todas las películas**:
    - La función `list_films` se encarga de listar todas las películas almacenadas en la base de datos. Devuelve una lista de todas las películas en formato JSON.




