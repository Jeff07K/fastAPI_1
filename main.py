from fastapi import FastAPI

app = FastAPI()

@app.get("/hola")
def hello():
    return {"hola": "Aqui vamos de nuevo"}

@app.get("/jeff07k")
def jeff07k():
    return {"jeff07k": "Hola"} 

@app.get("/suma/{a}/{b}")
def suma(a,b):
    res = int(a) + int(b)
    return {"la suma da": res}

@app.get("/edad/{nombre}/{fecha_nacimiento}")    
def edad(nombre, fecha_nacimiento): 
    from datetime import datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return {"Usuario": nombre, "edad": edad}
