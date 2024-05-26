from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain import OpenAI

llm = OpenAI(model_name='text-davinci-003', 
             temperature=0, 
             max_tokens = 256)

# create a long string
schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"}, 
                    {"output": f"{schedule}"})

memory.load_memory_variables({})

conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=True
)

conversation.predict(input="What would be a good demo to show?")

memory.load_memory_variables({})

