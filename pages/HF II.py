# importing Hugging Face Wrapper from LangChain
from langchain import HuggingFaceHub
import os
import streamlit as st
import time

st.title("Esempio 2 con chiave HF solo - LLM google/flan-t5-xxl")

st.write("[Gestione sessione] You have entered : ", st.session_state["my_input"])


# provide your API KEY here
os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''

# initialize Hugging Face LLM
flan_t5_model = HuggingFaceHub(
    repo_id="google/flan-t5-xxl",
    model_kwargs={"temperature":1e-1}
)

query1 = "Who was the first person to go to Space?"
query2 = "What is 2 + 2 equals to?"

generate = flan_t5_model.generate([query1, query2])

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)

st.write(generate.generations)
    
