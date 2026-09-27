from tools import web_tools, system_tools, weather_tools

JAI_TOOLS = [
    web_tools.open_claude,
    web_tools.open_chatgpt,
    web_tools.open_youtube,
    system_tools.get_date,
    system_tools.get_hour,
    system_tools.shutdown,
    weather_tools.get_weather,
]