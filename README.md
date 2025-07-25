# 🧘 Proyecto RAG Monástico

Un RAG donde un modelo LLM responde como si fuera un sabio monje benedictino, utilizando citas de santos almacenadas en una base de datos vectorial (ChromaDB). Cuenta con 116 frases de santos almacenados en el archivo `data/citas.json`

## 📦 Requisitos

- Python 3.10 o superior
- `pip`
- Tenés que crear un `.env` en la carpeta src/ con las siguientes variables:
```
OPENAI_API_KEY=tu_api_key
GEMINI=tu_api_key
````

## 🔧 Instalación

```bash
git clone https://github.com/s-blanco-dev/miniRAG.git
cd miniRAG
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
````

## 🚀 Ejecución

El proyecto incluye una demo en `main.py` que permite probar el sistema con una frase de entrada por el usuario, pero antes hay que cargar las frases ejecutando `rag.py `:

```bash
python src/rag.py
python src/main.py
```

Para elegir el modelo de LLM a utilizar, es preciso descomentar una de las dos funciones (por defecto usa Gemini):

```python
# Elegí un modelo
# respondeOpenai(frase_usuario, prompt, autores)
respondeGemini(frase_usuario, prompt, autores)
```

## 📚 El funcionamiento en cuestión

1. La frase del usuario se consulta en una base de datos vectorial ChromaDB.
2. Se recuperan las 4 citas más relevantes.
3. Se construye un prompt con esas citas.
4. Un LLM responde como si fuera un monje sabio, con tono reflexivo, citando a los autores correspondientes.
5. El LLM inventa una frase acorde: "Por mi parte yo siempre digo: {frase original}"

## 🧠 Modelos soportados

* ✅ GPT-3.5 / GPT-4 (OpenAI)
* ✅ Gemini 1.5 Flash (Google), es el modelo por defecto de este proyecto dado que se me hizo más fácil utilizar su API.
* **Nota**: También estuve investigando sobre el uso de modelos locales con [Ollama](https://ollama.com/), que permite ejecutar LLMs como LLaMA, Mistral o Gemma directamente en tu máquina sin depender de APIs externas. Por razones de fuerza menor decidí no incluirlo en el proyecto.


## Demostración
![demo](https://github.com/user-attachments/assets/cac2df34-87f2-420c-8d12-771ddf662aa1)
