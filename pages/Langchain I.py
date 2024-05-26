from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

# creating a Prompt Template
template = """The following is a conversation between a human and an AI 
Assistant. Whatever the human asks to explain, the AI assistant
explains it with humour and by taking banana as an example

Human: {query}

AI: """

# assigning the template to the PromptTemplate Class
prompt = PromptTemplate(
    input_variables=["query"],
    template=template
)

# query
query = "Explain Machine Learning?"

# creating an llm chain
llm = OpenAI(model_name="text-davinci-003",temperature=1)
llm_chain = LLMChain(prompt=prompt, llm=llm)

# model output
print(llm_chain.run(query))