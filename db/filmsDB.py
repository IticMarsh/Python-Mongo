from db.clientMD import client
from schema import usuari
from datetime import datetime
from bson.objectid import ObjectId
from fastapi import HTTPException
from pymongo.errors import PyMongoError
from model.model import Film


def get_film(film_id):
    db = client()
    try:
        # Convertir el ID en ObjectId
        film_id = ObjectId(film_id)
        
        # Encontrar la película por su ID
        film = db.films.find_one({"_id": film_id})
        
        if not film:
            raise HTTPException(status_code=404, detail="Film not found")
        
        # Convertir el ID en string
        film['_id'] = str(film['_id'])
        
        return {"status": 1, "film": film}
    except Exception as e:
        return {"status": -1, "error": str(e)}

def insert_film(film):
        db = client()

        data_json = {
                "title": film.title,
                "director": film.director,
                "year": film.year,
                "genre": film.genre,
                "rating": film.rating,
                "country": film.country,
                "created_at": datetime.now(),
                "update_at": datetime.now()
            }

        id = db.films.insert_one(data_json).inserted_id

        id_out = str(id)

        return{"status" : "1", "id": id_out}


def update_film(id: str, film: Film):
    db = client()
    try:
        # Convertir el ID en ObjectId
        film_id = ObjectId(id)
        
        # Verificar si la película está en la base de datos
        existing_film = db.films.find_one({"_id": film_id})
        if existing_film is None:
            raise HTTPException(status_code=404, detail="Film not found")
        
        # Actualizar la película
        db.films.update_one({"_id": film_id}, {"$set": {
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genre": film.genre,
            "rating": film.rating,
            "country": film.country,
            "updated_at": datetime.now()
        }})
        
        # Encontrar la película actualizada
        updated_film = db.films.find_one({"_id": film_id})
        updated_film['_id'] = str(updated_film['_id'])  # Convertir a string
        
        return {"status": 1, "film": updated_film}
    except Exception as e:
        return {"status": -1, "error": str(e)}


def list_films():
    db = client()
    try:
        # Buscar películas en la base de datos
        films = list(db.films.find({}))
        if not films:
            raise HTTPException(status_code=404, detail="No films found")
        
        # Iterar todas las películas y convertirlas a strings
        for film in films:
            film['_id'] = str(film['_id'])
        
        return {"status": 1, "films": films}
    except Exception as e:
        return {"status": -1, "error": str(e)}


def delete_film(id: str):
    db = client()
    try:
        # Convertir el ID en ObjectId
        film_id = ObjectId(id)
        
        # Verificar si existe
        existing_film = db.films.find_one({"_id": film_id})
        if existing_film is None:
            raise HTTPException(status_code=404, detail="Film not found")
        
        # Eliminar la película
        db.films.delete_one({"_id": film_id})
        
        return {"status": 1, "message": "Film deleted successfully"}
    except Exception as e:
        return {"status": -1, "error": str(e)}

