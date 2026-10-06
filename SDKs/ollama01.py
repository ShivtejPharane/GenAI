from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2:8b",temperature=0)

response = model.invoke('What is color of sky')

print(response.content)