import datetime
import psycopg2

def crear_id_conversacion(db_host: str, db_port: int, db_user: str, db_pass: str):
    """
    Crea una nueva conversación en la base de datos y devuelve su ID.

    Argumentos:
    - db_host (str): El host de la base de datos.
    - db_port (str): El puerto de la base de datos.
    - db_user (str): El nombre de usuario de la base de datos.
    - db_pass (str): La contraseña de la base de datos.

    Retorna:
    - int, ID de la conversación creada.
    """

     # Genera fecha y horas actuales
    fecha_hora_actual = datetime.datetime.now()
    fecha = str(fecha_hora_actual.strftime("%Y-%m-%d %H:%M"))


    # Conecta a la base de datos y creación de la conversación introduciendo la fecha anterior
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_pass)

    cursor = conn.cursor()
    cursor.execute('''INSERT INTO conversaciones (fecha_hora_inicio) VALUES (%s)''', (fecha,))

    cursor.execute('''SELECT MAX(id_conversacion) FROM conversaciones''')
    id_conversacion = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    
    return id_conversacion

def guardar_mensajes_bd(entrada: str, salida: str, id_conversacion: int, db_host: str, db_port: int, db_user: str, db_pass: str):
    """
    Guarda el mensaje del usuario y de la IA en la base de datos.

    Argumentos:
    - entrada (str): El mensaje de entrada del usuario.
    - salida (str): El mensaje de salida del sistema.
    - id_conversacion (int): El ID de la conversación asociada a los mensajes.
    - db_host (str): El host de la base de datos.
    - db_port (str): El puerto de la base de datos.
    - db_user (str): El nombre de usuario de la base de datos.
    - db_pass (str): La contraseña de la base de datos.

     Retorna:
    - None.
    """

    conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_pass)

    cursor = conn.cursor()
    cursor.execute('''INSERT INTO mensajes (mssg_user, mssg_gpt, id_conversacion) 
                VALUES  (%s, %s, %s)''', (entrada, salida, id_conversacion))
    conn.commit()
    conn.close()

    

def obtener_historial(db_host: str, db_port: int, db_user: str, db_pass: str, id_conversacion:int):
    """
    Obtiene el historial de mensajes de una conversación específica de la base de datos.

    Argumentos:
    - db_host (str): El host de la base de datos.
    - db_port (str): El puerto de la base de datos.
    - db_user (str): El nombre de usuario de la base de datos.
    - db_pass (str): La contraseña de la base de datos.
    - id_conversacion (int): Clave única de la conversación que se desea mostrar.

    Retorna:
    - Tuple list, conversación completa.
    """

    conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_pass)

    cursor = conn.cursor()
    cursor.execute('''SELECT mssg_user, mssg_gpt FROM mensajes
                    WHERE id_conversacion = %s''', (id_conversacion,))
    results = cursor.fetchall()
    conn.close()
    
    return results

def obtener_historial_completo(db_host: str, db_port: int, db_user: str, db_pass: str):
    """
    Obtiene el histórico de los mensajes de todas las conversaciones de la base de datos.

    Argumentos:
    - db_host (str): El host de la base de datos.
    - db_port (str): El puerto de la base de datos.
    - db_user (str): El nombre de usuario de la base de datos.
    - db_pass (str): La contraseña de la base de datos.

    Retorna:
    - Tuple list, histórico de mensajes.
    """

    conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_pass)

    cursor = conn.cursor()
    cursor.execute('''SELECT mssg_user, mssg_gpt, id_conversacion FROM mensajes''')
    results = cursor.fetchall()
    conn.close()
    
    return results