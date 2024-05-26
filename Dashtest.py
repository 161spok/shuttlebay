# Contents of ~/my_app/main_page.py
import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page 🎈")
#st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""
    st.session_state["srunpod"] = ""
    st.session_state["sllm"] = ""

my_input = st.text_input("Descrivi quello che deve fare l'applicazione", st.session_state["my_input"])
submit = st.button("Invia")
st.write(my_input)


st.session_state["my_input"] = my_input

if submit:
    st.session_state.submitted = True

if 'submitted' in st.session_state:
#if submit:   
    tipo_licenza_llm = st.selectbox("Licenza LLM : ", ['Opensource', 'Commerciale'], index=None, placeholder="Seleziona licenza...")
    st.write(tipo_licenza_llm)
    tipo_llm = st.selectbox("Tipo LLM : ", ['Pre addestrato', 'Nuovo'], index=None, placeholder="Seleziona tipo...")
    st.write(tipo_llm)







