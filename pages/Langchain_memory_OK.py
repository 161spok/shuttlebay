
import warnings
warnings.filterwarnings('ignore')

# account for deprecation of LLM model
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

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(openai_api_key = "",temperature=0.0, model=llm_model)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)

conversation.predict(input="Hi, my name is Andrew")

conversation.predict(input="What is 1+1?")

conversation.predict(input="What is my name?")

print("Memory buffer 1 ---> ",memory.buffer)

memory.load_memory_variables({})

memory = ConversationBufferMemory()

memory.save_context({"input": "Hi"}, 
                    {"output": "What's up"})

print("Memory buffer 2 ---> ", memory.buffer)

memory.load_memory_variables({})

memory.save_context({"input": "Not much, just hanging"}, 
                    {"output": "Cool"})

memory.load_memory_variables({})

