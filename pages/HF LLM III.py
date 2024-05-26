import requests
import json
import streamlit as st
import time

st.title("HF solo - LLM gpt2-medium")


API_URL = "https://api-inference.huggingface.co/models/gpt2-medium"
HEADERS = {
    "Authorization": " Bearer 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"  # sostituisci con la tua chiave API
}

# GPT-2 Medium is the 355M parameter version of GPT-2, a transformer-based language model created 
# and released by OpenAI. The model is a pretrained model on English language using a causal language 
# modeling (CLM) objective.

""" API_URL = "https://api-inference.huggingface.co/models/falcon-7b"
HEADERS = {
    "Authorization": "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"  # sostituisci con la tua chiave API
} """

#===================================================================================================
#I modelli sono in questa pagina:
#https://huggingface.co/models?sort=trending&search=gpt2
#===================================================================================================

def query_model(prompt, max_length, temperature, top_k, top_p, num_return_sequences):
    """
    Invia una richiesta al modello LLM attraverso le API cloud di Hugging Face.

    Parametri:
    - prompt: il testo di input per il modello.
    - max_length: lunghezza massima dell'output.
    - temperature: valore che influenza la casualità delle risposte. Valori più alti rendono l'output più casuale.
    - top_k: numero massimo di parole da considerare durante la generazione di testo.
    - top_p: probabilità cumulativa delle parole da considerare (filtraggio "nucleus").
    - num_return_sequences: numero di sequenze da generare.
    """
    
    payload = {
        "inputs": prompt,
        "max_length": max_length,
        "temperature": temperature,
        "top_k": top_k,
        "top_p": top_p,
        "num_return_sequences": num_return_sequences
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    
    if response.status_code == 200:
        return [item['generated_text'] for item in response.json()]
    else:
        st.write("Errore:", response.status_code, response.text)
        return None

# Esempio di utilizzo
prompt = "Once upon a time"
generated_texts = query_model(prompt, max_length=150, temperature=0.8, top_k=40, top_p=0.75, num_return_sequences=3)

print(generated_texts)
""" for idx, text in enumerate(generated_texts, 1):
    st.write(f"Generazione {idx}: {text}\n") """
