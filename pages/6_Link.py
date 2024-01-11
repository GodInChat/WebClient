import streamlit as st
from functions import chat_link

st.set_page_config(page_title="InChat")

if 'access_token' in st.session_state:
    with st.form("Chat_link_form"):
        pdf_names = [pdf['pdf_name'] for pdf in st.session_state.my_pdfs]
        pdf_option = st.selectbox('Select Document:', pdf_names)
        current_pdf = next((item for item in st.session_state.my_pdfs if item['pdf_name'] == pdf_option), None)
        text = st.text_input("Text")
        submit_button = st.form_submit_button("Get Link")
        # (token, pdf_id, text)
    if submit_button:
        response = chat_link(st.session_state.access_token,current_pdf['id'], text)
        st.write(response["link_tg"])
else:
    st.error("You are not authorized to access this page.")
