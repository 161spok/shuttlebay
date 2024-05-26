from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import openai
from langchain.callbacks import get_openai_callback

# Step 1: Import the necessary modules
import os
 
# Step 2: Set the OpenAI API key
openai.api_key = ""
 
# Step 3: Get user input
user_input = input("Enter a concept: ")
 
# Step 4: Define the Prompt Template
prompt = PromptTemplate(
    input_variables=["concept"],
    template="Definisci {concept} con un esempio del mondo reale ",
)
 
# Step 5: Print the Prompt Template
print(prompt.format(concept=user_input))
 
# Step 6: Instantiate the LLMChain
llm = OpenAI(openai_api_key = "", temperature=0.9)
#chain = LLMChain(llm=llm, prompt=prompt)
 
# Step 7: Run the LLMChain
with get_openai_callback() as cb:
    #result = llm("Tell me a joke")
    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run(user_input)
    print(cb)

#output = chain.run(user_input)

print(output)
