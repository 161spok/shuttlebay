# in caso di errore eseguire questo: 
# pip install huggingface_hub>=0.14.1 git+https://github.com/huggingface/transformers@v4.29.0 diffusers accelerate datasets torch soundfile sentencepiece opencv-python openai


from transformers import Tool

from huggingface_hub import list_models

from transformers.tools import HfAgent

from PIL import Image 

import requests 

import streamlit as st

from huggingface_hub import login

#Do this before HfAgent() and it should work
login("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")

class CatImageFetcher(Tool):
    name = "cat_fetcher"
    description = ("This is a tool that fetches an actual image of a cat online. It takes no input, and returns the image of a cat.")

    inputs = []
    outputs = ["text"]

    def __call__(self):
        return Image.open(requests.get('https://cataas.com/cat', stream=True).raw).resize((256, 256))

tool = CatImageFetcher()
tool()

agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder", additional_tools=[tool])

# OpenAssistant
#agent = HfAgent(url_endpoint= "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5" )

st.write(agent.run("Fetch an image of a cat online and caption it for me"))