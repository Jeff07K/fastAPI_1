from fastapi import FastAPI
from paydantic import BaseModel

app = FastAPI()

class Pokemon(BaseModel):
    id: int
    name: str
    hp: int
    attack: int
    vivo: bool

new_pokemon_db = [Pokemon(id=1, name="Gengar", hp=60, attack=65, vivo=True),
                   Pokemon(id=2, name="Charizard", hp=78, attack=84, vivo=True),
                   Pokemon(id=3, name="Pikachu", hp=35, attack=55, vivo=True),
                   Pokemon(id=4, name="Mewtwo", hp=106, attack=110, vivo=True),
                   Pokemon(id=5, name="Bulbasaur", hp=45, attack=49, vivo=True),
                   Pokemon(id=6, name="Squirtle", hp=44, attack=48, vivo=True)]

pokemon_db = [{"name":"Gengar"},
              {"name":"charizar"},
              {"name":"pikachu"},
              {"name":"Mewtwo"},
              {"name":"Bulbasaur"},
              {"name":"Squirtle"},
              {"name":"raichu"},
              {"name":"Eevee"},
              {"name":"Snorlax"},
              {"name":"Togepi"}]

@app.get ("/pokemoncho/")
def show_pokemon(skip: int = 0, limit: int = 3):
    return pokemon_db[skip:skip+limit]

@app.get("/hola")
def hello():
    return {"hola": "Aqui vamos de nuevo"}

@app.get("/jeff07k")
def jeff07k():
    return {"jeff07k": "Hola"} 

@app.get("/suma/{a}/{b}")
def suma(a:int,b:int):
    res = int(a) + int(b)
    return {"la suma da": res}

@app.get("/edad/{nombre}/{fecha_nacimiento}")    
def edad(nombre, fecha_nacimiento): 
    from datetime import datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return {"Usuario": nombre, "edad": edad}
