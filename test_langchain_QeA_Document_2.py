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

loader = CSVLoader(file_path=file)

docs = loader.load()

docs[0]

from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

embed = embeddings.embed_query("Hi my name is Harrison")

print(len(embed))

print(embed[:5])

db = DocArrayInMemorySearch.from_documents(
    docs, 
    embeddings
)

query = "Please suggest a shirt with sunblocking"


docs = db.similarity_search(query)


len(docs)

docs[0]

retriever = db.as_retriever()

llm = ChatOpenAI(temperature = 0.0, model=llm_model)

qdocs = "".join([docs[i].page_content for i in range(len(docs))])

response = llm.call_as_llm(f"{qdocs} Question: Please list all your \
shirts with sun protection in a table in markdown and summarize each one.") 

display(Markdown(response))

qa_stuff = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=retriever, 
    verbose=True
)

query =  "Please list all your shirts with sun protection in a table \
in markdown and summarize each one."

response = qa_stuff.run(query)

display(Markdown(response))



index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch,
    embedding=embeddings,
).from_loaders([loader])

response = index.query(query, llm=llm)







