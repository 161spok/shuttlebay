# Contents of ~/my_app/main_page.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page 🎈")
st.sidebar.success("Questa app di esperimenti utilizza RAG. Questo tipo di architettura implica l'utilizzo di diverse tecnologie: ")

st.sidebar.success("1 - raccolta e caricamento dati")
st.sidebar.success("2 - suddivisione documenti in blocchi")
st.sidebar.success("3 - Incorporare e archiviare blocchi")

#st.markdown("# Info 🎈")
#---------------------------------------- inizializzazione sessione --------------------------------
if "my_input" not in st.session_state:
    st.session_state["smy_input"] = ""
    st.session_state["srunpod"] = ""
    st.session_state["sllm"] = ""
    st.session_state["ssystem_prompt"] = ""
    st.session_state["sapi"] = ""

def sub_mitted():
    st.session_state.submitted = True

tab1, tab2, tab3 = st.tabs(["Descrizione problema", "System prompt", "Scelta tools"])

with tab1:
    st.header("Descrizione")
    #my_input = st.text_area("Descrivi quello che deve fare l'applicazione", st.session_state["smy_input"])
    my_input = st.text_area("Descrivi quello che deve fare l'applicazione")    
    submit1 = st.button("Invia", key="1", on_click=sub_mitted)
    st.sidebar.write(my_input)
    st.session_state["smy_input"] = my_input

with tab2:
    st.header("System prompt")
    #system_prompt = st.text_area("Descrivi il prompt di sistema", st.session_state["ssystem_prompt"])
    st.markdown("**Esempio:** Voglio che tu funga da generatore di titoli per i pezzi scritti. Ti fornirò l'argomento e le parole chiave di un articolo e genererai cinque titoli che attirano l'attenzione. Si prega di mantenere il titolo conciso e di meno di 20 parole e di assicurarsi che il significato sia mantenuto. Le risposte utilizzeranno il tipo di lingua dell'argomento. Il mio primo argomento è 'LearnData, una base di conoscenza costruita su VuePress, in cui ho integrato tutti i miei appunti e articoli, facilitandone l'utilizzo e la condivisione.'")
   
    system_prompt = st.text_area("Inserisci il prompt di sistema")
    
    submit2 = st.button("Invia", key="2", on_click=sub_mitted)
    st.sidebar.write(system_prompt)
    st.session_state["ssystem_prompt"] = system_prompt

with tab3:
    st.header("Prompt generator")
    st.page_link("https://emitechlogic.com/blog/building-a-simple-prompt-generator-in-python/", label="Sample prompt-generator 1", icon="1️⃣")
    st.page_link("https://github.com/felipeOliveira-1/gpt_prompt_generator/blob/main/prompt_generator_v5.py", label="Sample prompt-generator 2", icon="2️⃣")
   
    tipo_licenza_llm = st.selectbox("Licenza LLM : ", ['Opensource', 'Commerciale'], index=None, placeholder="Seleziona licenza...")
    tipo_llm         = st.selectbox("Tipo LLM : ", ['Pre addestrato', 'Nuovo'], index=None, placeholder="Seleziona tipo...")
        
    if tipo_llm == 'Pre addestrato':  
            scelta_llm = st.selectbox("LLM disponibili : ", ['Perplexity', 'Claude', 'GPT-3.5', 'GPT-4.0'] , index=None, placeholder="Seleziona LLM...")
            selezione = None
            selezione = st.selectbox("Link scelta LLM : ", ['https://chat.lmsys.org/?leaderboard', 'https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard'] , index=None, placeholder="Seleziona link...")
            
            if selezione == "https://chat.lmsys.org/?leaderboard":
                st.write("1")
                st.page_link("https://chat.lmsys.org/?leaderboard", label="leaderboard", icon="1️⃣")
                components.iframe("https://chat.lmsys.org/?leaderboard", height=500)
            else:
                st.write("2")
                st.page_link("https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard", label="leaderboard", icon="2️⃣")
                components.iframe("https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard", height=500)
                
            dim_llm = st.text_input("Dimensioni LLM : ", st.session_state["sllm"])
            
            submit3 = st.button("Invia", key="3")
        
            if submit3:
                st.session_state["sllm"] = llm
                st.session_state["sllm"] = scelta_llm
                st.write(llm)
                st.write(scelta_llm)
                st.write(dim_llm)
            else:
                st.write("-------------")   

    localizz_llm = st.selectbox("Localizzazione LLM : ", ['Locale', 'Pipeline'], index=None, placeholder="Seleziona localizzazione...")

    if localizz_llm == 'Locale':
            runpod = st.text_input("Inserisci setup Runpod")
            submit4 = st.button("Invia", key="4")
            if submit4:
                st.session_state["srunpod"] = runpod
                #st.sidebar.markdown("# Runpod 🎈")
    
    api_key = st.text_input("Inserisci API Key LLM scelto : ", st.session_state["sapi"])
    submit5 = st.button("Invia", key="5")

    sicurezza = st.selectbox("Pacchetti : ", ['GuardRails AI', 'GuardRails Nemo'], index=None, placeholder="Seleziona pacchetto...")








   







