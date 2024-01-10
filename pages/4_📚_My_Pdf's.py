import streamlit as st

st.set_page_config(page_title="InChat files", page_icon="📚")

if 'access_token' in st.session_state:

    message, status = '', ''
    uploaded_file = st.file_uploader("Upload PDF file", accept_multiple_files=False)


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Upload PDF"):
            if uploaded_file is None:
                message, status = "Please choose Pdf!", 'error'
            else:
                message, status = "Pdf Uploaded Successfully!", 'success'
    with col2:
        if st.button("Delete PDF"):
            pass

    if status == 'error':
        st.error(message)
    else:
        st.success(message)

    genre = st.radio(
        "List of your pdfs:",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        index=None,
    )

    st.write("You selected:", genre)

else:
    st.error("You are not authorized to access this page.")