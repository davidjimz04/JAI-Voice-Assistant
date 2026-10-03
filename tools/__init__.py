from tools import web_tools, system_tools, weather_tools
from memory.memory import save_memory, get_memory

JAI_TOOLS = [
    web_tools.open_claude,
    web_tools.open_chatgpt,
    web_tools.open_youtube,
    web_tools.open_hybridge,
    web_tools.search_youtube,
    web_tools.search_google,
    system_tools.get_date,
    system_tools.get_hour,
    system_tools.shutdown,
    system_tools.open_app,
    system_tools.info_disk,
    system_tools.info_ram,
    system_tools.info_battery,
    system_tools.volume,
    weather_tools.get_weather,
    save_memory,
    get_memory
]