import os
from openai import OpenAI
import google.generativeai as genai

def respondeOpenai(frase_usuario: str, prompt: str, autores: set):
    client_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client_openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    respuesta_llm = response.choices[0].message.content.strip()

    print(f"Frase del usuario: {frase_usuario}\n")
    print(f"Autor(es) involucrados: {', '.join(autores)}\n")
    print("Respuesta del monje:\n")
    print(respuesta_llm)


def respondeGemini(frase_usuario: str, prompt: str, autores: set):
    genai.configure(api_key=os.getenv("GEMINI"))

    generation_config = {"temperature": 0.7}

    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        response = model.generate_content(prompt, generation_config=generation_config)
        respuesta_llm = response.text.strip()
    except Exception as e:
        respuesta_llm = f"Error generando respuesta con Gemini: {e}"

    print(f"Frase del usuario: {frase_usuario}\n")
    print(f"Autor(es) involucrados: {', '.join(autores)}\n")
    print("Respuesta del monje:\n")
    print(respuesta_llm)

