import os
from llama_index.llms.ollama import Ollama
from dotenv import dotenv_values

config = {"COLLECTION_NAME" : "aiops24",
    "VECTOR_SIZE" : 512,
    "OLLAMA_URL" : "http://localhost:11434"}

llm = Ollama(
    model="qwen", base_url=config["OLLAMA_URL"], temperature=0, request_timeout=120
)

def rewrite(query):
    prompt = f"""
    整理下面文本的格式，返回给我整理好的版本:
    ---------
    {query}
    ---------
    """
    response = llm.complete(prompt)
    return response.text

for to_path in os.listdir("data"):
    path = "data/" + to_path + "/"
    for file in os.listdir(path):
        if file[-3:] == "txt":
            with open(path + file, "a+", encoding='utf-8') as f:
                data = f.readline()
                f.write(rewrite(data))
                f.close()