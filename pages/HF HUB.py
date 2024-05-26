import os
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

# Esempi tratti da quì https://python.langchain.com/docs/integrations/llms/huggingface_hub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

st.subheader('In questo esempio si utilizza Langchain con HUB HuggingFace', divider='rainbow')

st.markdown(
    """
    In questo esempio si utilizza Langchain con HUB HuggingFace
    **L'HUB consente di utilizzare il modello remoto**
    """)
st.subheader('**Utilizziamo la API key HuggingFace** is :blue[cool] :sunglasses:')

question = "Who won the FIFA World Cup in the year 1994? "

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

repo_id = st.selectbox(
    '**Seleziona  LLM**',
    ('google/flan-t5-xxl', 'databricks/dolly-v2-3b', 'Writer/camel-5b-hf', 'Salesforce/xgen-7b-8k-base', 'tiiuae/falcon-40b'))

st.write('Hai selezionato : ', repo_id)

#repo_id = "google/flan-t5-xxl"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

def show_res(repo_id):
    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    st.write(llm_chain.run(question))

show_res(repo_id)


