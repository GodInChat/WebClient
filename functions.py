import streamlit as st
import json
import requests
from settings import settings as setting
from api_routes import routes as route


base_url = setting.api_base_url

init_chat_route = base_url + route.chat_init
get_all_chats_route = base_url + route.chat_get_all
delete_chat_route = base_url + route.chat_delete
delete_pdf_route = base_url + route.pdf_delete
get_all_pdfs_route = base_url + route.pdf_get_all
new_message_route = base_url + route.chat_new_message
upload_file_route = base_url + route.pdf_upload
header = dict()



def init_chat(token):
    header['accept'] = 'application/json'
    header['Authorization'] = 'Bearer ' + token
    response = requests.post(init_chat_route, headers=header, data='')
    return response.json()


def get_all_chats(token):
    header['accept'] = 'application/json'
    header['Authorization'] = 'Bearer ' + token
    response = requests.get(get_all_chats_route, headers=header)
    return response.json()

def delete_chat(token ,chat_id: str):
    params = {"chat_id": chat_id}
    header['accept'] =  "*/*"
    header['Authorization'] = 'Bearer ' + token
    requests.delete(delete_chat_route, headers=header, params=params)

def delete_pdf(token ,pdf_id: str):
    params = {"pdf_id": pdf_id}
    header['accept'] =  "*/*"
    header['Authorization'] = 'Bearer ' + token
    requests.delete(delete_pdf_route, headers=header, params=params)


def get_all_pdfs(token):
    header['accept'] = 'application/json'
    header['Authorization'] = 'Bearer ' + token
    response = requests.get(get_all_pdfs_route, headers=header)
    return response.json()

def new_message(token, chat_id, pdf_id, human_question):
    header['accept'] = 'application/json'
    header['Authorization'] = 'Bearer ' + token
    header['Content-Type'] = 'application/json'
    data = {"chat_id": chat_id, "human_question": human_question, "pdf_id": pdf_id}
    response = requests.post(new_message_route,headers=header, data=json.dumps(data))
    return response.json()

def upload_file(token, file):
    header['accept'] = 'application/json'
    header['Authorization'] = 'Bearer ' + token
    # header['Content-Type'] = 'multipart/form-data'
    files = {'pdf_file': (file.name, file, 'application/pdf')}
    response = requests.post(upload_file_route, headers=header, files=files, data='')
    return response
