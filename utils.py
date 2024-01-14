import json, base64

def obtener_ultimo_objeto(archivo):
    ultimo_objeto = None
    
    for linea in archivo:
        # Decodificar la línea como JSON
        try:
            objeto = json.loads(linea)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            continue

        # Retener el objeto actual como el último
        ultimo_objeto = objeto

    return ultimo_objeto

#funcion para eliminar campos innecesarios
def eliminar_campos(object):
    #eliminar campos innecesarios
    if "uplink_message_f_cnt" in object["fields"]:
        del object["fields"]["uplink_message_f_cnt"]

    if "uplink_message_f_port" in object["fields"]:
        del object["fields"]["uplink_message_f_port"]

    if "uplink_message_rx_metadata_0_channel_index" in object["fields"]:
        del object["fields"]["uplink_message_rx_metadata_0_channel_index"]

    if "uplink_message_rx_metadata_0_timestamp" in object["fields"]:
        del object["fields"]["uplink_message_rx_metadata_0_timestamp"]

    if "uplink_message_settings_data_rate_lora_spreading_factor" in object["fields"]:
        del object["fields"]["uplink_message_settings_data_rate_lora_spreading_factor"]

    if "uplink_message_rx_metadata_0_channel_rssi" in object["fields"]:
        del object["fields"]["uplink_message_rx_metadata_0_channel_rssi"]
    
    if "uplink_message_settings_timestamp" in object["fields"]:
        del object["fields"]["uplink_message_settings_timestamp"]

#Funcion para desencriptar el mensaje
def decoder_payload(object):
    valor = object["fields"]["uplink_message_frm_payload"]
    decoded_payload = base64.b64decode(valor).decode('utf-8')

    object["fields"]["uplink_message_frm_payload"] = int(decoded_payload)
