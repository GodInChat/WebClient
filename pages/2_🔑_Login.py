import streamlit as st
import requests
from settings import settings as setting
from api_routes import routes as route

from functions import get_all_chats, get_all_pdfs

base_url = setting.api_base_url
login_route = base_url + route.login
data = {
    "grant_type": "",
    "username": "",
    "password": "",
    "scope": "",
    "client_id": "",
    "client_secret": ""
}
headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

st.set_page_config(page_title="InChat Login", page_icon="🔑")
st.title("User Login")


with st.form("login_form"):
    email_login = st.text_input("Email")
    password_login = st.text_input("Password", type="password")

    submit_button_login = st.form_submit_button("Login")


if submit_button_login:

    if email_login and password_login:
        data["username"] = email_login
        data["password"] = password_login
        response = requests.post(login_route, data=data, headers=headers)
        if response.status_code == 200:
            st.success("login successful")
            response_json = response.json()
            st.session_state.access_token = response_json["access_token"]
            st.session_state.token_type = response_json["token_type"]
            st.session_state.chats = get_all_chats(response_json["access_token"])
            st.session_state.my_pdfs = get_all_pdfs(response_json["access_token"])
        else:
            st.error("login failed.")
    else:
        st.error("Please fill out all fields.")