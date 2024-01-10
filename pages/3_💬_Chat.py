import streamlit as st
from functions import init_chat, delete_chat, new_message

st.set_page_config(page_title="InChat", page_icon="💬")

if 'access_token' in st.session_state:

    col1, col2, col3 = st.columns([0.7,0.1,0.2])

    with col1:
        chat_ids = [chat['id'] for chat in st.session_state.chats]
        chat_option = st.selectbox('Select Chat', chat_ids, label_visibility="collapsed")
        current_chat = next((item for item in st.session_state.chats if item['id'] == chat_option), None)  # це костиль
    with col2:
        if st.button("New", help='Create new chat.'):
            new_chat = init_chat(st.session_state.access_token)
            st.session_state.chats.append(new_chat)
            st.rerun()
    with col3:
        if st.button("Delete", help='Delete selected chat.'):
            if current_chat:
                delete_chat(st.session_state.access_token, current_chat['id'])
                st.session_state.chats.remove(current_chat)
                st.rerun()

    pdf_names = [pdf['pdf_name'] for pdf in st.session_state.my_pdfs]
    pdf_option = st.selectbox('Select Document', pdf_names)
    current_pdf = next((item for item in st.session_state.my_pdfs if item['pdf_name'] == pdf_option), None)

    prompt = st.chat_input("Say something")
    if prompt:
        if current_chat and current_pdf:
            with st.spinner('Wait for it...'):
                current_chat['messages'].append({'text': prompt, 'owner_type': 'HumanMessage'})
                respond = new_message(st.session_state.access_token, current_chat['id'], current_pdf['id'], prompt)
                current_chat['messages'].append({'text': respond['ai_answer'], 'owner_type': 'AiMessage'})
        else:
            st.error('Choose Chant and Pdf.')

    if current_chat:
        for message in current_chat['messages']:
            # st.text(('You: ' if message['owner_type'] == 'HumanMessage' else 'Ai: ') + message['created_at'])
            st.text('You: ' if message['owner_type'] == 'HumanMessage' else 'Ai: ')
            st.container(border=True).write(message['text'])

else:
    st.error("You are not authorized to access this page.")


