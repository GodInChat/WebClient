import streamlit as st

st.set_page_config(page_title="InChat", page_icon="💬")

if 'access_token' in st.session_state:

    chat_ids = [chat['id'] for chat in st.session_state.chats]

    col1, col2, col3 = st.columns([0.7,0.1,0.2])

    with col1:
        chat_option = st.selectbox('Select Chat', chat_ids, label_visibility="collapsed")
    with col2:
        new_button = st.button("New", help='Create new chat')
        if new_button:
            st.session_state.chat_history.append('new chat')
            st.rerun()
    with col3:
        if st.button("Delete"):
            st.session_state.chat_history.remove(chat_option)
            st.rerun()
    st.write('You selected:', chat_option)

    chat  = next((item for item in st.session_state.chats if item['id'] == chat_option), None)  # це костиль




    prompt = st.chat_input("Say something")
    if prompt:
        pass
    if chat:
        for message in chat['messages']:
            st.container(border=True).write(message['text'])

    # st.header("Chat with AI")
    # user_message = st.text_input("Your message to AI")
    # if st.button("Send"):
    #     st.session_state.chat_history.append("You: " + user_message)
    #     st.session_state.chat_history.append("AI: " + user_message)
    #
    # # Display chat history
    # for message in st.session_state.chat_history:
    #     st.text(message)
else:
    st.error("You are not authorized to access this page.")


