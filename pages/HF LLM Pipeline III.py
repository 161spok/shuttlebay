from transformers import pipeline
import streamlit as st

st.title("💬 LLM endpoint Pipeline") 
st.write("question-answering pipeline")
st.write("Il modello viene scaricato in locale - per il momento l'istruzione è commentata")
st.write("Model: bert-large-uncased-whole-word-masking-finetuned-squad")
st.write("Contesto = Huggingface is a French company that is pioneering NLP.")
st.write("Question = Where is Huggingface based?")


# Specify the model
model = "bert-large-uncased-whole-word-masking-finetuned-squad"

# Initialize the pipeline
nlp = pipeline('question-answering', model=model)

# Provide a context and a question
context = "Huggingface is a French company that is pioneering NLP."
question = "Where is Huggingface based?"

# Get the answer
#answer = nlp(question=question, context=context)
#st.write(answer)