import streamlit as st
from functions import upload_file, delete_pdf
st.set_page_config(page_title="InChat files", page_icon="📚")

if 'access_token' in st.session_state:
    uploaded_file = st.file_uploader("Upload PDF file", accept_multiple_files=False)
    if st.button("Upload PDF"):
        if uploaded_file:
            with st.spinner('Pdf is processing...'):
                response = upload_file(st.session_state.access_token, uploaded_file)
                print(response.json())
                if response.status_code == 201:
                    st.session_state.my_pdfs.append(response.json())
                    st.success("Pdf Uploaded and processed Successfully!")
                else:
                    st.error("Something is wrong. Please try again.")
        else:
            st.error("Please choose Pdf!")




    pdf_option = st.radio("List of your pdfs:",[pdf['pdf_name'] for pdf in st.session_state.my_pdfs],index=None)

    if st.button("Delete PDF"):
        current_pdf = next((item for item in st.session_state.my_pdfs if item['pdf_name'] == pdf_option), None)
        if current_pdf:
            delete_pdf(st.session_state.access_token, current_pdf['id'])
            st.session_state.my_pdfs.remove(current_pdf)
            st.rerun()
        else:
            st.error("Please choose PDF.")

else:
    st.error("You are not authorized to access this page.")