import streamlit as st

st.set_page_config(page_title="InChat files", page_icon="📚")

if 'access_token' in st.session_state:
    del st.session_state.access_token
    del st.session_state.token_type
    del st.session_state.chats
    del st.session_state.my_pdfs
    st.success("You are logged off successfully.")
else:
    st.error("You are not authorized to access this page.")