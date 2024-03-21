from db.clientMD import client
from schema import usuari
from datetime import datetime
from bson.objectid import ObjectId
from fastapi import HTTPException
from pymongo.errors import PyMongoError
from model.model import Film



def get_film(film_id):
    db = client()
    
    film_id = ObjectId(film_id)
    
    film = db.films.find_one({"_id": film_id})
    
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    
    film['_id'] = str(film['_id'])
    
    return film
    
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

     return{"status" : "ok", "id": id_out}



def list_films():
    db = client()
    films = list(db.films.find({}))
    if not films:
        raise HTTPException(status_code=404, detail="No films found")
    
    # Convertir ObjectId a cadena en cada documento
    for film in films:
        film['_id'] = str(film['_id'])
    
    return films





def update_film(id: str, film: Film):
    db = client()
    
    # Convierte el id a un ObjectId
    film_id = ObjectId(id)
    
    # Verifica si la película existe
    existing_film = db.films.find_one({"_id": film_id})
    if existing_film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    
    # Actualiza la película en la base de datos
    db.films.update_one({"_id": film_id}, {"$set": film})
        
    # Devuelve la película actualizada
    updated_film = db.films.find_one({"_id": film_id})
    updated_film['_id'] = str(updated_film['_id'])  # Convierte ObjectId a cadena
    
    return updated_film


