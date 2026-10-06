# Communicate with ollama model using the REST API

import requests
import json
base_url = "http://localhost:11434/api/generate" 

# Create body
data =  {
    "model" : "llama3:8b",
    "messages" : [{"role" : "user","content":"what is the color of the sky"}]
}

response = requests.post(base_url, #url to send the requests
                         data=json.dump(data), # send the body in json format
                         headers={"Content-type":"application/json" # send the content type
                        })

# process the response 
print(response.text)