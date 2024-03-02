import streamlit as st
import prompt_lib as glib

model_options_dict = {
    "anthropic.claude-v2:1": "Claude",
    "cohere.command-text-v14": "Command",
    "ai21.j2-ultra-v1": "Jurassic",
    "meta.llama2-13b-chat-v1": "Llama",
    "amazon.titan-text-express-v1": "Titan"
}

model_options = list(model_options_dict)

def get_model_label(model_id):
    return model_options_dict[model_id]
    

st.set_page_config(page_title="Prompt Engineering", layout="wide")

#st.title("Prompt Engineering")


#with st.sidebar:
#tab1, tab2, tab3, tab4, tab5 = st.tabs(["Summarization", "Analysis", "Content Creation", "Translation", "Code"])



col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Context")
    
    context_list = glib.get_context_list()
    
    selected_context = st.radio(
        "Lab context:",
        context_list,
        #label_visibility="collapsed"
    )
    
    with st.expander("See context"):
        context_for_lab = glib.get_context(selected_context)
        context_text = st.text_area("Context text:", value=context_for_lab, height=350)


with col2:
    
    
    st.subheader("Prompt & model")
    
    prompt_text = st.text_area("Prompt template text:", height=350)
    
    selected_model = st.radio("Model:", 
        model_options,
        format_func=get_model_label,
        horizontal=True
        #label_visibility="collapsed"
    )
    
    #selected_temperature = st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
    
    process_button = st.button("Run", type="primary")


with col3:
    st.subheader("Result")
    
    if process_button:
        with st.spinner("Running..."):
            response_content = glib.get_text_response(model_id=selected_model, temperature=0.0, template=prompt_text, context=context_text)

            st.write(response_content)
