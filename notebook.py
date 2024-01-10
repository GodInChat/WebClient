import streamlit as st
from PIL import Image
import io

# Simulated AI response function (replace with actual AI integration)
def get_ai_response(message):
    return "AI Response to: " + message

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Title of the app
st.title("Streamlit App with AI Chat and PDF Upload")

# Create columns: Left (spacer), Middle (Chat), Right (PDF Upload)
col1, col2, col3 = st.columns([1, 3, 2])

# Section 1: Chat with AI (Middle Column)
with col2:
    st.header("Chat with AI")
    user_message = st.text_input("Your message to AI")
    if st.button("Send"):
        ai_response = get_ai_response(user_message)
        st.session_state.chat_history.append("You: " + user_message)
        st.session_state.chat_history.append("AI: " + ai_response)

    # Display chat history
    for message in st.session_state.chat_history:
        st.text(message)

# Section 2: PDF Upload and Display (Right Column)
with col3:
    st.header("Upload and Display PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        # Display PDF here
        # You can use libraries like PyPDF2 to read and display PDF contents
        st.write("PDF file uploaded successfully.")

# Note: Left column (col1) is used as a spacer