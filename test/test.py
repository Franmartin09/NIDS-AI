import os

def copiar_y_pegar(archivo_origen, archivo_destino):
    try:
        # Abrir el archivo origen en modo lectura
        with open(archivo_origen, 'r') as origen:
            contenido = origen.read()

        # Abrir el archivo destino en modo append usando os.open
        with os.fdopen(os.open(archivo_destino, os.O_APPEND | os.O_WRONLY), 'a') as destino:
            destino.write(contenido)

        print(f"El contenido de {archivo_origen} ha sido copiado y pegado al final de {archivo_destino} exitosamente.")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso
archivo_origen = 'test/atack.json'
archivo_destino = 'zeek/logs/conn.log'
copiar_y_pegar(archivo_origen, archivo_destino)
