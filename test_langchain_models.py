import os
import openai
from langchain.chat_models import ChatOpenAI

# account for deprecation of LLM model
import datetime
import streamlit as st

openai.api_key = ""

# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"

# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
chat = ChatOpenAI(openai_api_key = "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",temperature=0.0, model=llm_model)

st.write("Chat ----> ",chat)

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

style = """American English \
in a calm and respectful tone
"""
customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""

from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(template_string)

 
prompt_template.messages[0].prompt
 
prompt_template.messages[0].prompt.input_variables
 
customer_style = """American English \
in a calm and respectful tone
"""
 
customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""
 
customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)
 
st.write("customer_messages ---> ", type(customer_messages))
st.write("customer_messages[0] ---> ",type(customer_messages[0]))
 
st.write("customer_messages[0] --->", customer_messages[0])
 
# Call the LLM to translate to the style of the customer message
customer_response = chat(customer_messages)
 
st.write("customer_response.content ---> ", customer_response.content)
 
service_reply = """Hey there customer, \
the warranty does not cover \
cleaning expenses for your kitchen \
because it's your fault that \
you misused your blender \
by forgetting to put the lid on before \
starting the blender. \
Tough luck! See ya!
"""
 
service_style_pirate = """\
a polite tone \
that speaks in English Pirate\
"""
 
service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply)

st.write("service_messages[0].content ---> ", service_messages[0].content)
 
service_response = chat(service_messages)
st.write("service_response.content ---> ", service_response.content)

{
  "gift": False,
  "delivery_days": 5,
  "price_value": "pretty affordable!"
}

customer_review = """\
This leaf blower is pretty amazing.  It has four settings:\
candle blower, gentle breeze, windy city, and tornado. \
It arrived in two days, just in time for my wife's \
anniversary present. \
I think my wife liked it so much she was speechless. \
So far I've been the only one using it, and I've been \
using it every other morning to clear the leaves on our lawn. \
It's slightly more expensive than the other leaf blowers \
out there, but I think it's worth it for the extra features.
"""

review_template = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? \
Answer True if yes, False if not or unknown.

delivery_days: How many days did it take for the product \
to arrive? If this information is not found, output -1.

price_value: Extract any sentences about the value or price,\
and output them as a comma separated Python list.

Format the output as JSON with the following keys:
gift
delivery_days
price_value

text: {text}
"""

from langchain.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(review_template)
st.write("prompt_template ---> ", prompt_template)

messages = prompt_template.format_messages(text=customer_review)

chat = ChatOpenAI(openai_api_key = "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",temperature=0.0, model=llm_model)

response = chat(messages)
st.write("response.content ---> ", response.content)

type(response.content)

# You will get an error by running this line of code 
# because'gift' is not a dictionary
# 'gift' is a string

#response.content.get('gift')

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser


gift_schema = ResponseSchema(name="gift",
                             description="Was the item purchased\
                             as a gift for someone else? \
                             Answer True if yes,\
                             False if not or unknown.")
delivery_days_schema = ResponseSchema(name="delivery_days",
                                      description="How many days\
                                      did it take for the product\
                                      to arrive? If this \
                                      information is not found,\
                                      output -1.")
price_value_schema = ResponseSchema(name="price_value",
                                    description="Extract any\
                                    sentences about the value or \
                                    price, and output them as a \
                                    comma separated Python list.")

response_schemas = [gift_schema, 
                    delivery_days_schema,
                    price_value_schema]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()

st.write("format_instructions ---> ", format_instructions)

review_template_2 = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? \
Answer True if yes, False if not or unknown.

delivery_days: How many days did it take for the product\
to arrive? If this information is not found, output -1.

price_value: Extract any sentences about the value or price,\
and output them as a comma separated Python list.

text: {text}

{format_instructions}
"""

prompt = ChatPromptTemplate.from_template(template=review_template_2)

messages = prompt.format_messages(text=customer_review, 
                                format_instructions=format_instructions)

st.write("messages[0].content ---> ", messages[0].content)

response = chat(messages)

st.write(response.content)

output_dict = output_parser.parse(response.content)

st.write(output_dict)

type(output_dict)

output_dict.get('delivery_days')
