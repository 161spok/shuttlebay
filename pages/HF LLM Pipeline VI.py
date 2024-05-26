from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate
import streamlit as st
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

load_dotenv()

st.title("🔎 LangChain e HF - Prompt template")
st.write("Non richiede OpenAI key")

# first example
# hub_llm = HuggingFaceHub(repo_id="mrm8488/t5-base-finetuned-wikiSQL")

# prompt = PromptTemplate(
#     input_variables=["question"],
#     template="Translate English to SQL: {question}"    
# )

# hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)
# print(hub_chain.run("What is the average age of the respondents using a mobile device?"))


# second example below:
hub_llm = HuggingFaceHub(
    repo_id='gpt2',
    model_kwargs={'temperature': 0.7, 'max_length': 100}
)

prompt = PromptTemplate(
    input_variables=["profession"],
    template="You had one job 😡! You're the {profession} and you didn't have to be sarcastic"
)

hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)


st.write(hub_chain.run("customer service agent"))

st.write(hub_chain.run("politician"))

st.write(hub_chain.run("Fintech CEO"))

st.write(hub_chain.run("insurance agent"))

#print(hub_chain.run("customer service agent"))
#print(hub_chain.run("politician"))
#print(hub_chain.run("Fintech CEO"))
#print(hub_chain.run("insurance agent"))
