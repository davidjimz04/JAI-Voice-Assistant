import json

def load_memory() -> dict:
    with open("data/memory.json", "r") as file:
        memory = json.load(file)
    return memory


def save_memory(key: str, value: str) -> str:
    """
    Guarda información importante del usuario en la memoria persistente.

    key: nombre corto y descriptivo que identifica el dato.
    value: información que se desea recordar.
    """

    memory = load_memory()

    memory[key] = value

    with open("data/memory.json", "w") as file:
        json.dump(memory, file)

    return "Diccionario actualizado!"


def get_memory():
    memory = load_memory()
    return memory

