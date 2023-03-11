from db import get_connection

#Consultar base de datos
'''try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("call consultar_alumnos()")
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
    connection.close()

except Exception as ex:
    print(ex)'''

#Consultar uno
'''try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("call consultar_alumno(%s)", (2))
        resultset = cursor.fetchone()
        for row in resultset:
            print(row)
    connection.close()

except Exception as ex:
    print(ex)'''

# Insertar
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("call insertar_alumno(%s, %s, %s)", ("nombre", "apellidos", "correo"))
        resultset = cursor.fetchone()
    connection.commit()
    connection.close()

except Exception as ex:
    print(ex)