import json, time, sys
from influx import influx_process
from postgres import insert_postgres
from utils import eliminar_campos, decoder_payload, obtener_ultimo_objeto

print(sys.executable)

# Ruta al archivo que contiene las métricas
archivo_metricas = "/etc/telegraf/metrics.json"

while True:
    # Llamar a la función para obtener el último objeto
    ultimo_objeto = obtener_ultimo_objeto(archivo_metricas)
    eliminar_campos(ultimo_objeto)
    decoder_payload(ultimo_objeto)
    influx_process(ultimo_objeto)

    # Imprimir el último objeto (si existe)
    if ultimo_objeto:
        print("Último objeto:")
        print(json.dumps(ultimo_objeto, indent=2))
    else:
        print("No se encontraron objetos en el archivo.")

    data = influx_process()
    insert_postgres(data)

    time.sleep(5)


    