from typing import Union
from typing import List
from fastapi import FastAPI, HTTPException, status
from model.model import Film
from db import filmsDB
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}




# get all
@app.get("/films/")
def get_films():
    return filmsDB.list_films()




# post film
@app.post("/film/" )
def create_film(film: Film):
    return filmsDB.insert_film(film)


# get by id
@app.get("/film/{id}")
def get_film(id: str):
    return filmsDB.get_film(id)


  

# Put by id
@app.put("/film/{id}")
def update_film(id: str, film: Film):
    return filmsDB.update_film(id, film)


# delete by id
@app.delete("/film/{id}")
async def delete_film(id: str):
    result = films_collection.delete_one({"_id": id})
    if result.deleted_count == 1:
        return {"status": 1, "message": "Film deleted successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film not found")

