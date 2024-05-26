
#pip install huggingface_hub>=0.14.1
#pip install trasformers
#pip install ipython


# in caso di errore eseguire questo: 
# pip install huggingface_hub>=0.14.1 git+https://github.com/huggingface/transformers@v4.29.0 diffusers accelerate datasets torch soundfile sentencepiece opencv-python openai



import IPython
import soundfile as sf
import getpass
import streamlit as st
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

st.subheader('In questo esempio si utilizza  HuggingFace Trasformers', divider='rainbow')

st.markdown(
    """
    In questo esempio si utilizza HuggingFace
    **Trasformers**
    """)
st.subheader('**Utilizziamo la API key HuggingFace** is :blue[cool] :sunglasses:')

def play_audio(audio):
    sf.write("speech_converted.wav", audio.numpy(), samplerate=16000)
    return IPython.display.Audio("speech_converted.wav")



#agent_name = "OpenAI (API Key)" #@param ["StarCoder (HF Token)", "OpenAssistant (HF Token)", "OpenAI (API Key)"]
agent_name = "OpenAssistant (HF Token)"


if agent_name == "StarCoder (HF Token)":
    from transformers.tools import HfAgent
    agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")
    print("StarCoder is initialized 💪")
elif agent_name == "OpenAssistant (HF Token)":
    from transformers.tools import HfAgent
    agent = HfAgent(url_endpoint="https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
    print("OpenAssistant is initialized 💪")
if agent_name == "OpenAI (API Key)":
    from transformers.tools import OpenAiAgent
    pswd = getpass.getpass('OpenAI API key:')
    agent = OpenAiAgent(model="text-davinci-003", api_key=pswd)
    print("OpenAI is initialized 💪")

boat = agent.run("Generate an image of a boat in the water")
st.image(boat)

caption = agent.run("Can you caption the `boat_image`?", boat_image=boat)
st.image(boat, caption)

audio = agent.run("Can you generate an image of a boat? Please read out loud the contents of the image afterwards")
#st.audio(play_audio(audio))

agent.chat("Show me an an image of a capybara")

agent.chat("Transform the image so that it snows")

agent.chat("Show me a mask of the snowy capybaras")

agent.prepare_for_new_chat()

