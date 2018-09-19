'''*********************************************************************************************************************
**                         Neste arquivo estão todas as funções de controle do projeto Goals                          **
*********************************************************************************************************************'''
from ProjetoSemestral.View.goals_view import *


def close():
    exit()


def sign_up():
    username = ask_string("Nome de usuário: ")
    password = ask_numeric_string("Digite sua senha: ")
# ToDo: Validação de senha válida
    email = ask_string("Insira seu email: ")
# ToDo: Validação de email válido

    return register(username, password, email)
# ToDo: Função Model que retorna True se conseguir cadastrar or False otherwise


def login():
    username = ask_string("Nome de usuário: ")
    password = ask_numeric_string("Digite sua senha: ")

    return validate_login(username, password)
# ToDo: Função Model que retorna True se login Válido or False otherwise


def forgot_password():
    pass


def add_goal():
    pass


def edit_goals():
    pass


def remove_goal():
    pass


def daily_monitoring():
    pass

def routine():
    pass


def review_results():
    pass


def profile():
    pass
