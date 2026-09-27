import webbrowser

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
