
#---------------->       pip install python-dotenv


# questo esempio provvede al caricamento in locale dell'llm
# non lo esegue subito

import os
import requests, json
from dotenv import load_dotenv, find_dotenv #pip install python-dotenv
import streamlit as st

load_dotenv(find_dotenv()) # read local .env file

#hf_api_key = os.environ['HF_API_KEY']
hf_api_key = ""

st.title("💬 LLM endpoint") 
st.write("SUMMARIZATION pipeline")
st.write("Endpoint: https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6")

#Summarization endpoint
def get_completion(inputs, parameters=None,ENDPOINT_URL="https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"):
    headers = {
      "Authorization": f"Bearer {hf_api_key}",
      "Content-Type": "application/json"
    }
    data = { "inputs": inputs }
    if parameters is not None:
        data.update({"parameters": parameters})
    response = requests.request("POST",
                                ENDPOINT_URL, headers=headers,
                                data=json.dumps(data)
                               )
    return json.loads(response.content.decode("utf-8"))

text = ('''The tower is 324 metres (1,063 ft) tall, about the same height
        as an 81-storey building, and the tallest structure in Paris. 
        Its base is square, measuring 125 metres (410 ft) on each side. 
        During its construction, the Eiffel Tower surpassed the Washington 
        Monument to become the tallest man-made structure in the world,
        a title it held for 41 years until the Chrysler Building
        in New York City was finished in 1930. It was the first structure 
        to reach a height of 300 metres. Due to the addition of a broadcasting 
        aerial at the top of the tower in 1957, it is now taller than the 
        Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the 
        Eiffel Tower is the second tallest free-standing structure in France 
        after the Millau Viaduct.''')

result = get_completion(text)
st.write(result)
