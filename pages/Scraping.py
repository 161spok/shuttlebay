import os
import openai
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.agents.agent_toolkits import FileManagementToolkit
from tempfile import TemporaryDirectory
from langchain.callbacks import get_openai_callback
import streamlit as st


st.title("Esempio 1")

st.write("You have entered", st.session_state["my_input"])



openai_api_key = ''

serpapi_api_key = ''

#working_directory = TemporaryDirectory(dir=os.getcwd())

# -------------------- genera una cartella 'data' in .venv\scripts
toolkit = FileManagementToolkit (
root_dir=str('data'),
selected_tools=["write_file"],
).get_tools()

llm = OpenAI (temperature=0, openai_api_key=openai_api_key)
toolkit.extend(load_tools(["serpapi"], llm=llm, serpapi_api_key=serpapi_api_key))
               
agent = initialize_agent(
toolkit,
llm,
verbose=True,
return_intermediate_steps=True,
agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
)

#response = agent ({
#"input": "cerca sul sito https://www.ondacinema.it/ la prima recensione per il " +
#"film 'Oppenheimer' , estrai il sentiment e salvalo su un file di testo"
#})

#print(response)

with get_openai_callback() as cb:
    response = agent({
"input": "cerca sul sito https://www.ondacinema.it/ la prima recensione per il " +
"film 'Oppenheimer' , estrai il sentiment e salvalo su un file di testo"
})
    st.write(response)
    st.write("=======================================================================")
    st.write(f"Total Tokens: {cb.total_tokens}")
    st.write(f"Prompt Tokens: {cb.prompt_tokens}")
    st.write(f"Completion Tokens: {cb.completion_tokens}")
    st.write(f"Total Cost (USD): ${cb.total_cost}")
