from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
#from Timer import Timer
import streamlit as st
from transformers import pipeline, Conversation
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

#expander = st.expander("See explanation")
#expander.write("The chart above shows some numbers I picked for you.")
#-------------------------------------------------------------------------------------

def predizione():
    #st.write("Genera un testo sulla base di una frase in input")
    #st.write("La frase è: Living a contented life is")
    #st.write("task=text-generation, model=GPT2")
    tab1.write("Genera un testo sulla base di una frase in input")
    tab1.write("La frase è: Living a contented life is")
    tab1.write("task=text-generation, model=GPT2")
    #prediction = pipeline(task="text-generation", model="GPT2")
    #pre_dizione = prediction("Living a contented life is")
    #st.write(pre_dizione)

# prediction(

#["Living a contented life is",

#"Success is not permanent. Failure is not fatal."]

#) 

#-------------------------------------------------------------------------------------
def classificatore():
    
    tab2.write("Classifica un testo sulla base di una frase in input")
    tab2.write("La frase è: I love eating mangoes")
    classifier = pipeline(task="text-classification", model="GPT2")
    class_ificatore = classifier("I love eating mangoes.")
    tab2.write(class_ificatore)
# classifier(

#["I love eating mangoes.",

#"I do not like papaya."]

#) 
#st.button("Classificatore", type="primary", on_click=classificatore)
#-------------------------------------------------------------------------------------
def riassunto():
    tab3.write("Riassume un testo sulla base di una frase in input")
    tab3.write("La frase è: Earth is warming up, and humans are at least partially to blame. The causes, effects, and complexities of global warming are important to understand so that we can fight for the health of our planet")
    tab3.write("Per ora genera un errore")
    #summary = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
    #rias_sunto = summary("Earth is warming up, and humans are at least partially to blame. The causes, effects, and complexities of global warming are important to understand so that we can fight for the health of our planet.", min_length=5, max_length=22)
    #tab3.write(rias_sunto)

#st.button("Riassunto", type="primary", on_click=riassunto)
#-------------------------------------------------------------------------------------
def classificatore2():
    tab4.write("Analisi del sentimento di un testo sulla base di più frasi in input")
    tab4.write("Le frasi sono: The movie is fantastic, I did not like the ice cream today, I am visiting Paris today")
    classifier = pipeline("sentiment-analysis", model = "finiteautomata/bertweet-base-sentiment-analysis")
    sentences = ["The movie is fantastic",
            "I did not like the ice cream today",
            "I am visiting Paris today"]
    output = classifier(sentences)
    tab4.write(output)

#st.button("Classificatore 2", type="primary", on_click=classificatore2)
#-------------------------------------------------------------------------------------
def generatore2():
    tab5.write("Generatore di testo sulla base di una frase in input")
    tab5.write("La frase è: If you look from the top of Eiffel Tower, you will see")
    generatore = pipeline(task="text-generation", model="GPT2")
    output = generatore("If you look from the top of Eiffel Tower, you will see")
    tab5.write(output)

#st.button("Generatore", type="primary", on_click=generatore2)
#-------------------------------------------------------------------------------------
def textdetector():
    text_detector = pipeline(task="fill-mask", model="GPT2")
    output = text_detector("Eiffel tower is located in <mask> the capital of France", top_k=2)
    for items in output:
        tab6.write(items)

#st.button("Text detector", type="primary", on_click=textdetector)        
#-------------------------------------------------------------------------------------
def translation():
    translator = pipeline(task="translation", model = "Helsinki-NLP/opus-mt-es-en")
    output = translator("Me encanta comer pasteles y frutas.")
    tab7.write(output)

#st.button("Translation", type="primary", on_click=translation)  
#-------------------------------------------------------------------------------------
def classificatore3():
    zs_classifier = pipeline(task="zero-shot-classification", model="GPT2")
    output = zs_classifier(
                        "England is the Cricket World Champion",
                        candidate_labels=["sports", "politics", "cinema"],
                    )
    tab8.write(output)

#st.button("Classificatore3", type="primary", on_click=classificatore3)
#-------------------------------------------------------------------------------------
def risponditore():
    answer_model = pipeline(task="question-answering", model="GPT2")
    output = answer_model(
        question="What is the name of the home ground of Manchester United",
        context="Manchester United plays their home matches at Old Trafford",
    )
    tab9.write(output)

#st.button("Risponditore", type="primary", on_click=risponditore)
#-------------------------------------------------------------------------------------
def conversational4():
    conversational_pipeline = pipeline(task="conversational", model="microsoft/DialoGPT-large")
    st.write(conversational_pipeline.model.config)
    #Sample inputs
    first_input = "Do you have any hobbies?"
    second_input = "I like to watch movies"
    third_input = "action movies"

    #Create a context
    bot_conversation = Conversation(first_input)

    tab10.write("\nFirst Exchange: \n--------------------")

    conversational_pipeline(bot_conversation)
    tab10.write(" User Input:", bot_conversation.past_user_inputs[0])
    tab10.write(" Bot Output:", bot_conversation.generated_responses[0])

    tab10.write("\nSecond Exchange: \n--------------------")
    bot_conversation.add_user_input(second_input)
    conversational_pipeline(bot_conversation)

    tab10.write(" User Input:", bot_conversation.past_user_inputs[1])
    tab10.write(" Bot Output:", bot_conversation.generated_responses[1])

    tab10.write("\nThird Exchange: \n--------------------")
    bot_conversation.add_user_input(third_input)
    conversational_pipeline(bot_conversation)

    tab10.write(" User Input:", bot_conversation.past_user_inputs[2])
    tab10.write(" Bot Output:", bot_conversation.generated_responses[1])

    tab10.write("\nAccessing All Responses: ")
    tab10.write(bot_conversation)

#-------------------------------------------------------------------------------------
st.title("Esempio 5 HF solo - Pipeline LLM ")

#st.write("You have entered", st.session_state["my_input"])

#-------------------------------------------------------------------------------------
st.subheader("Le tipologie di Task sono:")
st.write("Sentiment Classification, Token Classification, Text Generation, Text Completion, Text Translation")
st.write("Text Summarization, Zero Shot Classification, Question Answering, Conversational")

st.write("E' possibile scegliere il modello più adatto")
#st.divider()
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["📈 Predizione", "🗃 Classificatore", "Riassunto", "Classificatore", "Generatore", "Text detector", "Traduzione", "Classificatore 3", "Risponditore", "Conversazione"])
#tab1.subheader("A tab with a chart")
#my_expander = st.expander("Tipologie", expanded=True)

#with my_expander:
    #clicked = st.button("Expander button")
    #btn_pred = st.button("Predizione", type="primary", on_click=predizione)
    #btn_class = st.button("Classificatore", type="primary", on_click=classificatore)
    #btn_riass = st.button("Riassunto", type="primary", on_click=riassunto)
    #btn_class2 = st.button("Classificatore 2", type="primary", on_click=classificatore2)
    #btn_gen_2 = st.button("Generatore", type="primary", on_click=generatore2)
    #btn_text_det = st.button("Text detector", type="primary", on_click=textdetector)   
    #btn_transl = st.button("Translation", type="primary", on_click=translation)
    #btn_class3 = st.button("Classificatore3", type="primary", on_click=classificatore3)
    #btn_risp =st.button("Risponditore", type="primary", on_click=risponditore)
    #btn_conv = st.button("Conversational 4", type="primary", on_click=conversational4)

# AND in st.sidebar!

with st.sidebar:
    #clicked = st.button("Sidebar button")
    btn_pred = st.button("Predizione", type="primary", on_click=predizione)
    btn_class = st.button("Classificatore", type="primary", on_click=classificatore)
    btn_riass = st.button("Riassunto", type="primary", on_click=riassunto)
    btn_class2 = st.button("Classificatore 2", type="primary", on_click=classificatore2)
    btn_gen_2 = st.button("Generatore", type="primary", on_click=generatore2)
    btn_text_det = st.button("Text detector", type="primary", on_click=textdetector)   
    btn_transl = st.button("Translation", type="primary", on_click=translation)
    btn_class3 = st.button("Classificatore3", type="primary", on_click=classificatore3)
    btn_risp =st.button("Risponditore", type="primary", on_click=risponditore)
    btn_conv = st.button("Conversational 4", type="primary", on_click=conversational4)

#st.sidebar.button("my button")








