from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Create the instance of OpenAI (client) to communicate with required model
client = OpenAI()
# send the prompt along with the model name to the client
response = client.responses.create(
    model = "gpt-5-nano",
    input="what is color of sky?"
    )

# print the respone
print(response)