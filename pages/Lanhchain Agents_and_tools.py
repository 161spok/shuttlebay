from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent


import os
import streamlit as st


st.markdown(
    """
    In questo esempio si utilizza Langchain con Tools e Agents
    **Utilizziamo key OpenAI e SerpAPI**
    """)
st.write("Effettuiamo il caricamento")

os.environ['OPENAI_API_KEY'] = ""
os.environ['SERPAPI_API_KEY'] = ""

llm = OpenAI(temperature=0)
tool_names = ["serpapi"]
tools = load_tools(tool_names)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Input should be a search query.
st.write(agent.run("Chi è Giorgia Meloni ?"))
st.write(agent.agent.llm_chain.prompt.template)
st.divider()
st.write(agent.run("Chi è T'pring ?"))
st.write(agent.agent.llm_chain.prompt.template)
st.divider()

agent = create_csv_agent(
    OpenAI(temperature=0),
    "ing-mec.csv",
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

st.write(agent.run("The context is mechanical engineering. What is the advantage of evolving profiles ?"))
