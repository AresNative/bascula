import serial
import os
import time

# Configuración del puerto serial
puerto = 'COM3'  # Cambia esto al puerto de tu báscula
baud_rate = 9600  # Configuración de baudios de la báscula

def reiniciar_intelisis_tools():
    """
    Reinicia el programa Intelisis Tools cerrando el proceso si está en ejecución
    y abriéndolo nuevamente.
    """
    try:
        # Cerrar Intelisis Tools si está abierto
        os.system("taskkill /F /IM IntelisisTools.exe")  # Cambia IntelisisTools.exe si el nombre del proceso es diferente
        print("Intelisis Tools cerrado.")

        # Esperar un momento antes de reiniciar
        time.sleep(2)

        # Reiniciar Intelisis Tools
        os.system("start IntelisisPOSToolV2.exe")  # Asegúrate de que esté en la PATH o incluye la ruta completa
        print("Intelisis Tools reiniciado.")
    except Exception as e:
        print(f"Error al reiniciar Intelisis Tools: {e}")

def leer_peso():
    """
    Lee el peso desde la báscula y guarda los datos en un archivo.
    """
    try:
        bascula = serial.Serial(puerto, baud_rate, timeout=1)
        print(f"Conectado a la báscula en {puerto} a {baud_rate} baudios")

        with open('peso.txt', 'a') as archivo:  # Archivo para guardar el peso
            while True:
                datos = bascula.readline().decode('utf-8').strip()
                if datos:  # Si hay datos recibidos
                    print(f"Peso recibido: {datos}")
                    archivo.write(f"{datos}\n")  # Guardar el peso en el archivo
                    archivo.flush()
    except serial.SerialException as e:
        print(f"Error de conexión: {e}")
    except KeyboardInterrupt:
        print("Programa interrumpido manualmente.")
    finally:
        if 'bascula' in locals() and bascula.is_open:
            bascula.close()
        print("Conexión cerrada.")

# Ejecución del programa
if __name__ == "__main__":
    print("Iniciando programa...")
    reiniciar_intelisis_tools()  # Llama al reinicio de Intelisis Tools
    leer_peso()  # Inicia la lectura de la báscula
