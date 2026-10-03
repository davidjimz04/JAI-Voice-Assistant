from datetime import datetime, date
import subprocess
import psutil

jarvis_active = True

def shutdown() -> str:
    """ CERRAR SESION DE JARVIS """
    global jarvis_active
    jarvis_active = False
    return "Jai se apagara" 

def get_hour() -> str: 
    """ Muestra la hora actual """

    hour = datetime.now()
    return hour.strftime("%H:%M")

def get_date() -> str: 
    """ Muestra la fecha actual """

    today = date.today()
    return today.strftime('%d/%m/%Y')

def open_app(name_app:str) -> str:
    try:
        subprocess.run(["open", "-a", name_app], check=True)
        return f"La app {name_app} se ha abierto"
    except subprocess.CalledProcessError:
        return "No se encontro es app."


# INFORMACION DEL EQUIPO

def info_battery() -> str:
    """
    Esta funcion informa sobre el porciento de la bateria del equipo del usuario 

    Especificaciones:
        - 80% - 100% (Bateria perfecta)
        - 50% - 79% (Bateria buena)
        - 0% - 49% (Bateria mala, es mejor enchufar el equipo)
    """
    battery = psutil.sensors_battery()
    porcentage = battery.percent

    return f"{porcentage}%"

def info_ram() -> str:
    """
    Esta funcion es para informar sobre la memoria ram de la maquina del usuario

    Especificaciones:
        - Especifica la ram total
        - Especifica la ram libre 
    """
    ram = psutil.virtual_memory()
    ram_total = ram.total / (1024 ** 3)
    ram_free = ram.available / (1024 ** 3)

    return f"RAM total: {ram_total:.1f} GB, RAM libre: {ram_free:.1f} GB" 

def info_disk() -> str:
    """
    Esta funcion informa sobre la el disco duro del equipo del usuario

    Especificaciones: 
        - Especifica el total del almacenamiento del disco 
        - Especifica el libre del almacenamiento del disco 
    """

    disk = psutil.disk_usage("/")
    disk_total = disk.total / (1024 ** 3)
    disk_used = disk.used / (1024 ** 3)
    disk_free = disk.free / (1024 ** 3)

    return f"Almacenamiento de disco total: {disk_total:.1f}GB, Almacenamiento de disco usado: {disk_used:.1f}GB, Almacenamiento de disco libre: {disk_free:.1f}GB"

def volume(level:int) -> str:
    try:
        level = max(0, min(100, level))
        script = f'set volume output volume {level}'
        subprocess.run(["osascript", "-e", script], check=True)
        return f"El volumen esta ahora al {level}%"
    except subprocess.CalledProcessError:
        return "No se pudo bajar el volumen."

# def mute_mac(mute: bool=True) -> str:
#     """
#     Silencia o activa el sonido del equipo.

#     Args:
#         mute: True para silenciar el equipo.
#               False para activar nuevamente el sonido.

#     Returns:
#         Mensaje indicando el resultado de la acción.
#     """

#     try:
#         state = "TRUE" if mute else "FALSE"
#         script = f"set volume output muted {state}"
#         subprocess.run(["osascript", "-e", script], check=True)
#         return "El equpo se ha silenciado" if mute else "Sonido activado en el equipo"
#     except subprocess.CalledProcessError:
#         return "No se pudo silenciar el equipo."
