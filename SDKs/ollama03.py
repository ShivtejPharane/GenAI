from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3:8b",
                   base_url="http://127.0.0.1:11434")

response = model.invoke("What is the color of the sky")

print(response.content)