## PROYECTO FINAL V***IA***JANDO

Este proyecto consiste en una aplicación web que utiliza un modelo de lenguaje de inteligencia artificial (IA) para simular conversaciones de chat en tiempo real. La aplicación permite a los usuarios interactuar con un asistente de viajes virtual para obtener recomendaciones y sugerencias sobre destinos turísticos.

### Características

- **Asistente de Viajes Virtual**: Utiliza un modelo de lenguaje de IA para simular conversaciones realistas y proporcionar recomendaciones personalizadas a los usuarios sobre destinos turísticos, actividades y más.
- **Base de Datos en la Nube**: La aplicación se conecta a una base de datos alojada en Google Cloud para almacenar todas las conversaciones de manera segura y escalable.
- **Historial de Conversaciones**: Permite a los usuarios acceder al historial completo de sus conversaciones pasadas, identificadas por un ID único de conversación.


### Estructura de carpetas

- **src**: Contiene los archivos fuente de la aplicación.
  - `01_crear_bd.py`: Script para crear la base de datos y las tablas necesarias.
  - `02_api.py`: API de la aplicación que gestiona las solicitudes de los usuarios y las respuestas del chatbot.
  - `config.py`: Archivo de configuración con información sensible como credenciales de base de datos y claves de API.
  - `funciones.py`: Módulo con funciones auxiliares para interactuar con la base de datos.
- **static**: Contiene los archivos estáticos de la interfaz de usuario.
  - `index.html`: Página HTML que muestra la interfaz de chat para interactuar con el asistente virtual.

### Archivos y Funcionalidades

#### `01_crear_bd.py`

Este archivo contiene un script de Python para crear la base de datos y las tablas necesarias para almacenar las conversaciones y mensajes de la aplicación.

#### `02_api.py`

Este archivo implementa la API de la aplicación utilizando el framework FastAPI. Proporciona las siguientes rutas:

- **/**: Página principal que muestra la interfaz de chat para los usuarios.
- **/user_input**: Ruta para recibir la entrada del usuario y devolver la respuesta del chatbot.
- **/historial**: Ruta para obtener el historial de mensajes de una conversación específica. 
- **/historial_completo**: Ruta para obtener el historial completo de mensajes de todas las conversaciones.

#### `config.py`

Archivo de configuración que contiene información sensible como credenciales de base de datos y claves de API.

#### `funciones.py`

Módulo con funciones auxiliares para interactuar con la base de datos. Incluye funciones para crear una nueva conversación, guardar mensajes en la base de datos y recuperar el historial de mensajes.

#### `index.html`

Página HTML que muestra la interfaz de chat para interactuar con el asistente virtual. Utiliza JavaScript para enviar mensajes al servidor y recibir respuestas del chatbot en tiempo real.


### Requisitos

- Python 3.x
- PostgreSQL
- Bibliotecas Python: psycopg2, fastapi, uvicorn, openai, pydantic
- BBDD alojada en Google Cloud.

### Instrucciones de Uso

1. Clonar el repositorio del proyecto: 

    `git clone https://github.com/JavierCalderon94/Proyecto_Final_vIAjando`
2. Completar `config.py.`

    Antes de poder ejecutar cualquier script del proyecto, será necesario cumplimentar modificar el formarto del documento `config.py` de ".txt" a ".py" y cumplimentarlo ya que en éste están recopiladas todas las claves necesarias para conectar con ChatGPT y Google Cloud.
3. Ejecutar el script `01_crear_bd.py` para crear la base de datos y las tablas necesarias.
4. Ejecutar el script `02_api.py` para iniciar el servidor de la aplicación.
5. Acceder a la página principal en un navegador web. Ruta de acceso predeterminada: http://localhost:8000/
6. Interacción con el chatbot:

    Una vez que el chatbot se esté ejecutando, puedes interactuar con él escribiendo mensajes en la consola. El chatbot responderá a tus preguntas y solicitudes de forma automática.

    Ejemplos de uso:

    - ¿Qué me recomiendas para un viaje a París en agosto?
    - ¿Cuánto cuesta un vuelo a Roma desde Madrid?
    - ¿Qué hoteles hay en Barcelona que sean cercanos a la playa?



#### ¡Espero que disfrutes utilizando este chatbot para planificar tus viajes!
