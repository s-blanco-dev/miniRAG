from rag import construir_prompt
from llm import respondeGemini, respondeOpenai 

frase_usuario = input("Insertá la frase nomás:\n> ")

prompt, autores = construir_prompt(frase_usuario)

# Elegí un modelo
# respondeOpenai(frase_usuario, prompt, autores)
respondeGemini(frase_usuario, prompt, autores)

