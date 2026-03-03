from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pokemon(BaseModel):
    id: int
    name: str
    hp: int
    attack: int
    vivo: bool

p1=Pokemon(id=1, name="Gengar", hp=60, attack=65, vivo=True),
p2=Pokemon(id=2, name="Charizard", hp=78, attack=84, vivo=True),               
p3=Pokemon(id=3, name="Pikachu", hp=35, attack=55, vivo=True),
p4=Pokemon(id=4, name="Mewtwo", hp=106, attack=110, vivo=True),
p5=Pokemon(id=5, name="Bulbasaur", hp=45, attack=49, vivo=True),
p6=Pokemon(id=6, name="Squirtle", hp=44, attack=48, vivo=True),
p7=Pokemon(id=7, name="Raichu", hp=60, attack=90, vivo=True),
p8=Pokemon(id=8, name="Eevee", hp=55, attack=55, vivo=True),
p9=Pokemon(id=9, name="Snorlax", hp=160, attack=110, vivo=True),
p10=Pokemon(id=10, name="Togepi", hp=35, attack=20, vivo=True)

new_pokemon:list[Pokemon] = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

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

@app.get("/allpokemon/")
def show_all_pokemon():
    return new_pokemon

@app.get("/onepokemon/")
def show_one_pokemon(pos:int=0):
    return new_pokemon[pos]

@app.get ("/pokemon/")
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
