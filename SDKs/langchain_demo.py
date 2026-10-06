# Import openai class from the langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# create an instance of openai
client = ChatOpenAI(model="gpt-5-nano")

# Send the prompt and response
response = client.invoke('what is color of sky')

# print the response
print(response)