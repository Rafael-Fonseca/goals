'''*********************************************************************************************************************
**                         Neste arquivo estão todas as funções de controle do projeto Goals                          **
*********************************************************************************************************************'''
from View.goals_view import *
from Model.goals_model import *


def close():
    exit()


def sign_up():
    username = ask_string("Nome de usuário: ")
    password = ask_numeric_string("Digite sua senha: ")
# ToDo: Validação de senha válida
    email = ask_string("Insira seu email: ")
# ToDo: Validação de email válido

    return register(username, password, email)  # Talvez esteja errado pois a função de controle acaba retornando True or False
# e isso é o modus operandi da função de Model, a função de controle pega dados da visão e passa para a model ou o contrário
# ToDo: Se o escrito acima for verdade, talvez seja necessário um IF onde se o register = True printa sucesso, else printa erro
# ToDo: register() Função Model que retorna True se conseguir cadastrar or False otherwise


def login():
    username = ask_string("Nome de usuário: ")
    password = ask_numeric_string("Digite sua senha: ")

    return validate_login(username, password)
# ToDo: Função Model que retorna True se login Válido or False otherwise


def forgot_password():
    # ToDo: Pede a credencial do usuário envia e-mail com a senha atual.
    pass


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
