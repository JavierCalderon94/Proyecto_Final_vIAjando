from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from openai import OpenAI
from pydantic import BaseModel
import funciones as f
from config import db_user, db_pass, db_host, db_port, key,  conversacion_estado

# Ubicar en directorio principal
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Crear la clave única que se mantendrá en esta conversación
id_conversacion = f.crear_id_conversacion(db_host, db_port, db_user, db_pass) # Crear la id de la conversación que se mantendrá en esta conversación


# Inicializar el cliente de OpenAI y FastAPI
client = OpenAI(api_key=key)
app = FastAPI()


# Montar la carpeta estática para los archivos HTML
app.mount("/static", StaticFiles(directory="static"), name="index.html")
templates = Jinja2Templates(directory="static")


# Ruta principal que devuelve el archivo HTML sobre el que el usuario podrá interactuar
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Definir el modelo de entrada para el usuario
class UserInput(BaseModel):
    input_text: str


# Ruta para recibir la entrada del usuario y devolver la respuesta del chatbot
@app.post("/user_input")
async def imput_respuesta(user_input: UserInput):
    try:
        entrada = user_input.input_text

        # Agregar la entrada del usuario al historial
        conversacion_estado["historial"].append({"role": "user", "content": entrada})

        # Obtener la respuesta del modelo de lenguaje
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": conversacion_estado["rol"]},
                {"role": "user", "content": entrada}
            ] + conversacion_estado["historial"])
        salida = completion.choices[0].message.content

        # Agregar la respuesta al historial
        conversacion_estado["historial"].append({"role": "system", "content": salida})

        # Guardar la entrada del usuario y la respuesta en la base de datos
        f.guardar_mensajes_bd(entrada, salida, id_conversacion, db_host, db_port, db_user, db_pass)

        print("Entrada del usuario:", entrada)
        print("Respuesta GPT:", salida)
        
        # Devolver un mensaje de confirmación al usuario
        return {"message": "Entrada del usuario recibida correctamente", "output": salida}
        
    #Devuelve un mensaje de error en caso de que falle
    except Exception as e:
        raise HTTPException(status_code=500, detail= '''    Error inesperado, revise la estructura de los datos 
                                                            y las conexiones con la IA y la BBDD''' + str(e))



# Ruta para obtener el historial de mensajes de una conversación específica
@app.get("/historial")
async def historial_mensajes(id_conv: int = None):

    try:

        # Si se proporciona un ID de conversación, obtener el historial de esa conversación
        if id_conv:
            results = f.obtener_historial(db_host, db_port, db_user, db_pass, id_conv)
        
        # Si no se proporciona ningún ID de conversación, obtener el historial de la conversación actual
        else:
            results = f.obtener_historial(db_host, db_port, db_user, db_pass, id_conversacion)

        return results
    
    #Devuelve un mensaje de error en caso de que falle
    except Exception as e:
        raise HTTPException(status_code=500, detail= '''    Error inesperado, revise la ID 
                                                            y las conexiones con la BBDD''' + str(e))



# Ruta para obtener el historial completo de mensajes de todas las conversaciones
@app.get("/historial_completo")
async def historial_mensajes_completo():

    try:
        results = f.obtener_historial_completo(db_host, db_port, db_user, db_pass)
        return results
    
    #Devuelve un mensaje de error en caso de que falle
    except Exception as e:
        raise HTTPException(status_code=500, detail= '''    Error inesperado, revise las conexiones con la BBDD''' + str(e))
    

    
# Iniciar el servidor de la aplicación, únicamente cuando se ejecute como script principal
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


