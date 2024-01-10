import streamlit as st

if st.session_state.access_token:
    st.session_state.access_token = None
    st.session_state.token_type = None
    st.session_state.chats = []
    st.session_state.my_pdfs = []