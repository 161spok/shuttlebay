import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import PALChain

from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.chains import SimpleSequentialChain, SequentialChain
from langchain.memory import SimpleMemory
import streamlit as st

os.environ['OPENAI_API_KEY'] = ""
os.environ['SERPAPI_API_KEY'] = ""

llm = OpenAI(temperature=0)
tools = load_tools(["pal-math", "serpapi"], llm=llm)
agent = initialize_agent(tools,
                         llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)

# Simple Sequential Chains
chain_one = agent

template = """You are a gift recommender. Given a person's age,\n
 it is your job to suggest an appropriate gift for them.

Person Age:
{age}
Suggest gift:"""

prompt_template = PromptTemplate(input_variables=["age"], template=template)
chain_two = LLMChain(llm=llm, prompt=prompt_template)

overall_chain = SimpleSequentialChain(
                  chains=[chain_one, chain_two],
                  verbose=True)

question = "If my age is half of my dad's age and he is going to be 60 next year, what is my current age?"
st.write(overall_chain.run(question))

#Sequential Chains
template = """You are a gift recommender. Given a person's age,\n
 it is your job to suggest an appropriate gift for them. If age is under 10,\n
 the gift should cost no more than {budget} otherwise it should cost atleast 10 times {budget}.

Person Age:
{output}
Suggest gift:"""
prompt_template = PromptTemplate(input_variables=["output", "budget"], template=template)
chain_two = LLMChain(llm=llm, prompt=prompt_template)

overall_chain = SequentialChain(
                input_variables=["input"],
                memory=SimpleMemory(memories={"budget": "100 GBP"}),
                chains=[agent, chain_two],
                verbose=True)

st.write(overall_chain.run("If my age is half of my dad's age and he is going to be 60 next year, what is my current age?"))

st.write(agent.agent.llm_chain.prompt.template)

st.write(agent.agent.llm_chain.prompt.input_variables)