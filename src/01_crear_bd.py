import psycopg2
from config import db_user, db_pass, db_host, db_port

# Conexión con la base de datos alojada en la nube.
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_pass)

cursor = conn.cursor()


# Generar tabla conversaciones (id_conversacion: clave única para cada hilo de mensajes)
cursor.execute('''CREATE TABLE conversaciones 
               (id_conversacion SERIAL PRIMARY KEY,
               fecha_hora_inicio TEXT NOT NULL)''')

# Generar tabla mensajes (id: clave única para cada pareja de mensaje-respuesta, asociados a una conversación con id_conversación)
cursor.execute('''CREATE TABLE mensajes (
               id SERIAL PRIMARY KEY,
               mssg_user TEXT,
               mssg_gpt TEXT,
               id_conversacion INTEGER REFERENCES conversaciones(id_conversacion))''')

    

conn.commit()
conn.close()
