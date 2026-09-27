# JAI - JM Assistant Intelligence 🤖

JAI (JM Assistant Intelligence) es un asistente personal de voz desarrollado en Python e integrado con Gemini.

Este proyecto nació como mi primer acercamiento al desarrollo de asistentes de inteligencia artificial, con el objetivo de aprender sobre modelos de lenguaje, APIs, reconocimiento de voz, síntesis de voz y Function Calling.

JAI puede mantener conversaciones por voz, interpretar instrucciones y utilizar herramientas de Python para realizar acciones reales.

## ✨ Funcionalidades

- 🎙️ Reconocimiento de voz en español.
- 🔊 Respuestas mediante síntesis de voz.
- 🧠 Conversaciones utilizando Gemini.
- 💬 Memoria durante la sesión de conversación.
- 🛠️ Function Calling para ejecutar herramientas.
- 🌤️ Consulta del clima actual mediante Open-Meteo.
- 🕐 Consulta de hora y fecha.
- 🌐 Apertura de sitios web como YouTube, ChatGPT y Claude.
- 📴 Apagado del asistente mediante comandos de voz.

## 🧠 ¿Cómo funciona?

El flujo principal de JAI es:

```text
Usuario habla
     ↓
SpeechRecognition
     ↓
Texto
     ↓
Gemini
     ↓
¿Necesita una herramienta?
     ↓
   Sí / No
     ↓
Python ejecuta la herramienta
     ↓
Gemini genera la respuesta
     ↓
pyttsx3
     ↓
JAI responde por voz
```

Gemini funciona como el cerebro del asistente, mientras que Python se encarga de ejecutar las acciones reales mediante herramientas.

## 🛠️ Tecnologías utilizadas

- Python
- Google Gemini API
- google-genai
- SpeechRecognition
- PyAudio
- pyttsx3
- Requests
- Open-Meteo API
- python-dotenv
- Unidecode

## 📁 Estructura del proyecto

```text
jarvis-project-prototype/
│
├── main.py
├── ia.py
├── tools.py
├── requirements.txt
├── .gitignore
└── README.md
```

### `main.py`

Controla el ciclo principal del asistente, el reconocimiento de voz y la síntesis de voz.

### `ia.py`

Configura Gemini, la personalidad de JAI, la conversación y las herramientas disponibles.

### `tools.py`

Contiene las funciones que JAI puede ejecutar, como consultar el clima, obtener la hora o abrir páginas web.

## 🚀 Instalación

Clona el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd jarvis-project-prototype
```

Crea un entorno virtual:

```bash
python3 -m venv .venv
```

Actívalo en macOS/Linux:

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🔑 Configuración

JAI necesita una API key de Gemini.

Crea un archivo `.env` en la raíz del proyecto:

```env
GEMINI_API_KEY=TU_API_KEY
```

El archivo `.env` está incluido en `.gitignore` para evitar publicar la API key accidentalmente.

## ▶️ Ejecutar JAI

Con el entorno virtual activado:

```bash
python3 main.py
```

JAI iniciará y comenzará a escuchar mediante el micrófono.

## 🧰 Herramientas actuales

Actualmente JAI dispone de herramientas para:

- Obtener la hora actual.
- Obtener la fecha actual.
- Consultar la temperatura actual de una ciudad.
- Abrir YouTube.
- Abrir ChatGPT.
- Abrir Claude.
- Finalizar su propia sesión.

## 🗺️ Próximos pasos

Algunas ideas para futuras versiones:

- Memoria persistente entre sesiones.
- Nuevas herramientas y automatizaciones.
- Mejorar la síntesis y naturalidad de la voz.
- Mejor manejo de errores.
- Organización modular de herramientas a medida que crezca el proyecto.

## 👨‍💻 Autor

Desarrollado por David como proyecto personal de aprendizaje de Ingeniería de Software e Inteligencia Artificial.

## 📌 Versión

JAI 1.0.0 - Primera versión funcional del asistente.