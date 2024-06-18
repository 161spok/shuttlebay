# Contents of ~/my_app/main_page.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page 🎈")

st.page_link("https://medium.com/@vipra_singh/building-llm-applications-introduction-part-1-1c90294b155b#4d28", label="Introduzione", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-data-preparation-part-2-b7306d224245", label="Data preparation", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-sentence-transformers-part-3-a9e2529f99c1", label="Sentence transformers", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-vector-database-part-4-2bb29e7c798d", label="Vector database", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-retrieval-search-part-5-c83a7004037d", label="Search & retrieval", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-large-language-models-part-6-ea8bd982bdee", label="LLM", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-open-source-chatbots-part-7-1ca9c3653175", label="Open source RAG", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-evaluation-part-8-fcfa2f22bd1c", label="Evaluation", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-serving-llms-part-9-68baa19cef79", label="Serving LLM", icon="1️⃣")
st.page_link("https://medium.com/@vipra_singh/building-llm-applications-advanced-rag-part-10-ec0fe735aeb1", label="Advanced RAG", icon="1️⃣")


#---------------------------------------- inizializzazione sessione --------------------------------
if "my_input" not in st.session_state:
    st.session_state["smy_input"] = ""
    st.session_state["srunpod"] = ""
    st.session_state["sllm"] = ""
    st.session_state["ssystem_prompt"] = ""
    st.session_state["sapi"] = ""

def sub_mitted():
    st.session_state.submitted = True

tab1, tab2, tab3, tab4 = st.tabs(["FASE 1 - Descrizione problema", "FASE 2 - System prompt", "FASE 3 - Scelta LLM", "FASE 4 - Generazione del prompt"])

with tab1:
    st.header("Descrizione problema")
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
    st.header("Scelta LLM")
   
    tipo_licenza_llm = st.selectbox("Licenza LLM : ", ['Opensource', 'Commerciale'], index=None, placeholder="Seleziona licenza...")
    tipo_llm         = st.selectbox("Tipo LLM : ", ['Pre addestrato', 'Nuovo'], index=None, placeholder="Seleziona tipo...")
        
    if tipo_llm == 'Pre addestrato':  
            scelta_llm = st.selectbox("LLM disponibili : ", ['Perplexity', 'Claude', 'GPT-3.5', 'GPT-4.0'] , index=None, placeholder="Seleziona LLM...")
        
            if scelta_llm:
                st.session_state["sllm"] = scelta_llm
                localizz_llm = None
                localizz_llm = st.selectbox("Localizzazione LLM : ", ['Locale', 'Pipeline'], index=None, placeholder="Seleziona localizzazione...")
                st.session_state["locallm"] = local_llm
                if localizz_llm == 'Locale':
                        runpod = st.text_input("Inserisci setup Runpod")
                        submit4 = st.button("Invia", key="4")
                        if submit4:
                            st.session_state["srunpod"] = runpod
                else:
                    selezione = None
                    selezione = st.selectbox("Link scelta LLM : ", ['https://chat.lmsys.org/?leaderboard', 'https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard'] , index=None, placeholder="Seleziona link...")
                    #st.write(selezione)
                    if selezione == "https://chat.lmsys.org/?leaderboard":
                        #st.write("1")
                        st.page_link("https://chat.lmsys.org/?leaderboard", label="leaderboard", icon="1️⃣")
                        components.iframe("https://chat.lmsys.org/?leaderboard", height=500)
                    elif selezione == "https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard":
                        #st.write("2")
                        st.page_link("https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard", label="leaderboard", icon="2️⃣")
                        components.iframe("https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard", height=500)
                        
                    dim_llm = st.text_input("Dimensioni LLM : ", st.session_state["sllm"])
                    submit3 = st.button("Invia", key="3")
                
                    if submit3:
                        st.session_state["dimllm"] = dim_llm
                       
                        #st.write(llm)
                        #st.write(scelta_llm)
                        #st.write(dim_llm)
                    else:
                        st.write("-------------")   
                      
                    api_key = st.text_input("Inserisci API Key LLM scelto : ", st.session_state["sapi"])
                    submit5 = st.button("Invia", key="5")
                
                    sicurezza = st.selectbox("Pacchetti : ", ['GuardRails AI', 'GuardRails Nemo'], index=None, placeholder="Seleziona pacchetto...")

with tab4:
    st.header("Generazione prompt")
    st.page_link("https://emitechlogic.com/blog/building-a-simple-prompt-generator-in-python/", label="Sample prompt-generator 1", icon="1️⃣")
    st.page_link("https://github.com/felipeOliveira-1/gpt_prompt_generator/blob/main/prompt_generator_v5.py", label="Sample prompt-generator 2", icon="2️⃣")





   







