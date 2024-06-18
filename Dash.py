# Contents of ~/my_app/main_page.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RAG App",
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

st.page_link("pages/avvio.py", label="Avvio")


   







