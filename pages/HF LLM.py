from langchain import PromptTemplate, HuggingFaceHub, LLMChain
import os
import streamlit as st
import time

st.title("Esempio 3 con chiave HF solo - LLM google/flan-t5-xxl")

st.write("You have entered : ", st.session_state["my_input"])


os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

template = """Question: {query}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["query"])

llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.1})

llm_chain = LLMChain(prompt=prompt, llm=llm)

query = "When was America discovered ?"

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)

st.write(llm_chain.run(query))