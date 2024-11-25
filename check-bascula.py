import serial
import os
import time

# Configuración del puerto serial
puerto = 'COM1'  # Cambia esto al puerto de tu báscula
baud_rate = 9600  # Configuración de baudios de la báscula

def reiniciar_todo_intelisis():
    """
    Reinicia todos los procesos relacionados con Intelisis.
    """
    try:
        print("Buscando y cerrando procesos relacionados con Intelisis...")

        # Comando para cerrar todos los procesos que contengan "Intelisis" en el nombre
        os.system("taskkill /F /IM *Intelisis*")  # Mata cualquier proceso relacionado con Intelisis
        print("Procesos de Intelisis finalizados.")

        # Esperar un momento antes de reiniciar
        time.sleep(2)

        # Reiniciar Intelisis Tools o cualquier otro programa necesario
        print("Reiniciando Intelisis Tools...")
        os.system("IntelisisPOSToolV2.exe")  # Cambia el nombre o la ruta según sea necesario
        os.system("IntelisisPos.exe")
        # Puedes añadir otros programas relacionados aquí si es necesario
        # os.system("start OtroProgramaRelacionado.exe")

        print("Procesos de Intelisis reiniciados correctamente.")
    except Exception as e:
        print(f"Error al reiniciar Intelisis: {e}")
def ejecutar_comando_sql():
    """
    Ejecuta un comando SQL para eliminar los datos de la tabla IntelisisET.
    """
    try:
        print("Ejecutando comando SQL para eliminar datos de IntelisisET...")
        # Comando SQL usando sqlcmd
        comando = 'sqlcmd -S CAJA02 -U sa -P intelisis1 -Q "DELETE IntelisisET;"'
        resultado = os.system(comando)
        
        # Verificar el resultado del comando
        if resultado == 0:
            print("Datos eliminados correctamente de IntelisisET.")
        else:
            print("Error al ejecutar el comando SQL. Verifica la conexión y los parámetros.")
    except Exception as e:
        print(f"Error al ejecutar el comando SQL: {e}")
def leer_peso_en_tiempo_real():
    """
    Lee el peso desde la báscula en tiempo real y lo muestra en la consola.
    """
    try:
        bascula = serial.Serial(puerto, baud_rate, timeout=1)
        print(f"Conectado a la báscula en {puerto} a {baud_rate} baudios")
        print("Leyendo peso en tiempo real... Presiona Ctrl+C para detener.")

        while True:
            datos = bascula.readline().decode('utf-8').strip()
            if datos:  # Si hay datos recibidos
                # Mostrar el peso en tiempo real en la consola
                print(f"\rPeso: {datos} kg", end='', flush=True)  # Sobrescribe la línea en la consola
    except serial.SerialException as e:
        print(f"\nError de conexión: {e}")
    except KeyboardInterrupt:
        print("\nPrograma detenido manualmente.")
    finally:
        if 'bascula' in locals() and bascula.is_open:
            bascula.close()
        print("Conexión cerrada.")

# Ejecución del programa
if __name__ == "__main__":
    print("Iniciando programa...")
    reiniciar_todo_intelisis()  # Reinicia todos los procesos de Intelisis
    ejecutar_comando_sql()  # Ejecuta el comando SQL para limpiar la tabla IntelisisET
    leer_peso_en_tiempo_real()  # Inicia la lectura de la báscula en tiempo real