import pandas as pd
import requests

# Configura tus credenciales y URL de la API de WhatsApp aquí
WHATSAPP_API_URL = "https://graph.facebook.com/v12.0/201848473684/messages" #here you change your link for the link tht whatsapp bring you
TOKEN = "here you put the key"
#esta parte encia un mensaje con la plantilla que se crea en whatsapp business
def enviar_mensaje_plantilla_whatsapp(telefono, plantilla_nombre):
    headers = { 
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": telefono,
        "type": "template",
        "template": {
            "namespace": "tu_namespace_aquí",
            "name": plantilla_nombre,
            "language": {
                "code": "es_ES",
                "policy": "deterministic"
            }
        }
    }

    response = requests.post(WHATSAPP_API_URL, headers=headers, json=data)
    return response

#Con Pandas, leemos el archivo CSV y podemos extraer el numero celular de los clientes
def leer_numeros_celular_y_enviar_mensaje(archivo_csv):
    ruta_completa_csv = f'/app/data/{archivo_csv}'
    df = pd.read_csv(ruta_completa_csv, encoding='utf-8', sep=';')

    for numero in df['Teléfono']:
        print(f"Enviando mensaje a {numero}...")
        respuesta = enviar_mensaje_plantilla_whatsapp(numero, "inspeccion_notificacion")
        print(f"Respuesta: {respuesta.status_code}, {respuesta.text}")

leer_numeros_celular_y_enviar_mensaje('MAILING.csv')


