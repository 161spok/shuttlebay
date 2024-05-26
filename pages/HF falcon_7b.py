# ==================================================================
#
# questo codice consente di utilizzare Falcon 7b dall'HuggingFaceHub


import os

from langchain import HuggingFaceHub, PromptTemplate, LLMChain

os.environ['API_KEY'] = ''

#model_id = 'tiiuae/falcon-7b-instruct' # con questo funziona
#model_id = 'h2oai/h2ogpt-oasst1-falcon-40b'
#model_id = 'TheBloke/WizardLM-Uncensored-Falcon-40B-GGML'
model_id = 'TheBloke/falcon-40b-instruct-GPTQ'


falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
                            repo_id=model_id,
                            model_kwargs={"temperature":0.1,"max_new_tokens":2000})

template = """

Sei un assistente IA che fornisce utili risposte alle domande di un utente e che risponde in lingua italiana. Se non conosci la risposta, dì solamente che non sai, non provare a generare una risposta. 

{question}

"""

#You are an AI assistant that provides helpful answers to user queries.

prompt = PromptTemplate(template=template, input_variables=['question'])

falcon_chain = LLMChain(llm=falcon_llm,
                        prompt=prompt,
                        verbose=True)

#print(falcon_chain.run("What are the colors in the Rainbow?"))
print(falcon_chain.run("Quanti tipi di saldatura per alluminio esistono?"))
