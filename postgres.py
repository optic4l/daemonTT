import sys
import psycopg2

print(sys.executable)

def insert_postgres(data):
    conexion = psycopg2.connect(
    host="18.204.7.51",
    database="Tesis4",
    user="postgres",
    password="admin"
    )

    # Crear un cursor
    cursor = conexion.cursor()
    
    consulta = '''
            INSERT INTO "ValoresSensor" ("IdSensorV", "ValorMedidoS", "EstadoS", "IdKpi FK")
            VALUES (%s, %s, %s, %s)
            ON CONFLICT ("IdSensorV") DO UPDATE
            SET "ValorMedidoS" = EXCLUDED."ValorMedidoS";
        '''
    
    for tupla in data:
        cursor.execute(consulta, tupla)

    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    cursor.close()
    conexion.close()
    