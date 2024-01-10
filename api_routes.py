from pydantic_settings import BaseSettings


class Routes(BaseSettings):
    login: str = '/auth/jwt/login'
    logout: str = '/auth/jwt/logout'
    new_register: str = '/auth/register'
    
    pdf_upload: str ='/pdf/upload'
    pdf_get_all: str = '/pdf/get_all'
    pdf_delete: str = '/pdf/delete'

    chat_init: str= '/chat/init'
    chat_get_all: str='/chat/get_all'
    chat_new_message: str='/chat/new_message'

routes = Routes()