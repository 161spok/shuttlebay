from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import datetime
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
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)
memory = ConversationBufferWindowMemory(k=1)      

memory.save_context({"input": "Hi"},
                    {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})


memory.load_memory_variables({})

llm = ChatOpenAI(openai_api_key = "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", temperature=0.0, model=llm_model)
memory = ConversationBufferWindowMemory(k=1)
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=False
)

conversation.predict(input="Hi, my name is Andrew")

conversation.predict(input="What is 1+1?")

conversation.predict(input="What is my name?")

