import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page 🎈")
#st.sidebar.success("Select a page above.")
#st.markdown("# Main page 🎈")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""
    st.session_state["srunpod"] = ""
    st.session_state["sllm"] = ""

#===========================================================================
def increment_counter():
    st.session_state.count += 1

st.button('Increment', on_click=increment_counter)
#---------------------------------------------------------------------------
def update_first():
    st.session_state.second = st.session_state.first

def update_second():
    st.session_state.first = st.session_state.second

st.title('🪞 Mirrored Widgets using Session State')

st.text_input(label='Textbox 1', key='first', on_change=update_first)
st.text_input(label='Textbox 2', key='second', on_change=update_second)
#----------------------------------------------------------------------------
if 'user_inputs' not in st.session_state:
    st.session_state['user_inputs'] = []
 
user_input = st.text_input("Enter some text")

if user_input:
    st.session_state['user_inputs'].append(user_input)
 
st.write(f"You entered: {st.session_state['user_inputs']}")
#------------------------------------------------------------------------------
if 'my_var' not in st.session_state:
    st.session_state['my_var'] = 0
 
user_input = st.text_input("Enter some text")

if user_input:
    st.session_state['my_var'].append(user_input)
 
st.write(f"You entered: {st.session_state['my_var']}")
#-----------------------------------------------------------------------------
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''
 
user_input = st.text_input("Enter some text")

if user_input:
    st.session_state['user_input'] = user_input
 
st.write(f"You entered: {st.session_state['user_input']}")
#=====================================================================================