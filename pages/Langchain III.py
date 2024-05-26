from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain import OpenAI, ConversationChain
import os
import streamlit as st
from langchain.memory import ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = ""
os.environ['SERPAPI_API_KEY'] = ""

st.subheader('In questo esempio si utilizza Langchain con OpenAI', divider='rainbow')

st.markdown(
    """
    Chains
    **Combine LLMs and prompts in multi-step workflows**
    """)
st.subheader('**Utilizziamo la API key OpenAI** is :blue[cool] :sunglasses:')

#============================================================================================================================
llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["food"],
    template="What are 5 vacation destinations for someone who likes to eat {food}?",
)

chain = LLMChain(llm=llm, prompt=prompt)
#st.write(chain.run("fruit"))

#==========================================================================================================================
st.markdown(
    """
    Agents
    **Dynamically call chains based on user input**
    """)


llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
#st.write(agent.run("Who is the current leader of Japan? What is the largest prime number that is smaller than their age?"))

#==========================================================================================================================
st.markdown(
    """
    Memory
    **Add state to chains and agents**
    """)

memory = ConversationBufferMemory()
llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True, memory=memory)

# quella che segue è una conversazione, questi sono gli input

#conversation.predict(input="Hi there!")
res = conversation.predict(input="Hi, my name is Elizabeth!")
print(res)
rel = conversation.predict(input="In mechanical engineering What is the advantage of evolving profiles ?")
print(rel)
memory.load_memory_variables({})
#conversation.predict(input="What would be a good time for a coffe break ?")

#conversation.predict(input="Tell me more")


#conversation.predict(input="I'm doing well! Just having a conversation with an AI.")

#conversation.predict(input="What was the first thing I said to you?")

#conversation.predict(input="In mechanical engineering What is the advantage of evolving profiles ?")

# esempio non completo













