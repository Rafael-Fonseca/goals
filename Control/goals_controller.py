'''*********************************************************************************************************************
**                         Neste arquivo estão todas as funções de controle do projeto Goals                          **
*********************************************************************************************************************'''
from View.goals_view import *
from Model.goals_model import *


def close():
    exit()


def success(msg="Solicitação realizada com sucesso!"):
    input(msg)
    return main_menu()


def fail(msg="Erro, a operação não pode ser realizada!"):
    input(msg)
    return main_menu()


got_it = {True: success, False: fail}


def sign_up():
    username = ask_string("Nome de usuário: ")
    password = ask_numeric_string("Digite sua senha: ")
# ToDo: Validação de senha válida // ask_password(msg="Digite sua senha: ")
    email = ask_string("Insira seu email: ")
# ToDo: Validação de email válido // ask_email(msg="Insira seu email: ")
    got_it[register(username, password, email)]()


"""
TODO: PARA GARANTIR A RECURSIVIDADE AS FUNÇÕES DAS KEYS 1 ATÉ 6 DEVEM RETORNAR
PARA LOGGED_MENU()
"""
def logged_menu():
    menu_options = {"0": main_menu, "1": add_goal, "2": edit_goals,
                    "3": daily_monitoring, "4": routine,
                    "5": review_results, "6": profile}

    chosen_option = show_menu_options()

    try:
        menu_options[chosen_option]()

    except KeyError:
        fail()
        return logged_menu()


def login():
    login_result = {True: logged_menu, False: fail}
    username = ask_string("Nome de usuário: ")
    password = ask_numeric_string("Digite sua senha: ")

    return login_result[validate_login(username, password)]()

# TODO: DAQUI PARA BAIXO
def forgot_password():
    # ToDo: Pede a credencial do usuário envia e-mail com a senha atual.
    pass


def main_menu():
    first_option = {"0": close, "1": sign_up, "2": login, "3": forgot_password}
    try:
        login_option = show_login_options()
        first_option[login_option]()

    except KeyError:
        return main_menu()


def add_goal():
    ''' ToDo: **********************************************************************************************************
    **  ToDo: Chama create_goal() //    pergunta se quer adicionar outra meta IF TRUE return add_goal()               **
    **  ToDo: ELSE: Retorna ao menu, return bd com as novas metas inclusas                                            **
    **  Todo: *******************************************************************************************************'''
    pass


def create_goal():
    ''' ToDo: **********************************************************************************************************
    **  ToDo: Pede as entradas necessárias para criar um objeto goal / constrói o objeto /                            **
    **  ToDo: pergunta se quer dividir em SubMetas / IF TRUE chama add_sub_goals() ELSE: return Goal                  **
    **  Todo: *******************************************************************************************************'''
    pass


def add_sub_goals(goal):
    ''' ToDo: **********************************************************************************************************
    **  ToDo: Pede as entradas necessárias para criar um objeto subGoal / constrói o objeto /                         **
    **  ToDo: pergunta se quer adicionar nova subGoal / IF TRUE chama add_sub_goals(goal)                             **
    **  ToDo: ELSE: pergunta se quer adicionar outra meta IF TRUE return add_goal                                     **
    **  ToDo: ELSE: Retorna ao menu, return bd com as novas metas inclusas                                            **
    **  Todo: *******************************************************************************************************'''
    pass


def edit_goals():
    ''' ToDo: **********************************************************************************************************
    **  ToDo: Chama uma função de visão que Printa todas as metas, ao lado de um número para ser possível selecionar  **
    **  ToDo: Usa o número selecionado para pegar a Meta que o usuário quer editar / concede a opção de deletar ou    **
    **  ToDo: editar/concluir a Meta, IF Excluir, chama R.N. remove_goal(goal) e printa se foi excluida ou não        **
    **  ToDo: ELSE: chama função de controle create_goal() / da um replace e chama a função de controle que salva no BD*
    **  Todo: *******************************************************************************************************'''
    pass


def daily_monitoring():  # ToDo: A partir daqui fazer estes ToDo abaixo melhor, pq fiquei com preguiça.
    ''' ToDo: **********************************************************************************************************
    **  ToDo: Essa função deve efetuar um checklist para saber se as submetas esperadas foram realizadas              **
    **  ToDo:                                                                                                         **
    **  ToDo:                                                                                                         **
    **  ToDo:                                                                                                         **
    **  Todo: *******************************************************************************************************'''
    pass


def routine():  # A menos que esta função passe a fazer algo, ela deveria estar na camada de visão
    ''' ToDo: **********************************************************************************************************
    **  ToDo: Chama a função da camada de visão que irá printar a rotina pessoal do usuário atrelado as atividades    **
    **  ToDo: que o programa espera que ele execute no dia.                                                           **
    **  ToDo:                                                                                                         **
    **  ToDo:                                                                                                         **
    **  Todo: *******************************************************************************************************'''
    pass


def review_results():
    ''' ToDo: **********************************************************************************************************
    **  ToDo: Printa todas as metas, concluídas ou não, mostra o tempo em adamento ou necessário até a conclusão      **
    **  ToDo:                                                                                                         **
    **  ToDo:                                                                                                         **
    **  ToDo:                                                                                                         **
    **  Todo: *******************************************************************************************************'''
    pass


def profile():
    ''' ToDo: **********************************************************************************************************
    **  ToDo: Entra e printa no perfil do usuário                                                                     **
    **  ToDo:                                                                                                         **
    **  ToDo:                                                                                                         **
    **  ToDo:                                                                                                         **
    **  Todo: *******************************************************************************************************'''
    pass
