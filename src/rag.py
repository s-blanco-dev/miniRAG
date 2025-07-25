import json
import chromadb
import os

CITAS_PATH = "./data/citas.json"

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="sanctus")

# cargo frases de santos
if len(collection.get()["ids"]) == 0:
    with open(CITAS_PATH, "r", encoding="utf-8") as f:
        citas = json.load(f)

    for cita in citas:
        collection.add(
            documents=[cita["texto"]],
            ids=[cita["id"]],
            metadatas=[{"autor": cita["autor"]}]
        )

    print(f"Se cargaron {len(citas)} citas en ChromaDB.")


def construir_prompt(frase_usuario: str):
    resultados = collection.query(
        query_texts=[frase_usuario],
        n_results=4,
        include=["documents", "metadatas"]
    )

    citas_contexto = ""
    autores = set()

    for doc, meta in zip(resultados["documents"][0], resultados["metadatas"][0]):
        citas_contexto += f"- \"{doc}\" ({meta['autor']})\n"
        autores.add(meta["autor"])

    prompt = f"""
Eres un monje benedictino sabio antiguo. Una persona te dice: "{frase_usuario}".
Respondele con sabiduría utilizando las siguientes citas como inspiración y fundamento: 

{citas_contexto}

Responde de manera reflexiva y profunda, pero breve. Puedes mencionar a los autores si lo consideras relevante.


Agrega abajo una frase relacionada original creada por ti, de la manera:
    Por mi parte, yo siempre digo: [FRASE ORIGINAL]
"""
    return prompt.strip(), autores
