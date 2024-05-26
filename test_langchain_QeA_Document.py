
#pip install docarray
#pip install ipython

import datetime
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display, Markdown
from langchain.indexes import VectorstoreIndexCreator

# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"

llm = ChatOpenAI(openai_api_key = "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", temperature=0.0, model=llm_model)

file = 'inventory_v2.csv'
loader = CSVLoader(file_path=file)

index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

""" #query ="Please list all your shirts with sun protection in a table in markdown and summarize each one."

query ="Please list all products with product.partNumber equal PS-PL-R186."

response = index.query(query)

display(Markdown(response)) """