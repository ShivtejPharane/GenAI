from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3:8b")
while True:
    user_input = input("> ")
    if user_input == 'Bye':
        break
    response = model.invoke(user_input)

    print(response.content)