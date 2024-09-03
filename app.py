import streamlit as st
from openai_api import openai_request


DEFULT_PROMPT = """あなたはPythonプログラマーです。
これから指示されることのコードを示してください。
わからない場合は、無理に答えを出さすずにわからないとといってください。"""

st.title('Streamlit AI Demo')

prompt = st.text_area('Enter a prompt', value=DEFULT_PROMPT, height=150)
text = st.text_area('Enter text', height=200)
models = st.multiselect('Select models', ["GPT-4o", "GPT-4 turbo", "GPT-3.5"])

if text is not None and st.button("AI Search"):
    response_openais: list[tuple[str, str | None]] | None = None
    gpt_models: list[str] = []
    if "GPT-4o" in models:
        gpt_models.append("gpt-4o")
    if "GPT-4 turbo" in models:
        gpt_models.append("gpt-4-turbo")
    if "GPT-3.5" in models:
        gpt_models.append("gpt-3.5-turbo")
    if gpt_models:
        response_openais = list(openai_request(gpt_models, prompt, text))

    st.divider()
    res_texts: list[tuple[str, str, str]] = []
    st.subheader("Text:")
    if response_openais is not None:
        for model, res in response_openais:
            st.write("OpenAI model: ",  model)
            if res is not None:
                st.markdown(res, unsafe_allow_html=True)
                # res_texts.append((model, res_text, res))
                # st.code(res_text, language='text')
            else:
                st.warning("No response")
            st.divider()
    st.divider()
