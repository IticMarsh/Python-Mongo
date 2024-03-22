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
    return filmsDB.delete_film(id)

