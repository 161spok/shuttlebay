from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
#from Timer import Timer
import streamlit as st

st.title("Esempio 4 HF solo - Pipeline LLM lmsys/fastchat-t5-3b-v1.0")

st.markdown(
    """
    In questo esempio si utilizza Langchain con  HuggingFace pipeline
    **La pipeline scarica il modello in locale**
    
    """)

st.write("You have entered", st.session_state["my_input"])

model_id = "lmsys/fastchat-t5-3b-v1.0"
llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text2text-generation",
    model_kwargs={"temperature": 0, "max_length": 1000},
)

def ask_question(question):
    result = llm_chain(question)
    st.write(result['question'])
    st.write("")
    st.write(result['text'])


template = """
You are a friendly chatbot assistant that responds conversationally to users' questions.
Keep the answers short, unless specifically asked by the user to elaborate on something.

Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

#with Timer():
ask_question("Describe some famous landmarks in London")   