from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

# vengono create due catene che vengono poi unite insieme

# creating the first template
first_template = """Given the IPL Team Name, tell the Year in which they first
won the trophy.

% IPL TEAM NAME
{team_name}

YOUR RESPONSE:
"""
team_template = PromptTemplate(input_variables=["team_name"], template=first_template)

llm = OpenAI(model_name="text-davinci-003",temperature=1)

# creating the team_chain that holds the year informatino
team_chain = LLMChain(llm=llm, prompt=team_template)

# creating the second Template
second_template = """Given the Year, name the Highest Scoring Batsman in the IPL for that Year.
% YEAR
{year}

YOUR RESPONSE:
"""
batsman_template = PromptTemplate(input_variables=["year"], template=second_template)

# creating the batsman_chain that holds the bastman information
batsman_chain = LLMChain(llm=llm, prompt=batsman_template)

# combining two LLMChains
final_chain = SimpleSequentialChain(chains=[team_chain, batsman_chain], verbose=True)

# checking the chain output
final_output = final_chain.run("Sunrisers Hyderabad")