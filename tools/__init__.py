from tools import web_tools, system_tools, weather_tools
from memory.memory import save_memory

JAI_TOOLS = [
    web_tools.open_claude,
    web_tools.open_chatgpt,
    web_tools.open_youtube,
    web_tools.open_hybridge,
    system_tools.get_date,
    system_tools.get_hour,
    system_tools.shutdown,
    weather_tools.get_weather,
    save_memory,
]