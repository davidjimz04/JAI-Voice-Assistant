from datetime import datetime, date
import requests
import webbrowser

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

url = "https://geocoding-api.open-meteo.com/v1/search"
weather_url = "https://api.open-meteo.com/v1/forecast"

def get_weather(city:str="huehuetoca, estado de mexico") -> str:
    try: 
        params = {
            "name": city,
            "count": 1,
            "language": "es",
            "format": "json",
        }

        response = requests.get(url, params=params, timeout=10)
        dates = response.json()

        latitude = dates['results'][0]['latitude']
        longitude = dates['results'][0]['longitude']

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m",
        }

        weather_response = requests.get(weather_url, params=weather_params, timeout=10)
        weather_dates = weather_response.json()

        temperature = weather_dates['current']['temperature_2m']
        unit = weather_dates['current_units']['temperature_2m']

        return f"{city}: {temperature}{unit}"
    except (KeyError, IndexError):
        return "No se encontró la ciudad solicitada."
    except requests.exceptions.ConnectionError:
        return "Hubo un error de conexion."
    except requests.exceptions.Timeout:
        return "El servicio del clima tardó demasiado en responder."
    except requests.exceptions.RequestException:
        return "Ocurrió un error al consultar el servicio del clima."


def open_youtube() -> str:
    """ Abre YOUTUBE en el navegador """

    webbrowser.open_new_tab("https://www.youtube.com/")
    return "Youtube se ha abierto en una nueva ventana en su navegador"

def open_chatgpt() -> str:
    """ Abre CHATGPT en el navegador """ 

    webbrowser.open_new_tab("https://www.chatgpt.com/")
    return "ChatGPT se ha abierto en una nueva ventana en su navegador"

def open_claude() -> str:
    """ Abre CLAUDE en el navegador """

    webbrowser.open_new_tab("https://www.claude.com/")
    return "Claude se ha abierto en una nueva ventana en su navegador"

JAI_TOOLS = [
    shutdown,
    get_hour,
    get_date,
    get_weather,
    open_youtube,
    open_chatgpt,
    open_claude,
]