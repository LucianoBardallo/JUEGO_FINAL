import sqlite3 as sql

def crear_base():
    """
    Esta funcion sirva para crear la base de datos desde 0
    """
    with sql.connect("clasificacion.db") as conexion:
        conexion.commit()


def crear_tabla():
    """
    Esta funcion sirva para crear una tabla dentro de la base de datos, con los atributos de id, nombre, nivel y score
    """
    with sql.connect("clasificacion.db") as conexion:
        try:
            conexion.execute(
                """CREATE TABLE score(
                    id integer primary key autoincrement,
                    name text,
                    nivel text,
                    score integer
                )"""
            )
        except sql.OperationalError:
            print("La tabla score ya existe")


def insertar_linea(name:str, nivel:str, score:int):
    """
    Esta funcion sirve para ingresar una linea dentro de una tabla

    Parametros: name como str, nivel como str y score como int
    """
    with sql.connect("clasificacion.db") as conexion:
        try:
            conexion.execute(
                "insert into score(name,nivel,score) values (?,?,?)", (name, nivel, score))
            conexion.commit()
        except:
            print("Error")

def leer_lineas(nivel:str):
    """
    Esta funcion se encarga de leer todas lass lineas de la tabla score que compartan la columna nivel

    Parametros: nivel como clave para tomar los datos en la tabla
    """
    with sql.connect("clasificacion.db") as conexion:
        try:
            cursor = conexion.cursor()
            busqueda = "SELECT * FROM score WHERE nivel = ? ORDER BY score DESC LIMIT 50 "
            
            cursor.execute(busqueda,(nivel,))
            datos = cursor.fetchall()
            conexion.commit()
            return datos
        except:
            print("Error")

def eliminar_linea(id:int):
    """
    Esta funcion se encarga de borrar un dato dependiendo del ID

    Parametros: un id del tipo int
    """
    with sql.connect("clasificacion.db") as conexion:
        sentencia = "DELETE FROM score WHERE id=?"
        cursor=conexion.execute(sentencia,(id,))






        