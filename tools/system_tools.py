from datetime import datetime, date

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
