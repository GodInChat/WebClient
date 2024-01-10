import streamlit as st
import requests
from settings import settings as setting
from api_routes import routes as route

base_url = setting.api_base_url
register_route = base_url + route.new_register

st.set_page_config(page_title="InChat Registration", page_icon="📝")
st.title("User Registration")

with st.form("registration_form"):
    email_register = st.text_input("Email")
    password_register = st.text_input("Password", type="password")
    password_register_repeat = st.text_input("Retype Password", type="password")
    submit_button_register = st.form_submit_button("Register")

if submit_button_register:
    if password_register != password_register_repeat:
        st.error("Passwords do not match")
    elif email_register and password_register:
        data = {"email": email_register, "password": password_register}
        response = requests.post(register_route, json=data)
        if response.status_code == 201:
            st.success("Registration successful!")
        else:
            st.error("Registration failed. Please try again.")
    else:
        st.error("Please fill out all fields.")