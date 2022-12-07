import sqlite3 as sql

def crear_base():
    with sql.connect("clasificacion.db") as conexion:
        conexion.commit()


def crear_tabla():
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


def insertar_linea(name, nivel, score):
    with sql.connect("clasificacion.db") as conexion:
        try:
            conexion.execute(
                "insert into score(name,nivel,score) values (?,?,?)", (name, nivel, score))
            conexion.commit()
        except:
            print("Error")

def leer_lineas(nivel):
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

def eliminar_linea():
    with sql.connect("clasificacion.db") as conexion:
        sentencia = "DELETE FROM score WHERE id=?"
        cursor=conexion.execute(sentencia,(26,))






        